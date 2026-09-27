# dbs 技能注册表 v2

这是 `/dbs` 路由和任务交接的单一清单。技能描述负责“何时触发”，本表负责“输入、产物和边界”。

| 技能 | 适用输入 | 主要产物 | 默认写入 | 常见下一步 |
|---|---|---|---|---|
| `dbs-diagnosis` | 商业问题或商业模式 | 问诊/体检诊断 | 否 | `dbs-good-question`、`dbs-benchmark`、`dbs-content` |
| `dbs-benchmark` | 已知对标或寻找对标 | 对标筛选、模仿路径 | 否 | `dbs-content`、`dbs-decision` |
| `dbs-content` | 已确认选题或文稿 | 内容方向诊断 | 否 | `dbs-hook`、`dbs-xhs-title`、`dbs-ai-check` |
| `dbs-spread` | 已发布/已有内容与传播问题 | 传播机制分析 | 否 | `dbs-content`、`dbs-hook` |
| `dbs-resonate` | 待发布文稿 | 共鸣诊断与删改建议 | 否 | `dbs-content`、`dbs-hook` |
| `dbs-hook` | 短视频文稿或开头 | 开头候选与选择依据 | 否 | `dbs-content` |
| `dbs-xhs-title` | 主题、文稿或已有标题 | 公式编号与标题候选 | 否 | `dbs-hook`、`dbs-content` |
| `dbs-ai-check` | 文稿及体裁 | AI 特征证据报告 | 否 | `dbs-content` 或用户明确改写 |
| `dbs-wechat-html` | Markdown 与排版偏好 | HTML、预览和验收记录 | 是（用户指定目录） | 暂无 |
| `dbs-slowisfast` | 正在采用的方法 | 快慢方法与资产判断 | 否 | `dbs-action`、`dbs-diagnosis` |
| `dbs-action` | 知道目标但执行受阻 | 执行阻力的工作假设 | 否 | `dbs-goal`、`dbs-diagnosis` |
| `dbs-deconstruct` | 模糊概念或术语 | 概念边界与操作定义 | 否 | `dbs-goal`、`dbs-good-question` |
| `dbs-goal` | 愿望、模糊目标 | 可验收目标草案 | 否 | `dbs-action`、`dbs-decision` |
| `dbs-good-question` | 模糊问题或自动化设想 | 问题说明书与可解性 | 否 | 与问题类型对应的诊断技能 |
| `dbs-decision` | 需长期跟踪的领域 | 本地决策工程与快照 | 是（用户确认后的目录） | `dbs-diagnosis`、`dbs-restore` |
| `dbs-agent-migration` | 规则文件、skills、bridge | 迁移审计与真源/bridge 方案 | 是（用户指定项目） | `dbs-content-system` |
| `dbs-content-system` | 大量本地内容资产 | 可复用内容工程 | 是（用户指定项目） | `dbs-content`、`dbs-decision` |
| `dbs-chatroom` | 想比较多个视角的问题 | 多角色讨论与判官总结 | 否 | `/dbs` 或具体诊断技能 |
| `dbs-chatroom-austrian` | 价格、市场、企业家等经济学问题 | 奥派视角讨论 | 否 | `dbs-deconstruct`、`dbs-diagnosis` |
| `dbs-learning` | 学习主题与反馈 | 连续学习文章与进度 | 是（用户指定学习目录） | `dbs-restore` 或对应技能 |
| `dbs-save` | 已完成的 dbs 诊断上下文 | 结构化存档与写入回执 | 是（`~/.dbs/sessions`） | `dbs-restore`、`dbs-report` |
| `dbs-restore` | 已有存档 | 可继续使用的状态摘要 | 否 | 用户指定或 `next_skill` |
| `dbs-report` | 两份以上存档 | 可分享 Markdown 报告 | 是（`~/.dbs/reports`） | 对应未决问题的技能 |

## 路由优先级

1. 用户明确点名的 `/dbs-*` 或明确交付物优先。
2. 写入、发送、发布、删除等副作用必须单独确认授权，不由诊断结论推导。
3. 输入不足时先补最小缺口；不要因为路由表有一个“最像”的技能就硬跑。
4. 同时命中多个技能时先选择能消除最大不确定性的那个；其余作为交接建议。
5. 任何结论都要回到运行契约中的证据分层，不能把注册表的“主要产物”当成已经生成的产物。
