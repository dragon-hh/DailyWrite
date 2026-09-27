# AI Builders Digest — 2026-08-25

## X / TWITTER

### Thibault Sottiaux，OpenAI Codex 与 ChatGPT 团队

Thibault Sottiaux 表示，此前发现的账户用量问题已经部署了一轮重置和修复，用户应该能明显感受到改善，后续还会继续更新。他同时判断，2026 年企业会真正开始重视模型效率与可靠性，因为模型正在从可选工具变成关键基础设施，成本控制和稳定运行也因此进入核心议题。

- https://x.com/thsottiaux/status/2091688655828246890
- https://x.com/thsottiaux/status/2091581575108653374

### Peter Yang，AI 教程与访谈创作者

Peter Yang 将 AI eval 分成两类：自上而下的 eval，是从任务描述出发推导理想标准，Claude 很擅长协助完成；自下而上的 eval，则来自大量真实输出中的直觉反馈，需要人把模糊的不满意外化成可检查标准。他强调，模型能帮你搭建预期，却很难代替你从实际失败样本中识别真正的问题。

- https://x.com/petergyang/status/2091586298779955512

### Madhu Guru，Meta AI 高级总监

Madhu Guru 提出，eval 的颗粒度应该遵循“刚刚好”原则：不要只判断最终答案，也不要细到失去行动价值，而要围绕完成任务所需的各个 job 来评估。以金融分析 agent 为例，应分别检查客户理解、证据收集、数据分析和最终推荐；这样即使推荐错误，也能从各阶段分数定位问题究竟出在哪里，再决定是否需要继续拆分复杂步骤。

- https://x.com/realmadhuguru/status/2091684812012875981

### Guillermo Rauch，Vercel CEO

Guillermo Rauch 认为，推理价格下降会快速释放需求。OpenAI Sol 在 Vercel AI Gateway 上降价后成为增长最快的 frontier model，说明智能需求具有很高的价格弹性；他据此判断，能自动利用价格波动来降低成本、提高利润的 gateway 会逐渐成为必需品。

在 agent 扩展机制上，他主张采用开放协议，包括 MCP、Skills 和 Plugins，并把 Unix 视为最重要的设计范式：每个小程序只做好一件事，再通过组合形成复杂系统。配合可嵌入的 libfx，同一能力可以进入自定义 CLI、后台 agent 或 software factory，并在本地或云端运行。

- https://x.com/rauchg/status/2091671326897713424
- https://x.com/rauchg/status/2091583525661384813

### Garry Tan，Y Combinator 总裁兼 CEO

Garry Tan 给出一个直接预测：传统 system of record 必须演化成 AI harness，否则会被 agent 取代。其核心不只是给既有数据库加一个聊天入口，而是让记录系统承担 agent 运行所需的上下文、权限、工具和执行约束；如果系统无法成为 agent 的工作环境，agent 就会绕开它建立新的操作层。

- https://x.com/garrytan/status/2091742825042030681

### Peter Steinberger，OpenClaw 与 OpenAI Builder

Peter Steinberger 认为，CLI 虽然好用，但把执行过程做成可视化 UI，并直接放进团队日常工作的界面里，协作体验会更完整。他还给自己的项目加入了旋转 USB 协议，让 agent 能控制 360 度摄像头观察周围环境，展示了 agent 从纯软件工具延伸到实体设备控制的一种轻量路径。

- https://x.com/steipete/status/2091650136506327253
- https://x.com/steipete/status/2091639468935831910

## OFFICIAL BLOGS

### Claude Blog

#### Building intelligent apps for Apple platforms with Claude in the Foundation Models framework

Claude Blog 宣布推出一个新的 Swift package，让 Apple 开发者可以通过 Foundation Models framework 调用 Claude。Apple 的框架原本适合在设备端完成快速、本地的摘要与信息抽取，并能借助 `@Generable` 返回类型明确的 Swift 值；现在，当任务需要多步推理、代码生成、联网搜索或数据分析时，应用可以把干净的结构化输入交给 Claude，再把流式结果、工具调用和结构化响应返回同一个 SwiftUI 界面。

这套组合的重点是按任务选择合适的模型，而不是让一个模型包办全部流程。文章用日记和学习应用举例：设备端模型可以生成提示或解释术语，Claude 则负责跨数月内容寻找线索，或回答需要联系更广知识背景的追问。原文对此的概括是：“It's one experience for the user, backed by the right model for each step.”

对开发者而言，实际变化是可以在 Apple 原生框架中保留统一体验，同时把复杂任务升级到 Claude。该支持将在次日开放，适用于 iOS 27、iPadOS 27、macOS 27、visionOS 27 和 watchOS 27；接入时需要 Anthropic API key。

https://claude.com/blog/claude-for-foundation-models

Generated through the Follow Builders skill: https://github.com/zarazhangrui/follow-builders
