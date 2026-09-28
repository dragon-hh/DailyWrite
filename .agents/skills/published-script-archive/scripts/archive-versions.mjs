import { createHash } from 'node:crypto';
import { promises as fs } from 'node:fs';
import path from 'node:path';

function fail(message) { throw new Error(message); }
function sha256(bytes) { return createHash('sha256').update(bytes).digest('hex'); }
function inside(base, target) {
  const relative = path.relative(base, target);
  return relative === '' || (relative !== '..' && !relative.startsWith(`..${path.sep}`) && !path.isAbsolute(relative));
}
function relativeFile(root, value, label) {
  if (typeof value !== 'string' || !value || path.isAbsolute(value) || value.includes('\\') || value.split('/').some(part => part === '..' || part === '.')) fail(`${label}: invalid relative path`);
  const absolute = path.resolve(root, value);
  if (!inside(root, absolute) || absolute === root || path.extname(absolute).toLowerCase() !== '.md') fail(`${label}: must be a Markdown file inside root`);
  return absolute;
}
async function fileInfo(file, label) {
  const stat = await fs.lstat(file).catch(error => fail(`${label}: ${error.message}`));
  if (!stat.isFile() || stat.isSymbolicLink()) fail(`${label}: regular file required`);
  const bytes = await fs.readFile(file);
  return { sha256: sha256(bytes), bytes: bytes.length, modifiedAt: stat.mtime.toISOString() };
}
function args() {
  const [mode, ...rest] = process.argv.slice(2);
  if (!['plan', 'apply', 'verify'].includes(mode)) fail('mode must be plan, apply, or verify');
  const options = {};
  for (let i = 0; i < rest.length; i += 2) {
    const key = rest[i];
    if (!['--root', '--archive', '--plan'].includes(key) || !rest[i + 1] || options[key]) fail(`invalid argument: ${key}`);
    options[key] = rest[i + 1];
  }
  if (!options['--archive'] || (mode !== 'verify' && (!options['--root'] || !options['--plan']))) fail('missing --archive, --root, or --plan');
  return { mode, options };
}
async function prepare(root, archive, planPath) {
  if (inside(root, archive)) fail('archive must be outside DailyWrite root');
  const plan = JSON.parse(await fs.readFile(planPath, 'utf8'));
  if (plan.schemaVersion !== 1 || !Array.isArray(plan.groups) || !plan.groups.length) fail('invalid plan schema');
  const index = await fs.readFile(path.join(root, '00-内容资产索引', '内容主索引.md'), 'utf8');
  const match = index.match(/<!-- dailywrite-delivery:v1 -->\s*```json\s*([\s\S]*?)\s*```/);
  if (!match) fail('delivery metadata missing');
  const delivery = JSON.parse(match[1]);
  const protectedPaths = new Set(Object.keys(delivery.files || {}));
  for (const content of Object.values(delivery.contents || {})) {
    if (content.publication?.sourcePath) protectedPaths.add(content.publication.sourcePath);
    if (content.publication?.bodyPath) protectedPaths.add(content.publication.bodyPath);
    for (const item of content.artifacts || []) if (item.path) protectedPaths.add(item.path);
  }
  const seenIds = new Set();
  const seenPaths = new Set();
  const groups = [];
  for (const group of plan.groups) {
    const { contentId, finalSource, variants } = group;
    if (typeof contentId !== 'string' || !/^DW-[A-Za-z0-9-]+$/.test(contentId) || seenIds.has(contentId)) fail(`invalid or duplicate contentId: ${contentId}`);
    seenIds.add(contentId);
    if (!Array.isArray(variants) || !variants.length) fail(`${contentId}: no variants`);
    const publication = delivery.contents?.[contentId]?.publication;
    if (!publication || publication.sourcePath !== finalSource) fail(`${contentId}: final source does not match publication`);
    const scriptDirectory = value => value.startsWith('01-内容生产/01-脚本创作中/') || value.startsWith('01-内容生产/02-待拍摄/');
    if (!scriptDirectory(finalSource)) fail(`${contentId}: final must be in a script directory`);
    const publishedRow = index.split('\n').find(line => line.startsWith(`| ${contentId} |`));
    if (!publishedRow || !publishedRow.includes('| 已发布 |')) fail(`${contentId}: published index row missing`);
    const finalFile = relativeFile(root, finalSource, `${contentId} final`);
    const final = await fileInfo(finalFile, `${contentId} final`);
    const bodyFile = relativeFile(root, publication.bodyPath, `${contentId} body`);
    const body = await fileInfo(bodyFile, `${contentId} body`);
    if (final.sha256 !== body.sha256 || final.sha256 !== publication.sha256) fail(`${contentId}: final/body/publication hash mismatch`);
    const entries = [];
    for (const source of variants) {
      if (typeof source !== 'string' || !scriptDirectory(source)) fail(`${contentId}: variant must be in a script directory`);
      const sourceFile = relativeFile(root, source, `${contentId} variant`);
      if (source === finalSource || protectedPaths.has(source) || seenPaths.has(source)) fail(`${contentId}: variant is current or repeated: ${source}`);
      seenPaths.add(source);
      const info = await fileInfo(sourceFile, `${contentId} variant ${source}`);
      const destination = path.join(archive, contentId, path.basename(sourceFile));
      if (await fs.stat(destination).then(() => true, error => error.code === 'ENOENT' ? false : Promise.reject(error))) fail(`${contentId}: destination exists: ${destination}`);
      entries.push({ source: sourceFile, destination, relative: source, ...info, state: 'planned' });
    }
    const names = entries.map(item => path.basename(item.destination));
    if (new Set(names).size !== names.length) fail(`${contentId}: duplicate archive filenames`);
    groups.push({ contentId, finalSource, finalSha256: final.sha256, publishedBody: publication.bodyPath, variants: entries });
  }
  return { schemaVersion: 1, root, archiveRoot: archive, createdAt: new Date().toISOString(), state: 'planned', groups };
}
async function saveManifest(file, manifest) {
  const temporary = `${file}.tmp`;
  await fs.writeFile(temporary, `${JSON.stringify(manifest, null, 2)}\n`, { flag: 'wx' });
  await fs.rename(temporary, file);
}
async function replaceManifest(file, manifest) {
  const temporary = `${file}.tmp`;
  await fs.writeFile(temporary, `${JSON.stringify(manifest, null, 2)}\n`, { flag: 'wx' });
  await fs.rename(temporary, file);
}
async function verify(archive) {
  const manifest = JSON.parse(await fs.readFile(path.join(archive, 'manifest.json'), 'utf8'));
  if (path.resolve(manifest.archiveRoot) !== archive || !Array.isArray(manifest.groups)) fail('manifest does not match archive');
  let archived = 0;
  let planned = 0;
  for (const group of manifest.groups) {
    const final = await fileInfo(relativeFile(manifest.root, group.finalSource, 'final'), 'final');
    const body = await fileInfo(relativeFile(manifest.root, group.publishedBody, 'body'), 'body');
    if (final.sha256 !== group.finalSha256 || body.sha256 !== group.finalSha256) fail(`${group.contentId}: final/body changed`);
    for (const item of group.variants) {
      if (!inside(archive, item.destination)) fail('variant destination outside archive');
      if (item.state === 'archived') {
        const info = await fileInfo(item.destination, 'archived variant');
        if (info.sha256 !== item.sha256 || info.bytes !== item.bytes) fail(`${item.relative}: archived hash mismatch`);
        if (await fs.stat(item.source).then(() => true, error => error.code === 'ENOENT' ? false : Promise.reject(error))) fail(`${item.relative}: source still exists`);
        archived++;
      } else if (item.state === 'planned') {
        const info = await fileInfo(item.source, 'planned variant');
        if (info.sha256 !== item.sha256 || info.bytes !== item.bytes) fail(`${item.relative}: planned source changed`);
        planned++;
      } else fail(`${item.relative}: invalid state`);
    }
  }
  if ((manifest.state === 'complete') !== (planned === 0)) fail('manifest completion state mismatch');
  return { ok: true, state: manifest.state, groups: manifest.groups.length, archived, planned, manifest: path.join(archive, 'manifest.json') };
}

try {
  const { mode, options } = args();
  const archive = path.resolve(options['--archive']);
  if (mode === 'verify') {
    console.log(JSON.stringify(await verify(archive)));
  } else {
    const root = await fs.realpath(options['--root']);
    if (mode === 'apply' && await fs.stat(archive).then(() => true, error => error.code === 'ENOENT' ? false : Promise.reject(error))) fail('archive directory already exists; inspect it before any retry');
    const manifest = await prepare(root, archive, path.resolve(options['--plan']));
    const count = manifest.groups.reduce((sum, group) => sum + group.variants.length, 0);
    if (mode === 'plan') {
      console.log(JSON.stringify({ ok: true, mode, groups: manifest.groups.length, variants: count, archive }));
    } else {
      await fs.mkdir(archive, { recursive: true });
      const manifestPath = path.join(archive, 'manifest.json');
      await saveManifest(manifestPath, manifest);
      for (const group of manifest.groups) {
        await fs.mkdir(path.join(archive, group.contentId), { recursive: true });
        for (const item of group.variants) {
          const current = await fileInfo(item.source, 'variant before move');
          if (current.sha256 !== item.sha256 || current.bytes !== item.bytes) fail(`${item.relative}: source changed before move`);
          await fs.rename(item.source, item.destination);
          const moved = await fileInfo(item.destination, 'variant after move');
          if (moved.sha256 !== item.sha256 || moved.bytes !== item.bytes) fail(`${item.relative}: destination hash mismatch`);
          item.state = 'archived';
          item.archivedAt = new Date().toISOString();
          await replaceManifest(manifestPath, manifest);
        }
      }
      manifest.state = 'complete';
      manifest.completedAt = new Date().toISOString();
      await replaceManifest(manifestPath, manifest);
      console.log(JSON.stringify(await verify(archive)));
    }
  }
} catch (error) {
  console.error(JSON.stringify({ ok: false, error: error.message }));
  process.exitCode = 1;
}
