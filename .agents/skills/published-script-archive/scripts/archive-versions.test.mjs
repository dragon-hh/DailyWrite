import assert from 'node:assert/strict';
import { execFileSync } from 'node:child_process';
import { createHash } from 'node:crypto';
import { promises as fs } from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import test from 'node:test';

const script = fileURLToPath(new URL('./archive-versions.mjs', import.meta.url));
const hash = value => createHash('sha256').update(value).digest('hex');

test('plans read-only, archives a verified video variant, and rejects a mismatched published body', async t => {
  const sandbox = await fs.mkdtemp(path.join(os.tmpdir(), 'dailywrite-archive-skill-'));
  t.after(async () => {
    const realSandbox = await fs.realpath(sandbox);
    const realTemp = await fs.realpath(os.tmpdir());
    if (path.dirname(realSandbox) !== realTemp) throw new Error('refusing to remove non-temp fixture');
    await fs.rm(realSandbox, { recursive: true, force: true });
  });
  const root = path.join(sandbox, 'DailyWrite');
  const archive = path.join(sandbox, 'cold-archive');
  const final = '01-内容生产/01-脚本创作中/视频-最终.md';
  const variant = '01-内容生产/01-脚本创作中/视频-v1.md';
  const body = '03-已发布归档/已发布成品/DW-TEST-01.md';
  const content = '# 已发布视频\n\n这是确认的发布正文。\n';
  const createFile = async (relative, text) => {
    const target = path.join(root, relative);
    await fs.mkdir(path.dirname(target), { recursive: true });
    await fs.writeFile(target, text);
  };
  await createFile(final, content);
  await createFile(variant, '# 历史稿\n');
  await createFile(body, content);
  const delivery = { schemaVersion: 1, contents: { 'DW-TEST-01': { publication: { sourcePath: final, bodyPath: body, sha256: hash(content) } } }, files: { [final]: { path: final } } };
  const index = `# 内容主索引\n| content_id | 主题 | 状态 |\n|---|---|---|\n| DW-TEST-01 | 视频 | 已发布 |\n\n<!-- dailywrite-delivery:v1 -->\n\`\`\`json\n${JSON.stringify(delivery)}\n\`\`\`\n`;
  await createFile('00-内容资产索引/内容主索引.md', index);
  const planFile = path.join(sandbox, 'plan.json');
  await fs.writeFile(planFile, JSON.stringify({ schemaVersion: 1, groups: [{ contentId: 'DW-TEST-01', finalSource: final, variants: [variant] }] }));
  const run = mode => JSON.parse(execFileSync(process.execPath, [script, mode, '--root', root, '--archive', archive, '--plan', planFile], { encoding: 'utf8' }));
  assert.equal(run('plan').variants, 1);
  assert.equal(await fs.readFile(path.join(root, variant), 'utf8'), '# 历史稿\n');
  assert.equal(await fs.stat(archive).then(() => true, () => false), false);

  await fs.writeFile(path.join(root, body), '# 不一致的正文\n');
  assert.throws(() => run('apply'), /final\/body\/publication hash mismatch/);
  assert.equal(await fs.stat(archive).then(() => true, () => false), false);
  await fs.writeFile(path.join(root, body), content);

  const applied = run('apply');
  assert.equal(applied.state, 'complete');
  assert.equal(applied.archived, 1);
  assert.equal(await fs.stat(path.join(root, variant)).then(() => true, () => false), false);
  assert.equal(await fs.readFile(path.join(archive, 'DW-TEST-01', '视频-v1.md'), 'utf8'), '# 历史稿\n');
  assert.equal(JSON.parse(execFileSync(process.execPath, [script, 'verify', '--archive', archive], { encoding: 'utf8' })).archived, 1);
  assert.throws(() => run('apply'), /archive directory already exists/);
});
