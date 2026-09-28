from pathlib import Path
from decimal import Decimal, ROUND_HALF_UP
import hashlib
import json
import re
import sys
import openpyxl

sys.stdout.reconfigure(encoding='utf-8')
ROOT = Path(r'E:\projects\knowledgeProjects\DailyWrite')
RUN = ROOT / 'output/douyin-episode-files-20260929'
plan = json.loads((RUN / 'plan.json').read_text(encoding='utf-8'))
receipt = json.loads((RUN / 'receipt.json').read_text(encoding='utf-8'))
assert receipt['state'] == 'committed' and receipt['readbackVerified']
def sha(data):
    return hashlib.sha256(data).hexdigest()

assert sha(Path(plan['source']).read_bytes()) == plan['sourceSha256']
workbook = openpyxl.load_workbook(plan['source'], read_only=True, data_only=True)
rows = list(workbook.active.values)
workbook.close()
index = (ROOT / '00-内容资产索引/内容主索引.md').read_bytes().decode('utf-8')
assert sha(index.encode()) == receipt['revision']
meta = json.loads(re.search(r'<!-- dailywrite-delivery:v1 -->\s*```json\s*(.*?)\s*```', index, re.S).group(1))
assert sum(r['id'] == plan['requestId'] for r in meta['receipts']) == 1
metric_keys = {'点赞':'点赞量','评论':'评论量','收藏':'收藏量','分享':'分享量','主页访问量':'主页访问量','涨粉量':'粉丝增量','播放量':'播放量'}
for episode in plan['episodes']:
    raw = (ROOT / episode['path']).read_bytes()
    text = raw.decode('utf-8')
    marker = b'## ' + '文案内容'.encode() + b'\n\n'
    assert raw.count(marker) == 1
    body = raw.split(marker, 1)[1]
    assert body == (ROOT / episode['bodyPath']).read_bytes()
    assert sha(body) == episode['bodySha256'] == meta['contents'][episode['id']]['publication']['sha256']
    assert meta['contents'][episode['id']]['publication']['dataPath'] == episode['path']
    match = re.search(r'## 视频数据\n\n(.*?)\n\n---', text, re.S)
    metrics = dict(line.split('：', 1) for line in match.group(1).splitlines())
    if episode['sourceRow'] is not None:
        source = dict(zip(rows[0], rows[episode['sourceRow'] - 1]))
        assert source['审核状态'] == metrics['审核状态'] == '公开'
        assert metrics['发布时间'] == source['发布时间']
        assert metrics['体裁'] == source['体裁']
        for label, column in metric_keys.items():
            assert Decimal(metrics[label]) == Decimal(str(source[column]))
        for label in ['完播率','5s完播率','封面点击率','2s跳出率']:
            expected = '—' if source[label] in (None,'','-','—') else f'{(Decimal(str(source[label])) * 100).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP):.2f}%'
            assert metrics[label] == expected
        expected_seconds = '—' if source['平均播放时长'] in (None,'','-','—') else f'{Decimal(str(source["平均播放时长"])).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP):.2f}秒'
        assert metrics['平均播放时长'] == expected_seconds
    else:
        assert metrics['播放量'] == '7'
        assert all(metrics[key] == '待补' for key in ['点赞','评论','收藏','分享','主页访问量','涨粉量','完播率','5s完播率','封面点击率','2s跳出率','平均播放时长','脱粉量'])
        assert '具体时分秒待补' in metrics['发布时间'] and '不计入导出公开作品总计' in text
for relative, hash_value in plan['protectedHashes'].items():
    assert sha((ROOT / relative).read_bytes()) == hash_value, relative
data_dir = ROOT / '04-数据与复盘/抖音数据'
actual_files = {p.name for p in data_dir.glob('*.md')} - {'00-抖音数据汇总表.md','3.5-抖音违规积累.md'}
registry = json.loads((ROOT / '90-工具项目/published-archive-sync/published-works.json').read_text(encoding='utf-8'))
assert len(actual_files) == len(registry) == 33
assert {entry['source'] for entry in registry} == actual_files
assert len({entry['id'] for entry in registry}) == 33
index_rows = [line for line in index.split('## 已发布作品索引')[1].split('## 当前生产索引')[0].splitlines() if line.startswith('| DW-')]
assert len(index_rows) == 33
assert {line.strip('|').split('|')[5].strip().split('/')[-1] for line in index_rows} == actual_files
summary = (data_dir / '00-抖音数据汇总表.md').read_text(encoding='utf-8')
links = re.findall(r'\]\(<([^>]+)>\)', summary)
assert len(links) == 33 and set(links) == actual_files
assert '- 公开作品数：30' in summary and '- 总播放量：4066947' in summary
readme = (ROOT / '03-已发布归档/已发布成品/README.md').read_text(encoding='utf-8')
assert len([line for line in readme.splitlines() if line.startswith('| DW-')]) == 33
journal = json.loads(Path(receipt['journalPath']).read_text(encoding='utf-8'))
assert journal['state'] == 'committed'
assert not (ROOT / '00-内容资产索引/.workbench-write.lock').exists()
verification = {'ok': True, 'newFiles': 11, 'episodeFiles': 33, 'freshExportRowsVerified': 10, 'exactPublishedBodiesVerified': 11, 'summaryLinksVerified': 33, 'indexAndPublicationPathsAligned': True, 'protectedFilesUnchanged': len(plan['protectedHashes']), 'backupTransaction': journal['state']}
(RUN / 'verification.json').write_text(json.dumps(verification, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps(verification, ensure_ascii=False))
