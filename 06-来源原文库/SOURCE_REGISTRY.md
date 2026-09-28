# SOURCE_REGISTRY

来源登记表用于记录 Raw sources 的状态。每个来源进入 `06-来源原文库/` 后都应登记。

| source_id | 来源文件 | 类型 | 状态 | 抽取状态 | 写回目标 | 备注 |
|---|---|---|---|---|---|---|
| SRC-20260606-LLM-WIKI | `06-来源原文库/外部资料/llm-wiki.md` | 外部方法论参考 | 已评估 | 待吸收 | `SOURCE_OF_TRUTH.md`、`AGENTS.md`、`00-内容资产索引/` | 参考 Raw sources / Wiki / Schema、Ingest / Query / Lint 思路，不作为 DailyWrite 生产规则本体 |
| SRC-20260720-XYQ-SEEDANCE25-BRIEF | `06-来源原文库/小云雀Seedance2.5-Brief/01-小云雀S级推广-Seedance2.5模型升级-Brief.md` | 合作 Brief 原文 | 未评估 | 待吸收 | 待定 | 来源为飞书 Wiki，修订版本 9963；原始 PDF 导出被文档权限禁止，本地另有文本渲染 PDF；派生清洗版：`06-来源原文库/小云雀Seedance2.5-Brief/清洗版/01-小云雀S级推广-Seedance2.5模型升级-Brief-清洗版.md` |
| SRC-20260720-XYQ-SEEDANCE25-CASES | `06-来源原文库/小云雀Seedance2.5-Brief/02-小云雀Seedance2.5实测案例.md` | 合作案例原文 | 未评估 | 待吸收 | 待定 | 来源为飞书 Wiki，修订版本 2545；原始 PDF 导出超过尺寸限制，本地另有文本渲染 PDF；内嵌视频未下载；派生清洗版：`06-来源原文库/小云雀Seedance2.5-Brief/清洗版/02-小云雀Seedance2.5实测案例-清洗版.md` |

## 状态说明

- `未评估`：已入库但尚未判断价值。
- `已评估`：已读过并判断用途。
- `已抽取`：已写回素材库或方法论。
- `不抽取`：保留原文，但不进入生产系统。

## 抽取状态

- `待吸收`
- `部分吸收`
- `已吸收`
- `不适用`
