import assert from 'node:assert/strict';
import { readFile, writeFile } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { sha256, withWorkspaceLock, commitWorkspaceFiles } from '../../90-工具项目/dailywrite-workbench/server/workspaceTransaction.mjs';
import { readDeliveryMetadata, writeDeliveryMetadata } from '../../90-工具项目/dailywrite-workbench/shared/deliveryModel.js';

const runDir = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(runDir, '../..');
assert.equal(root, String.raw`E:\projects\knowledgeProjects\DailyWrite`);
const plan = JSON.parse(await readFile(path.join(runDir, 'plan.json'), 'utf8'));
const indexPath = '00-内容资产索引/内容主索引.md';
const receiptPath = path.join(runDir, 'receipt.json');
let receipt;
await withWorkspaceLock(root, async () => {
  const raw = await readFile(path.join(root, indexPath), 'utf8');
  assert.equal(sha256(raw), plan.expectedRevision, 'Index version changed');
  assert.equal(raw.split('<!-- dailywrite-delivery:v1 -->')[0], plan.beforePrefix);
  assert.equal(sha256(await readFile(plan.source)), plan.sourceSha256);
  for (const [relative, hash] of Object.entries(plan.protectedHashes)) {
    assert.equal(sha256(await readFile(path.join(root, relative))), hash, `Protected file changed: ${relative}`);
  }
  for (const change of plan.changes) {
    assert(!change.content.includes('\r\r\n'), `Invalid line endings: ${change.path}`);
    if (change.expectedHash === null) {
      let existing;
      try { existing = await readFile(path.join(root, change.path)); }
      catch (error) { if (error.code !== 'ENOENT') throw error; }
      assert.equal(existing, undefined, `New file already exists: ${change.path}`);
    } else {
      assert.equal(sha256(await readFile(path.join(root, change.path))), change.expectedHash, `Write target changed: ${change.path}`);
    }
  }
  const beforeMeta = readDeliveryMetadata(raw);
  assert(!beforeMeta.receipts.some(item => item.id === plan.requestId), 'Request already recorded; inspect receipt instead of retrying');
  const nextMeta = structuredClone(beforeMeta);
  for (const episode of plan.episodes) {
    assert.equal(nextMeta.contents[episode.id].publication.dataPath, episode.oldPath);
    assert.equal(nextMeta.contents[episode.id].publication.sha256, episode.bodySha256);
    nextMeta.contents[episode.id].publication.dataPath = episode.path;
  }
  const operation = { type: 'douyin-episode-files', source: plan.source, sourceSha256: plan.sourceSha256, files: plan.episodes.map(e => ({ contentId: e.id, dataPath: e.path, bodySha256: e.bodySha256, sourceRow: e.sourceRow })) };
  const indexReceipt = { id: plan.requestId, fingerprint: sha256(JSON.stringify(operation)), at: new Date().toISOString(), type: operation.type, result: { addedEpisodeFiles: 11, totalEpisodeFiles: 33, exportPublicWorks: 30, exportSelfVisibleWorks: 2, notInExport: 1, dataPaths: Object.fromEntries(plan.episodes.map(e => [e.id, e.path])) } };
  nextMeta.receipts.push(indexReceipt);
  const prefixUpdated = plan.afterPrefix + raw.slice(plan.beforePrefix.length);
  const nextRaw = writeDeliveryMetadata(prefixUpdated, nextMeta);
  assert.equal(nextRaw.split('<!-- dailywrite-delivery:v1 -->')[0], plan.afterPrefix);
  const changes = [...plan.changes, { path: indexPath, expectedHash: plan.expectedRevision, content: nextRaw }];
  assert.equal(new Set(changes.map(c => c.path)).size, changes.length);
  receipt = { schemaVersion: 1, requestId: plan.requestId, state: 'prepared', expectedRevision: plan.expectedRevision, operation, result: indexReceipt.result, at: indexReceipt.at };
  await writeFile(receiptPath, JSON.stringify(receipt, null, 2), { flag: 'wx' });
  try {
    const historyRoot = path.join(process.env.LOCALAPPDATA, 'DailyWriteWorkbench', 'content-history');
    receipt.journalPath = await commitWorkspaceFiles(root, changes, { requestId: plan.requestId, historyRoot });
    const actual = await readFile(path.join(root, indexPath), 'utf8');
    const readMeta = readDeliveryMetadata(actual);
    assert.deepEqual(readMeta, nextMeta, 'Delivery metadata readback failed');
    readMeta.receipts.pop();
    for (const episode of plan.episodes) readMeta.contents[episode.id].publication.dataPath = episode.oldPath;
    assert.deepEqual(readMeta, beforeMeta, 'Unrelated delivery metadata changed');
    for (const change of changes) assert.equal(sha256(await readFile(path.join(root, change.path))), sha256(change.content), `Readback failed: ${change.path}`);
    for (const [relative, hash] of Object.entries(plan.protectedHashes)) assert.equal(sha256(await readFile(path.join(root, relative))), hash, `Protected file changed after write: ${relative}`);
    receipt.state = 'committed';
    receipt.revision = sha256(actual);
    receipt.changedFiles = changes.map(c => c.path);
    receipt.readbackVerified = true;
    await writeFile(receiptPath, JSON.stringify(receipt, null, 2));
  } catch (error) {
    receipt.state = 'verification-or-transaction-failed';
    receipt.error = error.message;
    await writeFile(receiptPath, JSON.stringify(receipt, null, 2));
    throw error;
  }
}, plan.requestId);
console.log(JSON.stringify({ ok: receipt.state === 'committed', ...receipt.result, changedFiles: receipt.changedFiles.length, readbackVerified: receipt.readbackVerified, journalPath: receipt.journalPath }));
