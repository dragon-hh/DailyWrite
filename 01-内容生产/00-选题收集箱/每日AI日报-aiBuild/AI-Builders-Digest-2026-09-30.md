# AI Builders Digest — 2026-09-30

## X / TWITTER

### Boris Cherny，Anthropic Claude Code

Boris Cherny 展示了 Sonnet 5.5 在 Claude Code 中修复 bug 的效果：完成速度提升 30%，用量减少 30%。这组结果的重点不只是模型更快，而是更强的推理能力正在直接降低完成同一项工程任务所需的 token 成本。

原文：https://x.com/bcherny/status/2104638725317923228

### Thibault Sottiaux，OpenAI Codex 与 ChatGPT

Thibault Sottiaux 宣布，OpenAI 将重新开放每月 200 美元的 Pro 订阅，但会调整用量计算方式，按 API 标价折算后约为旧方案的一半。他强调不会恢复 5 小时限制，并称模型降价和效率提升会持续增加单位订阅费用能完成的工作量；同时预告订阅中将加入不消耗用量的新能力。

原文：https://x.com/thsottiaux/status/2104823812042940713

### Peter Yang，AI 教程创作者

Peter Yang 认为，与其在 OpenAI 和 Anthropic 每次领先变化后迅速唱衰另一方，不如关注两家持续竞争给所有用户带来的收益。他还用 Sonnet 5.5 做出了一个可玩的 StarCraft 关卡，整合 Sketchfab 模型和 Suno 音乐，展示了新模型把代码、设计与多媒体资产组合成完整体验的能力。

原文：https://x.com/petergyang/status/2104809410040336784

演示：https://x.com/petergyang/status/2104736498151256303

### Cat Wu，Anthropic Claude Code 与 Cowork

Cat Wu 表示，Sonnet 5.5 在 Claude Code 中能让用户多完成约 30% 的任务，因为更高的智能水平让它完成同样工作时需要更少 token。在她展示的工具调用测试中，新模型比 Sonnet 5 快 24 秒，同时少用了 6,000 个 token。

原文：https://x.com/_catwu/status/2104639552170377399

### Thariq，Anthropic Claude Code

Thariq 判断，Sonnet 5.5 和 Opus 5.5 的效率提升，会让 projects、Claude tag 和动态 workflow 这类高层抽象不再因为 token 成本而难以落地。他还指出，如今“把 prompt 发给我”已经不足以复现一个 agent 工作流，真正的上下文往往包括参考资料、skills、示例、其他代码库和外部工具。

原文：https://x.com/trq212/status/2104660926373023830

延伸观点：https://x.com/trq212/status/2104608785696440510

### Guillermo Rauch，Vercel CEO

Guillermo Rauch 宣布 Vercel 域名搜索现在无需认证，这对需要自动发现资源的 agent 尤其有用。他还分享了一次成熟项目迁移：在尽量少人工干预的情况下，一周内完成主要工作，构建速度提升约 70%，页面绘制速度提升约 75%，并从迁移中沉淀出两项将公开的 AI skills。

原文：https://x.com/rauchg/status/2104764419305796094

迁移案例：https://x.com/rauchg/status/2104660502723072281

### Alex Albert，Anthropic Research

Alex Albert 认为 Sonnet 5.5 延续了他喜欢的 Opus 5.5 特质：表达清晰、响应很快，同时相较 Sonnet 5 有明显能力跃升。他尤其认可它作为高频迭代模型的手感，这说明模型体验的价值不仅来自单次上限，也来自日常反馈循环的速度与稳定性。

原文：https://x.com/alexalbert__/status/2104633937280811010

### Aaron Levie，Box CEO

Aaron Levie 分享了 Box Agent 对 Sonnet 5.5 的企业知识工作评测：最难测试的总分提高 4 分，生成最终交付物的速度约为原来的 2.4 倍，同时少用 12% 的 token。行业任务提升更明显，包括金融服务提高 18 个百分点、法律提高 7 个百分点、生命科学提高 8 个百分点、公共部门提高 7 个百分点；模型还在财务计算、拒绝编造法律基准、统计标准差和提取学生进度数据等具体任务上取得明显改进。

原文：https://x.com/levie/status/2104648654074343480

### Ryo Lu，产品设计师与创业者

Ryo Lu 展示了面向台湾 YouBike 的城市骑行体验，支持站点查询、导航和语音实时转向提示。这个小产品把公共交通的实时信息直接变成可执行的出行流程，比单纯展示地图更接近用户真正需要的下一步。

原文：https://x.com/ryolu_/status/2104546903807660224

### Nikunj Kothari，FPV Ventures Partner

Nikunj Kothari 反驳“融资越多、分发就越能形成壁垒”的简单叙事：当大型 incumbents 真正动用既有分发能力时，资本本身并不能保护创业公司。他建议回到第一性原理，寻找不公平优势，打造高留存、最好具备网络效应的产品，把资本当作复利工具而不是命运，并尽早建立可自我维持的业务。

原文：https://x.com/nikunj/status/2104566122549063756

### Dan Shipper，Every CEO

Dan Shipper 的实际工作评测显示，Sonnet 5.5 的写作能力相较 Opus 5.5 明显改善，在修订任务上甚至优于他偏爱的 Astra；同时它比 Opus 5.5 更快、更便宜，适合快速迭代代码和设计。不过团队成员也提出相反判断：当顶级模型覆盖面越来越广，中档模型在个人工具栈中的位置可能会被压缩。

原文：https://x.com/danshipper/status/2104636728992776510

### Claude，Anthropic AI Assistant

Claude 官方展示了 Sonnet 5.5 的两个代码生成案例：同一 prompt 下的弹跳球物理效果对比，以及完全用代码逐帧绘制的像素风森林生物。它们共同指向一个更实用的进步：模型不仅能生成能运行的界面，还能更稳定地处理物理细节与连续视觉表达。

原文：https://x.com/claudeai/status/2104675003673325732

演示：https://x.com/claudeai/status/2104675000787603486

Generated through the Follow Builders skill: https://github.com/zarazhangrui/follow-builders
