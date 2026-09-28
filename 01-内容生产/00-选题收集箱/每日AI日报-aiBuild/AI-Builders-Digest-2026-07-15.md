# AI Builders Digest — 2026-07-15

## X / TWITTER

### Swyx（Cognition、AI Engineer、Latent Space 等）

Swyx 分享了自己处理大型项目时的多模型分工：用 Sol Ultra 做规划、Fable 5 做批评、Sonnet 5 / Terra Ultra / SWE 1.7 执行编码，再由 Devin Review 复核。他尤其强调，应先用 “grill-me” 或 “interview-me” 一类 prompt 把关键决策问清楚，再让 agent 动手。

来源：https://x.com/swyx/status/2076811977918484795

### Thibault Sottiaux（OpenAI，Codex & ChatGPT）

Thibault Sottiaux 暗示活跃用户可能即将达到 800 万，并发布了 “ChatGPT Work presents” 的产品相关内容，但原帖没有给出更多文字细节。

来源：https://x.com/thsottiaux/status/2076907789763621237

来源：https://x.com/thsottiaux/status/2076894071323537898

### Peter Yang（AI 教程与访谈创作者）

Peter Yang 提议识别并封禁那些总在大账号发帖后瞬间回复的账号，认为这类行为往往来自 AI bot。其余更新主要是餐厅和个人评论，没有值得展开的 AI 建设内容。

来源：https://x.com/petergyang/status/2076897407439454577

### Nan Yu（Linear 产品负责人）

Nan Yu 指出，如果观察软件行业之外那些职位中带有 “designer” 的工作，就更容易看清设计职责的本质。他还用 “Chinese room” 简短回应了一则引用内容，但现有文本不足以还原更多上下文。

来源：https://x.com/thenanyu/status/2076783865528516971

来源：https://x.com/thenanyu/status/2076713481177374749

### Cat Wu（Anthropic，Claude Code + Cowork）

Cat Wu 宣布 Artifacts 获得升级。原帖只提供了简短公告，没有列出具体功能细节。

来源：https://x.com/_catwu/status/2076867882894684314

### Thariq（Anthropic，Claude Code）

Thariq 表示升级后的 Artifacts 表达力更强，也能以更有创意的方式组合。他喜欢为项目创建可共享、可编辑的 dashboard，并让本地 Claude Code session 继续修改它。

来源：https://x.com/trq212/status/2076790799011131735

### Amjad Masad（Replit CEO）

Amjad Masad 正在接收模型训练任务的实时进度更新。他把这种体验比作早期 vibe coding，只不过现在被实时塑造的是个人模型。

来源：https://x.com/amasad/status/2076776737074184661

### Guillermo Rauch（Vercel CEO）

Guillermo Rauch 表示，一款产品目前最受欢迎的两项能力是易用的 filesystem API 与 observability，团队将继续加强两者。他还把“让 agent 用 feature flag 自主设置并调优实验”视为构建自优化网站和应用的重要模块。另一个值得注意的数据是，open-weight 模型已承载 29% 的 gateway token，高于 4 月的 11%。

来源：https://x.com/rauchg/status/2076817174073880957

来源：https://x.com/rauchg/status/2076786138195595704

来源：https://x.com/rauchg/status/2076713720731042174

### Aaron Levie（Box CEO）

Aaron Levie 认为 AI 产业不会走向单一赢家，而会形成长期共存的多层结构：frontier lab 持续推进能力边界，open-weight 模型快速吸收突破并降低成本，Applied AI 层负责结合不同模型、领域上下文、eval 与企业工作流，企业自身则重点维护数据和权限上下文。

他判断未来 model routing 的典型模式，是让 frontier intelligence 扮演“管理者”，把工作委派给低成本模型。真正的差异化不只是选模型，而是理解业务问题，并建立能把任务正确路由到不同模型的 harness。

他也提醒，“每家企业训练自己的模型”比想象中难：企业最有价值的信息持续变化且高度敏感，访问控制不能简单塞进模型或 agent。定制模型会大幅增加，但更可能集中在高价值的领域产品，而非每家企业各训一套通用模型。

来源：https://x.com/levie/status/2076882332821373381

来源：https://x.com/levie/status/2076839463410671637

来源：https://x.com/levie/status/2076764958579446006

### Ryo Lu（Cursor 设计师，前 Notion、Stripe）

Ryo Lu 用 Cursor 为 Xteink X3 / X4 制作了定制电子阅读器固件，重点支持 Latin 与 CJK 字体、竖排、禁则、大字符集，以及图书和阅读进度同步、快速渲染与缓存。这是 AI coding agent 进入硬件改造和多语言排版的一个具体案例。

来源：https://x.com/ryolu_/status/2076713331113734641

来源：https://x.com/ryolu_/status/2076713700942295226

### Garry Tan（Y Combinator 总裁兼 CEO）

Garry Tan 宣称“绅士科学家的时代回来了”。原帖是引用内容，现有 JSON 没有提供被引用帖正文，因此不进一步推断其具体所指。

来源：https://x.com/garrytan/status/2076587412516421945

### Zara Zhang（Builder）

Zara Zhang 提出了组织采用 AI 的三个层级，并判断大多数公司仍处于第二级。她还分享了一段 45 分钟对谈，主题包括公开构建、在不制造低质内容的前提下增长 X 受众，以及她对 vibe coding 的看法。

来源：https://x.com/zarazhangrui/status/2076862290985730481

来源：https://x.com/zarazhangrui/status/2076860372993388663

### Nikunj Kothari（FPV Ventures 合伙人）

Nikunj Kothari 开源了 Ramp-Autofill skill，用 Ramp CLI 与 Claude Fable 自动处理报销：从 iMessage、Gmail 和网页链接寻找并附加收据，依据 Google Calendar 补充会面信息，学习组织过往的 memo 与分类风格，自动分类缺失交易，并在核验后标出异常。它还能作为定时任务运行；他用它处理了过去 60 天的费用。

来源：https://x.com/nikunj/status/2076775924650107151

来源：https://x.com/nikunj/status/2076776777884811671

### Peter Steinberger（OpenClaw + OpenAI）

Peter Steinberger 把 maintainer agent 迁到了云端，并调侃这些 agent 已经开始“打架”。他还宣布 iOS、Android 应用获得更新；若自动更新失败，需要运行 web installer 处理 Node 版本升级。对于 agent 工作流，他推荐直接使用 “stress test” 作为 prompt。

来源：https://x.com/steipete/status/2076923300593422560

来源：https://x.com/steipete/status/2076917691139674373

来源：https://x.com/steipete/status/2076886451455992249

### Aditya Agarwal（South Park Commons GP、Bevel Health 联合创始人）

Aditya Agarwal 用一个生活化例子说明 coding agent 的用途正在外溢：他不确定自己究竟在用 Codex 还是 ChatGPT，但已经让这个“AGI 级 coding agent”帮女儿研究 Benson Boone 戴什么项链。

来源：https://x.com/adityaag/status/2076821102194721167

### Sam Altman

Sam Altman 对模型访问中的静默降级表达了尖锐讽刺，并称某则相关内容荒诞到让他一度以为是仿冒账号发的讽刺帖。他还表示，看到自家模型终于擅长设计，仍让他感到难以置信。

来源：https://x.com/sama/status/2076824870072238299

来源：https://x.com/sama/status/2076824686307271125

来源：https://x.com/sama/status/2076823209589313910

## OFFICIAL BLOGS

### Claude Blog

#### Building intelligent apps for Apple platforms with Claude in the Foundation Models framework

Claude 发布了面向 Apple Foundation Models framework 的 Swift package，让 Apple 开发者可以在同一套原生 Swift 工作流中，把简单、快速、隐私敏感的任务交给设备端模型，再把多步推理、代码生成、网页搜索或数据分析等复杂任务交给 Claude。

Apple framework 能借助 `@Generable` 输出 typed Swift values，因此传给 Claude API 的输入可以是清晰的结构化数据，而不是未经处理的用户文本。package 同时处理 streaming、tool call 和结构化响应，并把结果送回 SwiftUI view。

实际意义是“按任务选择正确模型”：例如日记应用先在设备端生成每日提示，再让 Claude 跨数月记录寻找线索；学习应用先本地解释术语，再把跨知识点推理交给 Claude。原文称该支持将于次日提供，适用于 iOS 27、iPadOS 27、macOS 27、visionOS 27 和 watchOS 27，并需要 Anthropic API key。

来源：https://claude.com/blog/claude-for-foundation-models

## PODCASTS

本次 JSON 中的 podcast 条目只提供了频道页 URL，并非具体视频 URL。根据 digest 的强制链接规则，本期不收录该条目。

Generated through the Follow Builders skill: https://github.com/zarazhangrui/follow-builders
