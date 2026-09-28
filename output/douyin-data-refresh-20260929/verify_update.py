from pathlib import Path
from decimal import Decimal, ROUND_HALF_UP
import base64
import datetime as dt
import hashlib
import json
import re
import sys
import unicodedata
import openpyxl

sys.stdout.reconfigure(encoding='utf-8')
ROOT = Path(r'E:\projects\knowledgeProjects\DailyWrite')
RUN = ROOT/'output/douyin-data-refresh-20260929'
receipt = json.loads((RUN/'receipt.json').read_text(encoding='utf-8'))
assert receipt['state']=='committed' and receipt['readbackVerified'] is True
journal = json.loads(Path(receipt['journalPath']).read_text(encoding='utf-8'))
assert journal['state']=='committed' and journal['entries'][-1]['path']=='00-内容资产索引/内容主索引.md'
source = Path(receipt['result']['source'])
digest = lambda value: hashlib.sha256(value).hexdigest()
assert digest(source.read_bytes()) == receipt['result']['sourceSha256']
assert digest((ROOT/'04-数据与复盘/平台导入/作品列表导出.xlsx').read_bytes()) == receipt['result']['sourceSha256']
book = openpyxl.load_workbook(source,read_only=True,data_only=True)
assert book.sheetnames==['Sheet1']
raw_rows = list(book.active.values)
records = [dict(zip(raw_rows[0],row)) for row in raw_rows[1:]]
for record in records:
    value = record['发布时间']
    record['发布时间'] = value.strftime('%Y-%m-%d %H:%M:%S') if isinstance(value,dt.datetime) else value
book.close()
public = [r for r in records if r['审核状态']=='公开']
assert len(records)==150 and len(public)==30
totals = {key:sum(int(Decimal(r[key])) for r in public) for key in ['播放量','点赞量','收藏量','分享量','评论量','粉丝增量']}
assert totals==receipt['result']['totals']
index = (ROOT/'00-内容资产索引/内容主索引.md').read_text(encoding='utf-8-sig')
metadata = json.loads(re.search(r'<!-- dailywrite-delivery:v1 -->\s*```json\s*(.*?)\s*```',index,re.S)[1])
assert sum(r['id']==receipt['requestId'] for r in metadata['receipts'])==1
index_rows = []
for line in index.split('## 当前生产索引')[0].splitlines():
    if line.startswith('| DW-'):
        fields = [v.strip() for v in line.strip('|').split('|')]
        index_rows.append({'id':fields[0],'dataPath':fields[5]})
by_file = {(ROOT/r['dataPath']).resolve():r['id'] for r in index_rows}
by_id = {}
for record in records:
    raw = json.dumps([unicodedata.normalize('NFC',record['作品名称'].strip()),record['发布时间'].replace(' ','T')+'+08:00',record['体裁'].strip()],ensure_ascii=False,separators=(',',':'))
    key = 'published-'+digest(raw.encode())[:24]
    link = metadata['platformLinks'].get(key)
    if link:
        assert link['contentId'] not in by_id
        by_id[link['contentId']] = record

def percent(value):
    if value in ('-',None,''):
        return '—'
    return str((Decimal(value)*100).quantize(Decimal('0.01'),rounding=ROUND_HALF_UP))+'%'

def seconds(value):
    if value in ('-',None,''):
        return '—'
    return str(Decimal(value).quantize(Decimal('0.01'),rounding=ROUND_HALF_UP))+'秒'

summary_path = ROOT/'04-数据与复盘/抖音数据/00-抖音数据汇总表.md'
summary = summary_path.read_text(encoding='utf-8')
section = summary.split('## 公开作品明细')[1].split('## 历史作品的当前可见性')[0]
table = [line for line in section.splitlines() if line.startswith('| 2026-')]
assert len(table)==30
seen = set()
table_totals = dict.fromkeys(totals,0)
for line in table:
    fields = [field.strip() for field in line.strip('|').split('|')]
    assert len(fields)==13
    relative = re.search(r'\]\(<(.*?)>\)',fields[1])[1]
    target = (summary_path.parent/relative).resolve()
    assert target.is_file() and target.is_relative_to(ROOT)
    cid = by_file[target]
    assert cid not in seen
    seen.add(cid)
    record = by_id[cid]
    assert record['审核状态']=='公开' and fields[0]==record['发布时间'][:10]
    assert fields[3]==record['体裁']
    for column,key in [(4,'播放量'),(8,'点赞量'),(9,'收藏量'),(10,'评论量'),(11,'分享量'),(12,'粉丝增量')]:
        assert fields[column]==str(int(Decimal(record[key]))),(cid,key)
        table_totals[key]+=int(fields[column])
    assert fields[5]==percent(record['完播率'])
    assert fields[6]==percent(record['5s完播率'])
    assert fields[7]==seconds(record['平均播放时长'])
assert table_totals==totals
for label,key in [('总播放量','播放量'),('总点赞','点赞量'),('总收藏','收藏量'),('总分享','分享量'),('总评论','评论量'),('总涨粉','粉丝增量')]:
    assert f'- {label}：{totals[key]}' in summary

verified_legacy = 0
historical_snapshots = 0
for entry in journal['entries']:
    file = ROOT/entry['path']
    actual = file.read_bytes()
    assert digest(actual)==entry['afterHash']
    if '/抖音数据/' not in entry['path'] or entry['path'].endswith('00-抖音数据汇总表.md'):
        continue
    before = base64.b64decode(entry['before']).decode('utf-8-sig')
    after = actual.decode('utf-8-sig')
    assert before[before.index('## 文案内容'):]==after[after.index('## 文案内容'):],entry['path']
    block = re.search(r'##\s*视频数据\s*\r?\n([\s\S]*?)\r?\n---',after)[1]
    data = dict(re.split('[：:]',line,1) for line in block.splitlines() if line.strip())
    matches = [r for r in records if r['发布时间']==data['发布时间']]
    assert len(matches)==1
    record = matches[0]
    assert data['审核状态']==record['审核状态'] and data['体裁']==record['体裁']
    for label,key in [('播放量','播放量'),('点赞','点赞量'),('收藏','收藏量'),('评论','评论量'),('分享','分享量'),('主页访问量','主页访问量'),('涨粉量','粉丝增量')]:
        assert data[label]==str(int(Decimal(record[key]))),(entry['path'],key)
    for key in ['完播率','5s完播率','封面点击率','2s跳出率']:
        assert data[key]==percent(record[key]),(entry['path'],key)
    assert data['平均播放时长']==seconds(record['平均播放时长'])
    if record['审核状态']=='自见':
        assert '## 历史数据快照（2026-05-19）' in after
        original = re.search(r'##\s*视频数据\s*\r?\n([\s\S]*?)\r?\n---',before)[1].strip()
        assert original.replace('\r\n','\n') in after.replace('\r\n','\n')
        historical_snapshots+=1
    verified_legacy+=1
assert verified_legacy==22 and historical_snapshots==2
original_index = base64.b64decode(journal['entries'][-1]['before']).decode('utf-8-sig')
assert original_index.split('<!-- dailywrite-delivery:v1 -->')[0]==index.split('<!-- dailywrite-delivery:v1 -->')[0]
result = {'ok':True,'publicRowsVerified':30,'legacyMetricFilesVerified':22,'historicalSnapshotsPreserved':2,'legacyBodiesPreserved':22,'summaryTotals':totals,'transactionBackupVerified':True,'indexRowsUnchanged':True}
(RUN/'verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(result,ensure_ascii=False))
