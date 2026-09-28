import assert from 'node:assert/strict';
import { readFile, writeFile } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { sha256, withWorkspaceLock, commitWorkspaceFiles } from '../../90-工具项目/dailywrite-workbench/server/workspaceTransaction.mjs';
import { readDeliveryMetadata, writeDeliveryMetadata } from '../../90-工具项目/dailywrite-workbench/shared/deliveryModel.js';

const runDirectory = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(runDirectory, '../..');
const plan = JSON.parse(await readFile(path.join(runDirectory, 'update-plan.json'), 'utf8'));
assert.equal(root, String.raw`E:\projects\knowledgeProjects\DailyWrite`);
const indexPath = '00-内容资产索引/内容主索引.md';
const receiptPath = path.join(runDirectory, 'receipt.json');
let receipt;
await withWorkspaceLock(root, async () => {
  const beforeRaw = await readFile(path.join(root, indexPath), 'utf8');
  assert.equal(sha256(beforeRaw), plan.expectedRevision, 'Index version changed; nothing has been written');
  assert.equal(sha256(await readFile(plan.source)), plan.sourceSha256, 'Export changed');
  for (const [relative, hash] of Object.entries(plan.protectedHashes)) {
    assert.equal(sha256(await readFile(path.join(root, relative))), hash, `Protected file changed: ${relative}`);
  }
  assert.equal(new Set(plan.changes.map(change => change.path)).size, plan.changes.length);
  for (const change of plan.changes) assert(!change.content.includes('\r\r\n'), `Invalid line endings: ${change.path}`);
  const beforeMeta = readDeliveryMetadata(beforeRaw);
  assert(!beforeMeta.receipts.some(item => item.id === plan.requestId), 'Request already exists; verify receipt instead of retrying');
  const operation = { type: 'douyin-data-refresh', source: plan.source, sourceSha256: plan.sourceSha256, observedDate: plan.observedDate, updatedDate: plan.updatedDate, files: plan.changes.map(change => change.path) };
  const result = { source: plan.source, sourceSha256: plan.sourceSha256, observedDate: plan.observedDate, updatedDate: plan.updatedDate, counts: plan.counts, totals: plan.totals };
  const afterMeta = structuredClone(beforeMeta);
  const indexReceipt = { id: plan.requestId, fingerprint: sha256(JSON.stringify(operation)), at: new Date().toISOString(), type: operation.type, result };
  afterMeta.receipts.push(indexReceipt);
  const afterRaw = writeDeliveryMetadata(beforeRaw, afterMeta);
  assert.equal(afterRaw.split('<!-- dailywrite-delivery:v1 -->')[0], beforeRaw.split('<!-- dailywrite-delivery:v1 -->')[0], 'Index rows must remain unchanged');
  const changes = [...plan.changes, { path: indexPath, expectedHash: plan.expectedRevision, content: afterRaw }];
  receipt = { schemaVersion: 1, requestId: plan.requestId, state: 'prepared', expectedRevision: plan.expectedRevision, operation, result, at: new Date().toISOString() };
  await writeFile(receiptPath, JSON.stringify(receipt, null, 2), { flag: 'wx' });
  try {
    const historyRoot = path.join(process.env.LOCALAPPDATA, 'DailyWriteWorkbench', 'content-history');
    receipt.journalPath = await commitWorkspaceFiles(root, changes, { requestId: plan.requestId, historyRoot });
    const readBack = await readFile(path.join(root, indexPath), 'utf8');
    const readMeta = readDeliveryMetadata(readBack);
    assert.deepEqual(readMeta.receipts.pop(), indexReceipt, 'Index receipt readback failed');
    assert.deepEqual(readMeta, beforeMeta, 'Existing delivery metadata changed');
    for (const change of changes) assert.equal(sha256(await readFile(path.join(root, change.path))), sha256(change.content), `Readback failed: ${change.path}`);
    for (const [relative, hash] of Object.entries(plan.protectedHashes)) {
      if (relative !== indexPath) assert.equal(sha256(await readFile(path.join(root, relative))), hash, `Protected file changed: ${relative}`);
    }
    receipt.state = 'committed';
    receipt.revision = sha256(readBack);
    receipt.changedFiles = changes.map(change => change.path);
    receipt.readbackVerified = true;
    await writeFile(receiptPath, JSON.stringify(receipt, null, 2));
  } catch (error) {
    receipt.state = 'verification-or-transaction-failed';
    receipt.error = error.message;
    await writeFile(receiptPath, JSON.stringify(receipt, null, 2));
    throw error;
  }
}, plan.requestId);
console.log(JSON.stringify({ ok: receipt.state === 'committed', requestId: plan.requestId, counts: plan.counts, totals: plan.totals, readbackVerified: receipt.readbackVerified, journalPath: receipt.journalPath }));
