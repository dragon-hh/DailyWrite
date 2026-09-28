# 内容资产维护日志

本日志按时间记录 DailyWrite 内容资产系统的维护动作。只记录关键事件，不替代正文、索引或复盘。

## 2026-06-06 ingest | LLM Wiki 方法论参考

- 来源：`06-来源原文库/外部资料/llm-wiki.md`
- 动作：从根目录迁入 Raw sources 层，并登记到 `06-来源原文库/SOURCE_REGISTRY.md`。
- 判断：该文件适合作为内容资产系统维护机制参考，不替代 DailyWrite 现有内容生产系统。
- 待吸收点：Raw sources / Wiki / Schema 三层分离；Ingest / Query / Lint 三类维护动作；`index.md` 与 `log.md` 的长期导航价值。

## 2026-06-06 lint | 首次轻量健康检查

- 检查对象：根目录、`00-内容资产索引/`、`06-来源原文库/`
- 结论：需要补齐来源层、日志和 lint 清单，避免素材库与原始资料混放。
- 处理：本次新增 `06-来源原文库/`、`SOURCE_REGISTRY.md`、`log.md`、`lint-checklist.md`。

## 2026-06-20 script | AI 博主视频文案追踪系统公众号版

- content_id：DW-20260620-AI-CREATOR-TRACKER-01
- 来源：`01-内容生产/01-脚本创作中/6.20 爬取ai博主视频，并存放多维表格-claude-v1.md`
- 动作：基于原口播稿新写公众号版，并生成 4 张配图到同名 assets 目录。
- 参考：读取飞书 Base `AI博主视频文案追踪` 的真实结构和样例记录；确认 24 个博主、72 条视频、70 条快照、42 条任务日志、评论表 200+ 条。
- 待处理：发布前可用已登录浏览器替换为真实飞书截图；当前配图为基于真实结构生成的截图式示意图。

## 2026-07-18 archive | 补齐抖音已发布成品

- 范围：`04-数据与复盘/抖音数据/00-抖音数据汇总表.md` 中截至 2026-05-19 的 22 个公开作品。
- 动作：为 22 个作品建立唯一 `content_id`，把平台单条数据文件中的实际发布文案和数据快照同步到 `03-已发布归档/已发布成品/`，并补齐 `00-内容资产索引/内容主索引.md`。
- 结果：新增 17 个成品文件，扩充原有 5 个只有溯源指针的成品文件；成品、数据和主索引现为 22 对 22 对 22。
- 可观测性：新增 `90-工具项目/published-archive-sync/`。同步脚本会在出现重复 ID、未映射数据文件、空正文、缺失过程稿或断链时直接报错。
- 待补：`DW-20260312-OPENCLAW-BUGS` 的平台数据只保存了“图文，随便发的”，原图文页正文仍缺失，已明确标记为待补。

## 2026-07-18 archive | 低版本过程稿移出知识库

- 源目录：`03-已发布归档/草稿归档/`
- 备份目录：`E:\projects\knowledgeProjects\DailyWrite-历史过程稿备份\2026-07-18\`
- 动作：移动 47 个明确低版本、`backup` / `bak` 或完全重复文件，保持原相对目录结构；没有删除文件。
- 保护边界：15 个已绑定已发布成品的高置信过程稿全部保留；未标版本、不同用途或版本关系不明确的独立稿未移动。
- 可恢复性：外层备份的 `migration-record.json` 记录每个文件的原路径、备份路径、大小、SHA-256 和迁移原因。

## 2026-07-18 archive | 草稿归档全部移出知识库

- 口径修正：实际发布内容已经完整进入 `03-已发布归档/已发布成品/`，因此草稿归档中的最高版本、独立稿、不同模型稿和相关图片同样属于过程产物，不应留在活跃知识库。
- 第二批移动：将 `03-已发布归档/草稿归档/2026-05-19/` 剩余 211 个文件全部移到 `E:\projects\knowledgeProjects\DailyWrite-历史过程稿备份\2026-07-18\`，随后删除空的日期目录。
- 最终结果：两批共移动 258 个文件、37877464 字节；`03-已发布归档/草稿归档/` 只保留说明文件。
- 成品解耦：15 个已发布成品的过程稿溯源已改为外层冷备份路径；发布正文和数据仍分别以 `03-已发布归档/已发布成品/`、`04-数据与复盘/` 为准。
- 可恢复性：`migration-record-all.json` 记录全部 258 个文件的原路径、备份路径、大小、SHA-256 和迁移原因。

## 2026-07-18 archive | 根目录整理产物移出知识库

- 源目录：`03-已发布归档/根目录整理/`
- 判断：该目录保存迁移清单、未命名 Base/Canvas 和相关图片，是根目录整理过程产物，不是已发布成品或可复用素材。
- 动作：将 42 个文件、55073921 字节整体移动到 `E:\projects\knowledgeProjects\DailyWrite-历史过程稿备份\2026-07-18\根目录整理\`，源目录已删除。
- 可恢复性：`migration-record-root-cleanup.json` 保存本批次记录；`migration-record-all-process-artifacts.json` 汇总草稿归档和根目录整理两类过程产物，共 300 个文件、92951385 字节。

## 2026-07-18 archive | 删除草稿归档空壳目录

- 删除：`03-已发布归档/草稿归档/README.md` 及其空目录。
- 原因：历史过程产物已全部移到外层冷备份，保留空壳目录和说明文件没有继续存在的价值。
- 最终边界：`03-已发布归档/` 只允许存在 `已发布成品/`。

## 2026-07-20 script | 小云雀 Seedance 2.5 十七方向拍摄执行包

- 范围：当前合作 Brief 的整体测评 2 篇、影视 7 篇、广告营销 4 篇、自媒体 2 篇、UGC 2 篇，共 17 篇。
- 动作：为每篇建立独立 `content_id`、五列表格脚本、附件命名、实拍/录屏方案、图片与视频提示词、失败补救、剪辑与发布要求；创建总览和受控 Markdown→飞书 XML 转换器。
- 能力边界：参考视频总时长 ≤30 秒；单次生成 ≤30 秒；《白垩纪之烬》只用 18 秒授权片段；片段重拍只用于 Seedance 2.5 生成视频；动态布景未写成当前可用能力。
- 旧稿处理：`7.19 小云雀，seedance2.5 推广.md` 已标记为被第 15 篇替代，主索引只指向新稿。
- 飞书文档：`https://hcnwllogsej4.feishu.cn/docx/QCfddLiyMoOyX0xZMVuczRE6nQd`，已回读目录及代表章节，脚本表与提示词未截断。

## 2026-07-20 script revision | 片段重拍方向重写

- 原因：旧稿以操作步骤串联，缺少具体事件、对照冲突和完整交付结果。
- 动作：将 `DW-20260720-XYQ-RESHOOT-01` 改为红鞋带换白的审片案例；新增整条重跑对照、5–10 秒局部重拍、三版同屏、边界四帧和 15 秒完整成片。
- 前置资产：补齐三张同鞋参考图、空景、15 秒底片提示词、整条重跑提示词、局部重拍指令、录屏步骤、剪辑时间线、验收门槛和失败处理。
- 飞书同步：仅替换总文档第 10 节，回读确认五列表格和全部提示词完整，文档修订版本为 34。

## 2026-07-20 source | 小云雀 Seedance 2.5 合作资料本地归档

- 原文：将合作 Brief 与实测案例两份飞书 Wiki 保存为可检索 Markdown，登记到 `06-来源原文库/SOURCE_REGISTRY.md`。
- PDF：飞书原始导出分别因文档权限和尺寸上限失败；改用已读取原文生成本地文本版 PDF，并完成首页与中段抽页检查。
- 素材边界：未下载文档内嵌视频；Brief 明确说明视频不可直接下载使用。图片在 PDF 中以文档提供的说明文字呈现。

## 2026-07-20 source cleaning | 小云雀 Seedance 2.5 文本清洗版

- 原始归档：两份飞书 Wiki 原文保持不变，继续作为 Raw source。
- Brief 清洗：移除生成视频、截图、媒体 token 和自动图片描述；将断裂的多行表格重排为“卖点、选题方向、功能入口、格式要求”的可读条目。
- 案例清洗：移除结果输出、生成视频、复刻参考视频和视频输入等纯媒体列；16 张媒体表转换为 110 个“参考素材 + 提示词”案例，保留完整提示词代码块。
- 校验：两份清洗版均无残留飞书媒体标签、替换字符或控制字符；案例库 220 个代码围栏成对闭合。
- 位置：`06-来源原文库/小云雀Seedance2.5-Brief/清洗版/`。

## 2026-09-17 script | Codex 高级使用技巧口播初稿

- content_id：`DW-20260917-CODEX-WORKFLOW-01`；状态：脚本创作中。
- 根据用户本轮初稿、同内容的《9.17 codex高级使用技巧.md》及指定 ChatGPT 聊天分享页，新建《9.17 codex高级使用技巧-口播稿.md》。
- 结构：项目规则 → 会话分工 → 本地记忆 → Skill 渐进加载；采用工作台开发场景解释分工。
- 核对：官方 AGENTS.md、项目与会话、子 Agent、记忆及 Skill 文档；修正规则整份覆盖、多线程必然省 token、固定时长触发永久记忆、加载全部技能元数据等过度表述。
- 产物：约 5–6 分钟口播正文、录屏建议、记忆结构表与来源核对说明；未将演示建议记为已经实测。
- 写前备份与请求收据：`E:/projects/knowledgeProjects/DailyWrite-历史过程稿备份/2026-09-17/codex口播稿写前备份/`；正文、索引及日志写后读回验收。

## 2026-09-17 script revision | Codex 高级使用技巧 v2

- content_id：`DW-20260917-CODEX-WORKFLOW-01`；仍为脚本创作中。
- 用户反馈上一版普通，明确指定 human-strongest-director 重写；读取核心方法论、脚本工作流、用户与内容、语言风格和质量检查说明。
- 主线改为“用多个 AI 却还要自己来回传话”，由一键日报的假设功能串起会话协作、共同规则、历史经验与可复用流程；引用当前项目真实的错误处理要求体现创作者判断。
- 新建《9.17 codex高级使用技巧-口播稿-v2.md》，主索引切换到 v2；已读取用户修订后的首版并保留原文件。
- 正文 1573 个非空白字符、38 段，每段最多 2 句；附画面节奏和事实边界。假设案例未记为实测，不承诺流量或 token 节省。
- 写前备份与请求收据：`E:/projects/knowledgeProjects/DailyWrite-历史过程稿备份/2026-09-17/codex口播稿-v2写前备份/`。

- 2026-09-27T13:27:13.097Z 工作台 analytics-import；content_id: 无；request_id: manual-import-20260927-a011dada0081425f9a7b84424bd734af；关联文件: 见主索引交付元数据。

- 2026-09-27T15:27:02.116Z 工作台 publish；content_id: DW-20260917-CODEX-WORKFLOW-01；request_id: bulk-publish-20260927-2a089ff08e7c49a7a32d76df8be64862；关联文件: 01-内容生产/01-脚本创作中/9.17 codex高级使用技巧-claude-v1-口播稿.md。

- 2026-09-27T15:27:02.295Z 工作台 publish；content_id: DW-20260815-DEEPSEEK-HARNESS-01；request_id: bulk-publish-20260927-48c6d8c158254677b39d84b7fb995b45；关联文件: 01-内容生产/01-脚本创作中/8.15 deepseek harness发布-claude v3.md。

- 2026-09-27T15:27:02.455Z 工作台 publish；content_id: DW-20260715-AI-DEV-SKILL-WORKFLOW-01；request_id: bulk-publish-20260927-189f5289f89b48159135c30bb3caa246；关联文件: 01-内容生产/01-脚本创作中/7.15 硅谷顶级工程师的最新AI开发工作流 -claude-v2.md。

- 2026-09-27T15:27:02.607Z 工作台 publish；content_id: DW-20260620-AI-CREATOR-TRACKER-01；request_id: bulk-publish-20260927-62ac964e85ca4a7d8fcdb279d9f41a3f；关联文件: 01-内容生产/01-脚本创作中/6.20 爬取ai博主视频，并存放多维表格-claude-v1 1.md。

- 2026-09-27T15:27:02.771Z 工作台 publish；content_id: DW-20260605-CC-WORKFLOW-01；request_id: bulk-publish-20260927-e2020e0f6a67402f83e4cf481b3ce0c8；关联文件: 01-内容生产/01-脚本创作中/5.30 claudecode workflow v4 口播稿.md。

- 2026-09-27T15:27:16.674Z 工作台 register；content_id: DW-20260927-63692E72AA32；request_id: bulk-publish-20260927-059226cc08d844328be38924a16fd57e；关联文件: 01-内容生产/01-脚本创作中/7.4 豆包办公任务推广 1.md。

- 2026-09-27T15:27:16.846Z 工作台 publish；content_id: DW-20260927-63692E72AA32；request_id: bulk-publish-20260927-2783e65bac824c64baa27bc9a9b93525；关联文件: 01-内容生产/01-脚本创作中/7.4 豆包办公任务推广 1.md。

- 2026-09-27T15:27:17.010Z 工作台 register；content_id: DW-20260927-34A87258B328；request_id: bulk-publish-20260927-9696509eff624e6a9eac4a3b15210d56；关联文件: 01-内容生产/01-脚本创作中/6.19 ai日报-claude v1 1.md。

- 2026-09-27T15:27:17.148Z 工作台 publish；content_id: DW-20260927-34A87258B328；request_id: bulk-publish-20260927-1ae2db0c45184fe79043d51e379f26e9；关联文件: 01-内容生产/01-脚本创作中/6.19 ai日报-claude v1 1.md。

- 2026-09-27T15:27:17.304Z 工作台 register；content_id: DW-20260927-5E64ADE79FD5；request_id: bulk-publish-20260927-2fc854c45e914da4b2a459cece4508f4；关联文件: 01-内容生产/01-脚本创作中/5.20 微信聊天数据沉淀 -claude v4 口播稿.md。

- 2026-09-27T15:27:17.450Z 工作台 publish；content_id: DW-20260927-5E64ADE79FD5；request_id: bulk-publish-20260927-95c3f590a7614939acc587dd2a85a66d；关联文件: 01-内容生产/01-脚本创作中/5.20 微信聊天数据沉淀 -claude v4 口播稿.md。

- 2026-09-27T15:27:32.864Z 工作台 platform-link；content_id: DW-20260917-CODEX-WORKFLOW-01；request_id: bulk-link-20260927-56042b519e7f4572be50a783884c514c；关联文件: 见主索引交付元数据。

- 2026-09-27T15:27:33.017Z 工作台 platform-link；content_id: DW-20260815-DEEPSEEK-HARNESS-01；request_id: bulk-link-20260927-c7fbe9f44d71455e9fe7591ba908b057；关联文件: 见主索引交付元数据。

- 2026-09-27T15:27:33.143Z 工作台 platform-link；content_id: DW-20260715-AI-DEV-SKILL-WORKFLOW-01；request_id: bulk-link-20260927-4043341fbbca4f45bd09e3f3a9082809；关联文件: 见主索引交付元数据。

- 2026-09-27T15:27:33.277Z 工作台 platform-link；content_id: DW-20260927-63692E72AA32；request_id: bulk-link-20260927-a840e0efac224f7191947f0a1b0663d9；关联文件: 见主索引交付元数据。

- 2026-09-27T15:27:33.414Z 工作台 platform-link；content_id: DW-20260620-AI-CREATOR-TRACKER-01；request_id: bulk-link-20260927-f424982c058548399d348702e2fe0441；关联文件: 见主索引交付元数据。

- 2026-09-27T15:27:33.553Z 工作台 platform-link；content_id: DW-20260620-AI-CREATOR-TRACKER-01；request_id: bulk-link-20260927-7472bad69d524757b7d23a0c5d52db9f；关联文件: 见主索引交付元数据。

- 2026-09-27T15:27:33.687Z 工作台 platform-link；content_id: DW-20260927-34A87258B328；request_id: bulk-link-20260927-4c418a611099499dbf459ef061a590db；关联文件: 见主索引交付元数据。

- 2026-09-27T15:27:33.827Z 工作台 platform-link；content_id: DW-20260605-CC-WORKFLOW-01；request_id: bulk-link-20260927-970f562ce9894276815bc27d91c39a7f；关联文件: 见主索引交付元数据。

- 2026-09-27T15:27:34.038Z 工作台 platform-link；content_id: DW-20260927-5E64ADE79FD5；request_id: bulk-link-20260927-16379e5674d24d1cad7cc96e7046a1f7；关联文件: 见主索引交付元数据。

- 2026-09-27T15:31:16.247Z 工作台 register；content_id: DW-20260927-13FCB3D74AE1；request_id: codex-register-image-comparison-f26a551f057b442481c6251cfa310c9e；关联文件: 01-内容生产/01-脚本创作中/9.15 豆包生图和gpt生图对比-claude-v2.md。

- 2026-09-27T15:31:16.412Z 工作台 publish；content_id: DW-20260927-13FCB3D74AE1；request_id: codex-publish-image-comparison-bea224e1da3346b5b22b08b8928a2f29；关联文件: 01-内容生产/01-脚本创作中/9.15 豆包生图和gpt生图对比-claude-v2.md。

- 2026-09-27T15:31:16.575Z 工作台 register；content_id: DW-20260927-5AE65027300B；request_id: codex-register-ai-ppt-7b604565a0f54494ac9f54ffff5067c9；关联文件: 01-内容生产/01-脚本创作中/2.11 ai ppt神器 Gemini-发布稿.md。

- 2026-09-27T15:31:16.726Z 工作台 publish；content_id: DW-20260927-5AE65027300B；request_id: codex-publish-ai-ppt-c84fb91f34324d3cabfd2484fff38a38；关联文件: 01-内容生产/01-脚本创作中/2.11 ai ppt神器 Gemini-发布稿.md。

- 2026-09-27T15:31:55.642Z 工作台 platform-link；content_id: DW-20260503-CODEX-PET；request_id: codex-platform-link-7635692430432033673-358435f3bd7f47b4b1164f9616858273；关联文件: 见主索引交付元数据。

- 2026-09-27T15:31:55.797Z 工作台 platform-link；content_id: DW-20260429-MIMO-MULTIMODAL；request_id: codex-platform-link-7634182951772753190-b8a548efe2f046eeafd6fe9e89d0af50；关联文件: 见主索引交付元数据。

- 2026-09-27T15:31:55.953Z 工作台 platform-link；content_id: DW-20260428-CLAUDE-DESKTOP-CN；request_id: codex-platform-link-7633474967338718638-c39be15cedad4bcabbd891d3edfb53f5；关联文件: 见主索引交付元数据。

- 2026-09-27T15:31:56.102Z 工作台 platform-link；content_id: DW-20260422-CLAUDECODE-COMMANDS；request_id: codex-platform-link-7631568120880599731-bf3f7697a2124759baf6ec04d184f018；关联文件: 见主索引交付元数据。

- 2026-09-27T15:31:56.242Z 工作台 platform-link；content_id: DW-20260420-GEMMA-CLAUDECODE；request_id: codex-platform-link-7630698435666038051-a8754f3b3af94705accfa4d277469415；关联文件: 见主索引交付元数据。

- 2026-09-27T15:31:56.381Z 工作台 platform-link；content_id: DW-20260412-VIDEO-TO-NOTES-SKILL；request_id: codex-platform-link-7627850088028109222-891bb19abb93413b94f200cad65ab5bb；关联文件: 见主索引交付元数据。

- 2026-09-27T15:31:56.524Z 工作台 platform-link；content_id: DW-20260410-WECHAT-CHAT-ANALYSIS；request_id: codex-platform-link-7627107053455485542-fdb9bcdaeb55468a89a544021b3affb3；关联文件: 见主索引交付元数据。

- 2026-09-27T15:31:56.663Z 工作台 platform-link；content_id: DW-20260331-GSTACK；request_id: codex-platform-link-7623331041310182656-552a290e60c547ba9da7aa11251990ac；关联文件: 见主索引交付元数据。

- 2026-09-27T15:31:56.868Z 工作台 platform-link；content_id: DW-20260326-OPENCLAW-CLAUDECODE-ACP；request_id: codex-platform-link-7621438252230151466-70888b7e355246ecb4064c9c35169bc9；关联文件: 见主索引交付元数据。

- 2026-09-27T15:31:57.094Z 工作台 platform-link；content_id: DW-20260318-OPENCLAW-AGENT-TEAM；request_id: codex-platform-link-7618582013578120463-61f0bcdba3d24bc489d6dd8bf0ef2de8；关联文件: 见主索引交付元数据。

- 2026-09-27T15:31:57.296Z 工作台 platform-link；content_id: DW-20260316-OPENCLAW-MINIMAX；request_id: codex-platform-link-7617834153031093531-182de32c6e584d0481abcf949a2c2f2f；关联文件: 见主索引交付元数据。

- 2026-09-27T15:31:57.436Z 工作台 platform-link；content_id: DW-20260312-OPENCLAW-BUGS；request_id: codex-platform-link-7616037367098412294-fccb90174748451b869d326f29d759e0；关联文件: 见主索引交付元数据。

- 2026-09-27T15:31:57.566Z 工作台 platform-link；content_id: DW-20260307-OPENCLAW-SKILLS；request_id: codex-platform-link-7614496760291020067-8885cbe6942c4c53b94de79a8e02851c；关联文件: 见主索引交付元数据。

- 2026-09-27T15:31:57.706Z 工作台 platform-link；content_id: DW-20260927-5AE65027300B；request_id: codex-platform-link-7605605168641592639-426f3cf409cb47da84533fd2aac25527；关联文件: 见主索引交付元数据。

- 2026-09-27T15:31:57.867Z 工作台 platform-link；content_id: DW-20260208-VIBE-CODING；request_id: codex-platform-link-7604485515164880163-f91c345d2bf246f2826e67e8dd918a50；关联文件: 见主索引交付元数据。

- 2026-09-27T15:31:58.015Z 工作台 platform-link；content_id: DW-20260207-AGENT-SKILLS-INSTALL；request_id: codex-platform-link-7604090738770529546-40cbd12c1b534056a776301453c05cb3；关联文件: 见主索引交付元数据。

- 2026-09-27T15:31:58.152Z 工作台 platform-link；content_id: DW-20260205-CLAUDECODE-VSCODE；request_id: codex-platform-link-7603380758333508904-9d2faa4e4832408092497803a9204baf；关联文件: 见主索引交付元数据。

- 2026-09-27T15:31:58.305Z 工作台 platform-link；content_id: DW-20260204-CLAUDECODE-AGENT-TEAM；request_id: codex-platform-link-7602978535447285032-04717ef720d34569a9c0700ef752e167；关联文件: 见主索引交付元数据。

- 2026-09-27T15:31:58.433Z 工作台 platform-link；content_id: DW-20260128-REMOTION-CODE-VIDEO；request_id: codex-platform-link-7600394302530800923-da3b9e8090db45709f87c6118ad37f61；关联文件: 见主索引交付元数据。

- 2026-09-27T15:31:58.579Z 工作台 platform-link；content_id: DW-20260122-AI-CHAT-NAVIGATION；request_id: codex-platform-link-7598195002128207104-1336beeebab6433b84abee8960da321d；关联文件: 见主索引交付元数据。

- 2026-09-27T15:31:58.718Z 工作台 platform-link；content_id: DW-20260117-MANUS-DANKOE；request_id: codex-platform-link-7596327998182264105-7fc3886035ae4a649dfe54bf73a85d71；关联文件: 见主索引交付元数据。

- 2026-09-27T16:29:43.842Z 工作台 analytics-import；content_id: 无；request_id: ca7dd338-a014-4540-87fe-2b5a8c755c39；关联文件: 见主索引交付元数据。

- 2026-09-27T16:29:45.085Z 工作台 analytics-import；content_id: 无；request_id: 9fbb7736-119f-4ef5-ba1d-af6336fc3c7d；关联文件: 见主索引交付元数据。

- 2026-09-27T16:59:55.726Z 工作台 correct-published-body；content_id: DW-20260927-34A87258B328；request_id: correct-ai-daily-20260928-v1；关联文件: 01-内容生产/01-脚本创作中/6.19 ai日报-claude v1 口播稿.md；原因: 用户确认 6.19 ai日报-claude v1 口播稿.md 是实际发布正文；原入库文件仅为配套建议。

- 2026-09-27T16:59:55.748Z 工作台 withdraw-incorrect-publication；content_id: DW-20260927-63692E72AA32；request_id: withdraw-doubao-20260928-v1；关联文件: 03-已发布归档/已发布成品/DW-20260927-63692E72AA32.md；原因: 用户确认豆包办公任务没有发布；此前把平台导出记录和残缺 Markdown 误登记为该作品。

- 2026-09-27T17:13:21.343Z 工作台 register；content_id: DW-20260927-C49B7E6A2AFE；request_id: register-doubao-creative-20260928-v1；关联文件: 01-内容生产/01-脚本创作中/6.28 豆包使用分享 -创意视频 -v4-口播稿.md。

- 2026-09-27T17:13:21.518Z 工作台 publish；content_id: DW-20260927-C49B7E6A2AFE；request_id: publish-doubao-creative-20260928-v1；关联文件: 01-内容生产/01-脚本创作中/6.28 豆包使用分享 -创意视频 -v4-口播稿.md。

- 2026-09-27T17:13:21.682Z 工作台 platform-link；content_id: DW-20260927-C49B7E6A2AFE；request_id: link-doubao-creative-20260928-v1；关联文件: 见主索引交付元数据。

- 2026-09-27T17:17:47.741Z 工作台 register；content_id: DW-20260927-A8082587F1DC；request_id: register-ai-creator-tracker-episode2-20260928-v1；关联文件: 01-内容生产/01-脚本创作中/6.22 爬取ai博主视频，并存放多维表格第二集 1-口播稿.md。

- 2026-09-27T17:17:47.910Z 工作台 publish；content_id: DW-20260927-A8082587F1DC；request_id: publish-ai-creator-tracker-episode2-20260928-v1；关联文件: 01-内容生产/01-脚本创作中/6.22 爬取ai博主视频，并存放多维表格第二集 1-口播稿.md。

- 2026-09-27T17:17:48.087Z 工作台 platform-link；content_id: DW-20260927-A8082587F1DC；request_id: relink-ai-creator-tracker-episode2-20260928-v1；关联文件: 见主索引交付元数据。

- 2026-09-27T17:20:24.7611940Z 已发布视频版本归档：10 组、39 个非最终 Markdown 已移至外层冷备份；清单及逐文件原路径、目标路径、SHA256 见 E:/projects/knowledgeProjects/DailyWrite-历史过程稿备份/2026-09-28/已发布视频版本归档/manifest.json；最终发布稿保留原位，6.25 AI 博主追踪第二集已独立登记。
