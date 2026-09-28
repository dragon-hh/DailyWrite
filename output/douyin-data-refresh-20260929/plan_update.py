from pathlib import Path
from decimal import Decimal, InvalidOperation
from decimal import ROUND_HALF_UP
import datetime as dt
import hashlib
import json
import re
import sys
import unicodedata

sys.stdout.reconfigure(encoding='utf-8')
ROOT = Path(r'E:\projects\knowledgeProjects\DailyWrite')
RUN = ROOT / 'output/douyin-data-refresh-20260929'
source = json.loads((RUN / 'source-inspection.json').read_text(encoding='utf-8'))
index_by_id = {r['id']: r for r in source['indexRows']}

def platform_id(record):
    key = json.dumps([unicodedata.normalize('NFC',record['作品名称'].strip()), record['发布时间'].replace(' ','T')+'+08:00', record['体裁'].strip()], ensure_ascii=False, separators=(',',':'))
    return 'published-' + hashlib.sha256(key.encode()).hexdigest()[:24]

public = [r for r in source['records'] if r['审核状态']=='公开']
missing_ids = []
mapped = []
for record in public:
    link = source['metadata']['platformLinks'].get(platform_id(record))
    assert link, record['作品名称']
    if link['contentId'] not in index_by_id:
        missing_ids.append(link['contentId'])
    mapped.append({'date':record['发布时间'],'id':link['contentId'],'dataPath':index_by_id.get(link['contentId'],{}).get('dataPath')})
print(json.dumps({'mappedPublic':len(mapped),'uniqueContentIds':len(set(r['id'] for r in mapped)),'missingIndexIds':missing_ids,'indexedButNotPublic':[r['id'] for r in source['indexRows'] if r['id'] not in {m['id'] for m in mapped}]},ensure_ascii=False))
for item in mapped:
    if item['dataPath'] and '/抖音数据/' not in item['dataPath']:
        print(json.dumps(item,ensure_ascii=False))
for record in source['records']:
    if record['审核状态']=='自见' and record['发布时间'] in {'2026-02-01 22:07:05','2026-05-12 17:22:10'}:
        print(json.dumps(record,ensure_ascii=False))
print(json.dumps({'totals':{key:sum(Decimal(str(r[key])) for r in public) for key in ['播放量','点赞量','收藏量','分享量','评论量','粉丝增量']}},ensure_ascii=False,default=str))

DATE = '2026-09-29'
OBSERVED = '2026-09-27'
SOURCE_REL = '04-数据与复盘/平台导入/作品列表导出.xlsx'
INDEX_REL = '00-内容资产索引/内容主索引.md'
changes = []
body_hashes = {}
records_by_cid = {}
index_before = (ROOT / INDEX_REL).read_bytes()
meta_match = re.search(r'<!-- dailywrite-delivery:v1 -->\s*```json\s*(.*?)\s*```', index_before.decode('utf-8-sig'), re.S)
assert json.loads(meta_match.group(1)) == source['metadata'], 'Index changed after inspection'
for record in source['records']:
    link = source['metadata']['platformLinks'].get(platform_id(record))
    if link:
        assert link['contentId'] not in records_by_cid, 'Content has multiple exported records; needs explicit aggregation'
        records_by_cid[link['contentId']] = record
for old in source['oldData']:
    cid = next(r['id'] for r in source['indexRows'] if r['dataPath'] == '04-数据与复盘/抖音数据/' + old['file'])
    if cid not in records_by_cid:
        candidates = [r for r in source['records'] if r['发布时间'] == old['published']]
        assert len(candidates) == 1 and candidates[0]['审核状态'] == '自见', (cid, candidates)
        records_by_cid[cid] = candidates[0]

def digest(value):
    return hashlib.sha256(value).hexdigest()

def decimal_value(value):
    if value in (None, '', '-', '—'):
        return None
    result = Decimal(str(value).replace(',', ''))
    assert result.is_finite(), value
    return result

def count(record, key):
    value = decimal_value(record[key])
    assert value is not None and value == value.to_integral(), (record['source_row'], key, record[key])
    return str(int(value))

def rate(record, key):
    value = decimal_value(record[key])
    if value is None:
        return '—'
    assert 0 <= value <= 1, (record['source_row'], key, value)
    return f'{(value * 100).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP):.2f}%'

def seconds(record):
    value = decimal_value(record['平均播放时长'])
    if value is None:
        return '—'
    assert value >= 0
    return f'{value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP):.2f}秒'

def add_change(relative, text):
    file = ROOT / relative
    before = file.read_bytes() if file.exists() else None
    after = text.encode('utf-8')
    if before == after:
        return
    assert relative.startswith(('04-数据与复盘/', '05-方法论沉淀/', '02-素材知识库/', '00-内容资产索引/'))
    changes.append({'path':relative, 'expectedHash':digest(before) if before is not None else None, 'content':text})

def metrics(record):
    return {
        '发布时间':record['发布时间'], '体裁':record['体裁'], '审核状态':record['审核状态'],
        '标签':' '.join(dict.fromkeys(re.findall(r'#[^\s#]+', record['作品名称']))) or '未提供',
        '播放量':count(record,'播放量'), '完播率':rate(record,'完播率'), '5s完播率':rate(record,'5s完播率'),
        '封面点击率':rate(record,'封面点击率'), '2s跳出率':rate(record,'2s跳出率'), '平均播放时长':seconds(record),
        '点赞':count(record,'点赞量'), '评论':count(record,'评论量'), '收藏':count(record,'收藏量'),
        '分享':count(record,'分享量'), '主页访问量':count(record,'主页访问量'), '涨粉量':count(record,'粉丝增量'),
        '脱粉量':'未知（导出未提供）'
    }

legacy_records = []
index_by_path = {r['dataPath']:r for r in source['indexRows']}
for old in source['oldData']:
    relative = '04-数据与复盘/抖音数据/' + old['file']
    indexed = index_by_path[relative]
    cid = indexed['id']
    record = records_by_cid[cid]
    assert old['published'] == record['发布时间']
    before = (ROOT / relative).read_bytes().decode('utf-8-sig')
    newline = '\r\n' if '\r\n' in before else '\n'
    match = re.search(r'##\s*视频数据\s*\r?\n([\s\S]*?)\r?\n---', before)
    body_start = before.index('## 文案内容')
    assert match and match.end() < body_start, relative
    prefix = before[:match.start()]
    body = before[body_start:]
    body_hashes[relative] = digest(body.encode('utf-8'))
    annotations = [f'content_id: {cid}', f'数据来源：`{SOURCE_REL}`，Sheet1 第 {record["source_row"]} 行', f'指标观测：{OBSERVED} 导出快照', f'更新时间：{DATE}', '']
    block = ['## 视频数据'] + [f'{key}：{value}' for key,value in metrics(record).items()]
    if record['审核状态'] == '自见':
        block.append('统计说明：本次导出标为自见，不计入当前公开作品汇总；原有历史数据保留在下方。')
        if count(record,'播放量') == '0':
            block.append('播放字段说明：导出原值为 0；本条另有非零互动指标，不能据此判断历史播放或互动为零。')
    block += ['', '---', '']
    if record['审核状态'] == '自见':
        block += ['## 历史数据快照（2026-05-19）', '', '> 以下为本次更新前留存的历史指标，不计入本次汇总。', '', match.group(1).strip().replace('\r\n','\n'), '', '---', '']
    after = prefix + newline.join(annotations) + '\n'.join(block).replace('\n',newline) + newline + body
    assert digest(after[after.index('## 文案内容'):].encode('utf-8')) == body_hashes[relative]
    add_change(relative,after)
    legacy_records.append({'path':relative,'id':cid,'row':record['source_row'],'visibility':record['审核状态'],'metrics':metrics(record),'bodyHash':body_hashes[relative]})

totals = {key:sum(int(count(r,key)) for r in public) for key in ['播放量','点赞量','收藏量','分享量','评论量','粉丝增量']}
newer = [r for r in public if '/抖音数据/' not in index_by_id[source['metadata']['platformLinks'][platform_id(r)]['contentId']]['dataPath']]
assert len(public) == 30 and len(newer) == 10 and len(legacy_records) == 22
summary = ['# 抖音发布数据汇总表','',f'> 数据来源：`{SOURCE_REL}`（Sheet1；与 `D:\\webDownload\\作品列表导出 (1).xlsx` 字节一致）',f'> 指标观测：{OBSERVED} 导出快照；导出最新发布时间为 2026-09-23 20:01:32',f'> 更新时间：{DATE}', '> 统计范围：仅本次导出中审核状态为“公开”的作品；自见作品与导出之后发布的作品另列，不混入总计。','', '## 总览','', f'- 公开作品数：{len(public)}', f'- 总播放量：{totals["播放量"]}', f'- 总点赞：{totals["点赞量"]}', f'- 总收藏：{totals["收藏量"]}', f'- 总分享：{totals["分享量"]}', f'- 总评论：{totals["评论量"]}', f'- 总涨粉：{totals["粉丝增量"]}', '- 导出记录总数：150（公开 30、自见 120）', '- 数据覆盖：本目录 20 条公开作品 + 10 条已登记的工作台发布数据；链接均指向主索引已有数据文件。', '- 百分比和平均时长显示到小数点后两位；精确原始值保留在来源 Excel。`—` 表示导出未提供，不按零处理。', '', '## 公开作品明细', '', '| 发布日期 | 作品/数据文件 | 标签 | 体裁 | 播放量 | 完播率 | 5s完播率 | 平均播放时长 | 点赞 | 收藏 | 评论 | 分享 | 涨粉 |', '|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|']
for record in sorted(public,key=lambda r:int(count(r,'播放量')),reverse=True):
    cid = source['metadata']['platformLinks'][platform_id(record)]['contentId']
    indexed = index_by_id[cid]
    datapath = indexed['dataPath']
    assert (ROOT / datapath).is_file(), datapath
    if '/抖音数据/' in datapath:
        linkpath = Path(datapath).name
    else:
        linkpath = '../工作台发布数据/' + Path(datapath).name
    tags = ' '.join(dict.fromkeys(re.findall(r'#[^\s#]+', record['作品名称'])))
    columns = [record['发布时间'][:10],f'[{indexed["topic"]}](<{linkpath}>)',tags,record['体裁'],count(record,'播放量'),rate(record,'完播率'),rate(record,'5s完播率'),seconds(record),count(record,'点赞量'),count(record,'收藏量'),count(record,'评论量'),count(record,'分享量'),count(record,'粉丝增量')]
    assert all('|' not in item and '\n' not in item for item in columns)
    summary.append('| ' + ' | '.join(columns) + ' |')
summary += ['', '## 历史作品的当前可见性', '', '> 以下两条曾在旧汇总中计入公开作品，本次导出标为自见。下表保留导出原值，旧观测记录保留在对应单条数据文件中。', '', '| content_id | 作品 | 当前状态 | 本次导出播放量 | 点赞 | 收藏 | 分享 | 涨粉 |', '|---|---|---|---:|---:|---:|---:|---:|']
for item in legacy_records:
    if item['visibility'] != '自见':
        continue
    record = records_by_cid[item['id']]
    summary.append('| ' + ' | '.join([item['id'],f'[{index_by_id[item["id"]]["topic"]}](<{Path(item["path"]).name}>)','自见',count(record,'播放量'),count(record,'点赞量'),count(record,'收藏量'),count(record,'分享量'),count(record,'粉丝增量')]) + ' |')
summary += ['', '## 尚未进入本次导出的已登记作品', '', '- [GPT-Image-2.5 与豆包 Seedream 5.0 Pro 生图对比](<../工作台发布数据/DW-20260927-13FCB3D74AE1.md>)：主索引登记发布日期为 2026-09-27，已留存该日页面观测；本次导出不含此作品，未补造指标，也不计入上述总计。', '', '## 观测与引用规则', '', '- 本文件为累计指标的导出快照，不是 2026-09-29 实时数据，也不是当天新增播放或新增涨粉。', '- 历史汇总曾包含现在自见的作品，不能直接用旧总计与本次总计计算增长或下降。', '- 较新作品的完整数据记录位于 `04-数据与复盘/工作台发布数据/`；本表直接引用已有记录，内容归属仍以主索引的显式平台映射为准。', '- 单条文案保持原文；本次仅刷新指标、可见性、来源和关联汇总。', '']
add_change('04-数据与复盘/抖音数据/00-抖音数据汇总表.md','\n'.join(summary))

install = records_by_cid['DW-20260201-CLAUDECODE-INSTALL']
review_path = '05-方法论沉淀/爆款拆解/ClaudeCode教程复盘.md'
review = (ROOT / review_path).read_bytes().decode('utf-8-sig')
for label,key in [('播放量','播放量'),('点赞','点赞量'),('收藏','收藏量'),('分享','分享量'),('涨粉','粉丝增量')]:
    review,n = re.subn(rf'(?m)^(  - {label}：)\d+', lambda m:m[1]+count(install,key), review)
    assert n==1,(review_path,label,n)
review,n = re.subn(r'(?m)^(  - 完播率：)[\d.]+%', lambda m:m[1]+rate(install,'完播率'), review); assert n==1
review,n = re.subn(r'(?m)^(  - 5s完播率：)[\d.]+%', lambda m:m[1]+rate(install,'5s完播率'), review); assert n==1
review = review.replace('## 1. 核心数据记录',f'## 1. 核心数据记录\n\n> 数据刷新：{DATE}；指标来自 {OBSERVED} 抖音导出。当前审核状态为自见，不计入当前公开作品汇总；原结构复盘沿用历史结论。',1)
add_change(review_path,review)

formula_path = '05-方法论沉淀/爆款公式/爆款结构公式.md'
formula = (ROOT / formula_path).read_bytes().decode('utf-8-sig')
sample_ids = ['DW-20260201-CLAUDECODE-INSTALL','DW-20260307-OPENCLAW-SKILLS','DW-20260318-OPENCLAW-AGENT-TEAM','DW-20260428-CLAUDE-DESKTOP-CN']
sample_records = [records_by_cid[cid] for cid in sample_ids]
sample_basis = '、'.join(f'{label}({count(record,"播放量")})' for label,record in zip(['2.1','3.7','3.18','4.28'],sample_records))
formula = formula.replace('刷新于 2026-06-06',f'结构拆解于 2026-06-06；指标刷新于 {DATE}',1)
formula,n = re.subn(r'(?m)^> 数据基座：.*$',f'> 数据基座（{OBSERVED} 导出）：{sample_basis}',formula); assert n==1
formula = formula.replace('> 数据基座（'+OBSERVED+' 导出）：'+sample_basis, '> 数据基座（'+OBSERVED+' 导出）：'+sample_basis+'\n> 2.1 安装教程当前为自见。以下保留历史结构复盘，不作为当前公开作品排名。',1)
team = records_by_cid['DW-20260318-OPENCLAW-AGENT-TEAM']
skill = records_by_cid['DW-20260307-OPENCLAW-SKILLS']
formula = formula.replace('完播率14.45%，5s完播率52.57%',f'完播率{rate(team,"完播率")}，5s完播率{rate(team,"5s完播率")}',1)
formula = formula.replace('3.18: 14.45%',f'3.18: {rate(team,"完播率")}',1)
formula = formula.replace('3.7分享8507',f'3.7分享{count(skill,"分享量")}',1)
formula = formula.replace('*最后更新：2026-06-06*',f'*最后更新：{DATE}（指标刷新，结构判断未重新复盘）*',1)
add_change(formula_path,formula)

wiki_path = '02-素材知识库/爆款拆解库/高数据工具内容拆解.md'
wiki = (ROOT / wiki_path).read_bytes().decode('utf-8-sig')
for cid in sample_ids:
    record = records_by_cid[cid]
    pattern = rf'(?m)^\| {re.escape(cid)} \| (.*?) \|$'
    found = re.search(pattern,wiki); assert found,cid
    mode = found[1].split('|')[-1].strip()
    row = '| ' + ' | '.join([cid,count(record,'播放量'),rate(record,'完播率'),rate(record,'5s完播率'),count(record,'收藏量'),count(record,'分享量'),count(record,'粉丝增量'),mode]) + ' |'
    wiki,n = re.subn(pattern,row,wiki); assert n==1
wiki = wiki.replace('## 数据样本',f'## 数据样本\n\n> 指标来自 {OBSERVED} 抖音导出，刷新于 {DATE}。安装教程当前为自见，其他三条为公开；结构判断沿用历史复盘。',1)
add_change(wiki_path,wiki)

request_id = 'douyin-data-refresh-20260929-' + source['sourceSha256'][:12]
now = dt.datetime.now(dt.timezone.utc).isoformat().replace('+00:00','Z')
log_path = '00-内容资产索引/log.md'
log = (ROOT / log_path).read_bytes().decode('utf-8-sig')
add_change(log_path,log.rstrip()+f'\n\n- {now} 抖音指标刷新；request_id: {request_id}；来源: {SOURCE_REL}，SHA256: {source["sourceSha256"]}；观测日期: {OBSERVED}；更新旧目录 22 条单条数据（20 公开、2 自见），汇总关联另 10 条已有工作台记录，共计 30 条公开作品；保留单条文案及两条自见作品历史快照；同步刷新 2 份方法论和 1 份素材的数据基座；未将导出缺失作品补造入统计。\n')
protected = {INDEX_REL:digest(index_before), SOURCE_REL:digest((ROOT/SOURCE_REL).read_bytes())}
for row in source['indexRows']:
    protected[row['bodyPath']] = digest((ROOT/row['bodyPath']).read_bytes())
    if '/工作台发布数据/' in row['dataPath']:
        protected[row['dataPath']] = digest((ROOT/row['dataPath']).read_bytes())
plan = {'requestId':request_id,'expectedRevision':digest(index_before),'source':source['source'],'sourceSha256':source['sourceSha256'],'observedDate':OBSERVED,'updatedDate':DATE,'counts':{'updatedLegacyFiles':22,'legacyPublicFiles':20,'legacyPrivateFiles':2,'linkedExistingWorkbenchFiles':10,'publicWorks':30,'methodologyFiles':2,'wikiFiles':1},'totals':totals,'legacyRecords':legacy_records,'protectedHashes':protected,'changes':changes}
(RUN/'update-plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'planPrepared':True,'requestId':request_id,'changedFilesBeforeReceipt':len(changes),'counts':plan['counts'],'totals':totals},ensure_ascii=False))
