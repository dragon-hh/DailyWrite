---
name: published-script-archive
description: 核对 DailyWrite 已发布视频与 Markdown 最终稿的对应关系，并将同一视频的历史稿可追溯地移入项目外冷备份。用户要求补齐发布文稿、核对发布映射或清理旧版本时使用；不处理普通未发布稿。
---

# 已发布视频文稿核对与版本归档

在 DailyWrite 项目根目录工作。先读根目录 `AGENTS.md`、`SOURCE_OF_TRUTH.md` 和 `00-内容资产索引/内容主索引.md` 的当前规则。按本次请求的范围执行：只要求核对时交付映射报告；用户要求整理旧版时才移动文件。完整归档任务交付一张可核对的“平台作品 → `content_id` → 发布正文 → 唯一保留稿”映射，以及可恢复的旧版归档清单。图文无文稿可以是合理结果。

## 找到每条已发布视频

1. 以工作台当前发布记录、`04-数据与复盘/` 的平台导入及已发布索引为起点；用户新给的导出表先只读核对。按平台、作品链接或平台记录 ID、发布时间、标题共同识别作品。标题相近不代表同一条，系列的不同集数分别登记。导出表缺少链接时，检查已有记录，再从用户指定的账号主页找对应公开视频；仍不确定就列为待核对。
2. 用 `rg --files '01-内容生产/01-脚本创作中' '01-内容生产/02-待拍摄'` 查 Markdown 候选；必要时再查 `03-已发布归档/已发布成品/`。逐篇看正文的主题、集数、口播内容及发布时间是否吻合。文件修改时间可把同组候选排序，**不能单独证明最终版或已发布**。HTML、ZIP、封面和图文图片不是视频文稿；公众号稿等独立文章不作为视频旧版。
3. 对每条输出证据和结论：已确认的 `content_id`、平台 URL、发布时间、最终 Markdown 路径、其他同视频版本；或者明确标为“缺文稿 / 待确认 / 非视频 / 实际未发布”。不能用相近草稿填补实际发布正文，也不能把两个视频共用一个 `content_id`。用户已明确给出的发布或未发布事实优先于文件名推断。

## 补齐发布登记

只有实际正文、作品链接、发布日期和平台均已由用户确认或已有等价的明确记录时，才登记或更正。使用工作台现有 `GET/PATCH /api/delivery`；从当前快照取 `expectedRevision`，为每次操作生成唯一 `requestId`，保留请求/收据并写后读回。接口约束以 `90-工具项目/dailywrite-workbench/server/deliveryRepository.mjs` 和项目现行规则为准，不绕过工作台手改交付 JSON。结果未知时检查原请求收据与文件哈希，不换 ID 盲目重发。发布成品在 `03-已发布归档/已发布成品/`，数据文件在 `04-数据与复盘/`，两者与主索引的 `content_id` 要一致。未确认的作品不进入归档步骤。

## 归档同视频旧版

先检查最终稿与工作台 `publication.sourcePath`、发布成品的 SHA-256 一致；旧版不得是任何当前发布来源稿或工作台已登记文件。按每个 `content_id` 写明确的计划文件，格式见下文；**只列已核实属于同一视频的 Markdown 旧版**。运行脚本的 `plan` 模式先检查全部路径、哈希和索引引用，审阅输出后再运行 `apply`。`apply` 将旧稿逐份移到 DailyWrite 外层冷备份，先落清单再移动，每份移动后更新状态。不得创建 `03-已发布归档/草稿归档/`，也不批量移动未发布稿、公众号稿或素材。若途中失败，保留现场并用 `verify` 查看，先排查再继续，不另开同名归档覆盖。

```json
{
  "schemaVersion": 1,
  "groups": [
    {
      "contentId": "DW-已核实ID",
      "finalSource": "01-内容生产/01-脚本创作中/最终稿.md",
      "variants": ["01-内容生产/01-脚本创作中/旧版.md"]
    }
  ]
}
```

```text
node .agents/skills/published-script-archive/scripts/archive-versions.mjs plan --root "DailyWrite绝对路径" --archive "项目外新归档目录" --plan "计划文件绝对路径"
node .agents/skills/published-script-archive/scripts/archive-versions.mjs apply --root "DailyWrite绝对路径" --archive "同一归档目录" --plan "同一计划文件"
node .agents/skills/published-script-archive/scripts/archive-versions.mjs verify --archive "同一归档目录"
```

`plan` 只读；`apply` 要求归档目录尚不存在。清单保存每份原路径、目标路径、修改时间、字节数和 SHA-256。归档后搜索旧路径在封面记录等文档中的引用，按事实改为冷备份路径，保留历史溯源；再核对最终稿、成品、数据与主索引，运行工作台 `npm run validate:data`。报告成功数与未解决缺口，不能把已有降级问题写成这次已修复。
