from pathlib import Path
from decimal import Decimal, ROUND_HALF_UP
import datetime as dt
import hashlib
import json
import re
import sys
import unicodedata
import openpyxl

sys.stdout.reconfigure(encoding='utf-8')
ROOT = Path(r'E:\projects\knowledgeProjects\DailyWrite')
RUN = ROOT / 'output/douyin-episode-files-20260929'
INDEX = '00-内容资产索引/内容主索引.md'
SOURCE = ROOT / '04-数据与复盘/平台导入/作品列表导出.xlsx'
SOURCE_HASH = 'b07795644c4df569b5a8bf6d9d92929735aebf46f97b5cd08c78183ccc0e77b3'
NAMES = {
    'DW-20260917-CODEX-WORKFLOW-01': '9.23--Codex高级使用技巧.md',
    'DW-20260815-DEEPSEEK-HARNESS-01': '8.16--DeepSeek Harness两天破10万Star.md',
    'DW-20260715-AI-DEV-SKILL-WORKFLOW-01': '7.18--17万Star的顶级AI开发流程.md',
    'DW-20260927-C49B7E6A2AFE': '7.10--豆包一句话出宣传片.md',
    'DW-20260927-A8082587F1DC': '6.25--Codex自动追踪AI博主-第二集.md',
    'DW-20260620-AI-CREATOR-TRACKER-01': '6.20--Codex自动追踪AI博主更新-第一集.md',
    'DW-20260927-34A87258B328': '6.20--AI日报与全自动推送.md',
    'DW-20260605-CC-WORKFLOW-01': '5.31--Claude Code Workflow更新.md',
    'DW-20260927-5E64ADE79FD5': '5.22--微信聊天记录私人商业情报系统.md',
    'DW-20260927-5AE65027300B': '2.11--Gemini做PPT教程.md',
    'DW-20260927-13FCB3D74AE1': '9.27--GPT与豆包生图对比.md',
}
def sha(data):
    return hashlib.sha256(data).hexdigest()

assert sha(SOURCE.read_bytes()) == SOURCE_HASH
book = openpyxl.load_workbook(SOURCE, read_only=True, data_only=True)
values = list(book.active.values)
headers = ['作品名称','发布时间','体裁','审核状态','播放量','完播率','5s完播率','封面点击率','2s跳出率','平均播放时长','点赞量','分享量','评论量','收藏量','主页访问量','粉丝增量']
assert book.sheetnames == ['Sheet1'] and list(values[0]) == headers
records = []
for n, row in enumerate(values[1:], 2):
    record = dict(zip(headers, row))
    if isinstance(record['发布时间'], dt.datetime):
        record['发布时间'] = record['发布时间'].strftime('%Y-%m-%d %H:%M:%S')
    dt.datetime.strptime(record['发布时间'], '%Y-%m-%d %H:%M:%S')
    record['source_row'] = n
    records.append(record)
book.close()
assert len(records) == 150
index_bytes = (ROOT / INDEX).read_bytes()
index = index_bytes.decode('utf-8')
meta = json.loads(re.search(r'<!-- dailywrite-delivery:v1 -->\s*```json\s*(.*?)\s*```', index, re.S).group(1))
prefix = index.split('<!-- dailywrite-delivery:v1 -->')[0]
published = prefix.split('## 已发布作品索引')[1].split('## 当前生产索引')[0]
index_rows = {}
for line in published.splitlines():
    if line.startswith('| DW-'):
        cells = [c.strip().strip('`') for c in line.strip('|').split('|')]
        assert len(cells) == 8 and cells[0] not in index_rows
        index_rows[cells[0]] = cells
assert len(index_rows) == 33

def platform_id(record):
    payload = [unicodedata.normalize('NFC', record['作品名称'].strip()), record['发布时间'].replace(' ', 'T') + '+08:00', record['体裁'].strip()]
    return 'published-' + sha(json.dumps(payload, ensure_ascii=False, separators=(',', ':')).encode())[:24]

by_id = {}
for record in records:
    if record['审核状态'] == '公开':
        link = meta['platformLinks'][platform_id(record)]
        cid = link['contentId']
        assert cid not in by_id and cid in index_rows
        by_id[cid] = record
assert len(by_id) == 30 and len(set(NAMES) & set(by_id)) == 10

def value(record, key):
    raw = record[key]
    if raw in (None, '', '-', '—'):
        return None
    result = Decimal(str(raw).replace(',', ''))
    assert result.is_finite()
    return result

def count(record, key):
    number = value(record, key)
    assert number is not None and number >= 0 and number == number.to_integral()
    return str(int(number))

def rate(record, key):
    number = value(record, key)
    if number is None:
        return '—'
    assert 0 <= number <= 1
    return f'{(number * 100).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP):.2f}%'

def metrics(record):
    seconds = value(record, '平均播放时长')
    return {
        '发布时间': record['发布时间'], '体裁': record['体裁'], '审核状态': record['审核状态'],
        '标签': ' '.join(dict.fromkeys(re.findall(r'#[^\s#]+', record['作品名称']))) or '未提供',
        '播放量': count(record, '播放量'), '完播率': rate(record, '完播率'), '5s完播率': rate(record, '5s完播率'),
        '封面点击率': rate(record, '封面点击率'), '2s跳出率': rate(record, '2s跳出率'),
        '平均播放时长': '—' if seconds is None else f'{seconds.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP):.2f}秒',
        '点赞': count(record, '点赞量'), '评论': count(record, '评论量'), '收藏': count(record, '收藏量'),
        '分享': count(record, '分享量'), '主页访问量': count(record, '主页访问量'), '涨粉量': count(record, '粉丝增量'),
        '脱粉量': '未知（导出未提供）',
    }

changes = []
protected = {}
for file in (ROOT / '03-已发布归档/已发布成品').glob('DW-*.md'):
    protected[file.relative_to(ROOT).as_posix()] = sha(file.read_bytes())
for file in (ROOT / '04-数据与复盘/抖音数据').glob('*.md'):
    if file.name != '00-抖音数据汇总表.md':
        protected[file.relative_to(ROOT).as_posix()] = sha(file.read_bytes())
for relative in ['04-数据与复盘/平台导入/作品列表导出.xlsx', '01-内容生产/01-脚本创作中/选题.md']:
    protected[relative] = sha((ROOT / relative).read_bytes())

def add(relative, text):
    file = ROOT / relative
    before = file.read_bytes() if file.exists() else None
    assert before is None or before != text.encode('utf-8')
    changes.append({'path': relative, 'expectedHash': sha(before) if before is not None else None, 'content': text})

episodes = []
next_prefix = prefix
registry_path = '90-工具项目/published-archive-sync/published-works.json'
registry = json.loads((ROOT / registry_path).read_text(encoding='utf-8'))
assert len(registry) == 22
registry_before = json.loads(json.dumps(registry))
for cid, filename in NAMES.items():
    cells = index_rows[cid]
    publication = meta['contents'][cid]['publication']
    assert cells[2:4] == ['已发布', '抖音']
    assert publication['dataPath'] == cells[5] and publication['bodyPath'] == cells[4]
    assert publication['platform'] == '抖音'
    body_raw = (ROOT / cells[4]).read_bytes()
    assert sha(body_raw) == publication['sha256'] and body_raw.strip()
    body = body_raw.decode('utf-8')
    old_path = cells[5]
    old_data = (ROOT / old_path).read_bytes()
    protected[old_path] = sha(old_data)
    new_path = '04-数据与复盘/抖音数据/' + filename
    assert not (ROOT / new_path).exists(), new_path
    if cid in by_id:
        record = by_id[cid]
        assert publication['publishedAt'] == record['发布时间'][:10]
        field_values = metrics(record)
        provenance = f'数据来源：`04-数据与复盘/平台导入/作品列表导出.xlsx`，Sheet1 第 {record["source_row"]} 行\n指标观测：2026-09-27 导出快照\n'
        row = record['source_row']
    else:
        assert cid == 'DW-20260927-13FCB3D74AE1' and publication['publishedAt'] == '2026-09-27'
        assert '核对时间 2026-09-27；播放量：7；' in old_data.decode('utf-8')
        field_values = {'发布时间': '2026-09-27（具体时分秒待补）', '体裁': '视频（时长分类待补）', '审核状态': '已发布（本次导出未收录）', '标签': '待补', '播放量': '7'}
        field_values.update({key: '待补' for key in ['完播率','5s完播率','封面点击率','2s跳出率','平均播放时长','点赞','评论','收藏','分享','主页访问量','涨粉量','脱粉量']})
        provenance = f'数据来源：抖音主页与作品详情页的既有观测；原始记录：`{old_path}`\n指标观测：2026-09-27 页面核对记录\n统计说明：未进入本次 Excel 导出，不计入导出公开作品总计；未重新抓取实时指标。\n'
        row = None
    title = filename.split('--', 1)[1][:-3]
    header = f'# {title}\n\ncontent_id: {cid}\n平台：抖音\n作品链接：{publication["url"]}\n' + provenance
    header += f'更新时间：2026-09-29\n发布正文来源：`{cells[4]}`\n发布正文 SHA256：{sha(body_raw)}\n\n## 视频数据\n\n'
    header += '\n'.join(f'{key}：{val}' for key, val in field_values.items()) + '\n\n---\n\n## 文案内容\n\n'
    add(new_path, header + body)
    line = next(line for line in prefix.splitlines(keepends=True) if line.startswith(f'| {cid} |'))
    assert line.count(old_path) == 1
    next_prefix = next_prefix.replace(line, line.replace(old_path, new_path), 1)
    registry.append({'id': cid, 'source': filename, 'title': title, 'topic': cells[1], 'reuse': cells[7]})
    episodes.append({'id': cid, 'path': new_path, 'oldPath': old_path, 'bodyPath': cells[4], 'bodySha256': sha(body_raw), 'sourceRow': row, 'metrics': field_values})
assert registry[:22] == registry_before
assert len({entry['source'] for entry in registry}) == len({entry['id'] for entry in registry}) == 33
add(registry_path, json.dumps(registry, ensure_ascii=False, indent=2) + '\n')

summary_path = '04-数据与复盘/抖音数据/00-抖音数据汇总表.md'
summary = (ROOT / summary_path).read_bytes().decode('utf-8')
for episode in episodes:
    old_link = '<../工作台发布数据/' + episode['id'] + '.md>'
    assert summary.count(old_link) == 1
    summary = summary.replace(old_link, '<' + Path(episode['path']).name + '>')
summary = summary.replace('- 数据覆盖：本目录 20 条公开作品 + 10 条已登记的工作台发布数据；链接均指向主索引已有数据文件。', '- 数据覆盖：本目录 33 份单条作品文件（导出公开 30 条、自见 2 条、未进入导出 1 条），每条包含对应观测与实际发布文案；不同观测来源分别记录。')
summary = summary.replace('- 较新作品的完整数据记录位于 `04-数据与复盘/工作台发布数据/`；本表直接引用已有记录，内容归属仍以主索引的显式平台映射为准。', '- 全部已登记作品的单条数据文件位于本目录，内容归属以主索引的显式平台映射为准；`工作台发布数据/` 中原有记录保留，作为历史登记与观测依据。')
summary = summary.replace('- 单条文案保持原文；本次仅刷新指标、可见性、来源和关联汇总。', '- 原有单条文案保持原文；新增 11 份按期文件的文案从已核对的已发布成品复制，并校验正文 SHA256。')
assert '../工作台发布数据/' not in summary
add(summary_path, summary)

readme_path = '03-已发布归档/已发布成品/README.md'
readme = (ROOT / readme_path).read_bytes().decode('utf-8')
readme = readme.replace('- 历史平台指标保存在 `04-数据与复盘/抖音数据/`；工作台登记的发布指标保存在 `04-数据与复盘/工作台发布数据/`，不同观测时间的数据分别记录。', '- 33 个已登记作品的单条指标与发布文案副本统一保存在 `04-数据与复盘/抖音数据/`；`04-数据与复盘/工作台发布数据/` 的原有记录保留为历史依据，不同观测时间分别记录。')
readme = readme.replace('- 下表 22 条历史作品由 `90-工具项目/published-archive-sync/sync-published-archive.mjs` 从显式映射表同步；工作台后续登记的作品以 `00-内容资产索引/内容主索引.md` 为完整清单。', '- 下表与 `00-内容资产索引/内容主索引.md` 连接到同一批 33 个已登记作品；新增单条数据通过工作台事务机制写入，保留已发布正文原件。')
readme = readme.replace('当前目录有 33 份 `content_id` 成品文件；下表记录历史同步批次的 22 份。', '当前目录有 33 份 `content_id` 成品文件；下表列出全部 33 份。当前可见性与指标观测以单条数据文件为准，已登记作品不等于全部当前公开。')
newline = '\r\n' if '\r\n' in readme else '\n'
readme = readme.rstrip('\r\n') + newline
for episode in episodes:
    cid = episode['id']
    cells = index_rows[cid]
    readme += f'| {cid} | {episode["metrics"]["发布时间"]} | {cells[1]} | {episode["metrics"]["体裁"]} | `{cid}.md` | `{episode["path"]}` | 已回填 |' + newline
add(readme_path, readme)

request_id = 'douyin-episode-files-20260929-' + SOURCE_HASH[:12]
log_path = '00-内容资产索引/log.md'
log = (ROOT / log_path).read_bytes().decode('utf-8')
now = dt.datetime.now(dt.timezone.utc).isoformat().replace('+00:00', 'Z')
log += f'\n- {now} 补齐按期抖音数据文件；request_id: {request_id}；新增 11 份，目录共 33 份单条作品文件；其中 10 份指标来自 2026-09-27 Excel 导出，9.27 生图对比使用既有页面观测（播放 7，其余待补），不同观测不混入总计；文案复制自已核对发布成品，原件与旧数据文件保持不变；同步主索引与 publication.dataPath、汇总链接、显式映射表和成品目录说明；使用事务备份和逐文件读回校验。\n'
add(log_path, log)

plan = {'requestId': request_id, 'source': str(SOURCE), 'sourceSha256': SOURCE_HASH, 'expectedRevision': sha(index_bytes), 'beforePrefix': prefix, 'afterPrefix': next_prefix, 'episodes': episodes, 'changes': changes, 'protectedHashes': protected}
(RUN / 'plan.json').write_text(json.dumps(plan, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps({'newEpisodeFiles': len(episodes), 'plannedWritesExcludingIndex': len(changes), 'sourceRows': [e['sourceRow'] for e in episodes], 'indexRevision': plan['expectedRevision']}, ensure_ascii=False))
