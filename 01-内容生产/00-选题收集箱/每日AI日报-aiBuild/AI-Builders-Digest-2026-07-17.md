# AI Builders Digest｜2026-07-17

## X / TWITTER

### Swyx（AI Engineer、Latent Space 等项目参与者）

Swyx 认为 Computer Use Agent 正在以远超许多人认知的速度进步。他从 2017 年的 World of Bits 一路跟踪到 Adept、Anthropic Computer Use 和 Claude Cowork，如今判断 GPT-5.6 + Superapp 的 CUA 能力已经超过此前方案；如果决策者仍低估它，可能犯下危险的能力判断错误。他也在推动非技术团队尽量用 CUA 处理付款、发票及活动数据请求等真实知识工作。

来源：https://x.com/swyx/status/2077475285205958771

### Google VP Josh Woodward

Josh Woodward 宣布 Gemini Spark 正向更多国家和地区的 Ultra 订阅用户开放，并新增四项能力：直接打开和编辑 Google Docs、读取 Google Sheets 与 Slides 评论、整体速度提升超过 50%，以及跨多个来源并行处理任务。另据首份 Gemini 东南亚报告，过去一年活跃用户翻倍，70% 的 prompt 使用本地语言，40% 的 prompt 只使用语音、图片或视频，显示本地语言、多模态与移动端正在共同拉动增长。

来源：https://x.com/joshwoodward/status/2077471111240204457

来源：https://x.com/joshwoodward/status/2077411104775406045

来源：https://x.com/joshwoodward/status/2077411109326221322

### Anthropic Claude Code 团队 Boris Cherny

Boris Cherny 的核心判断是：agent 时代，工程团队更该把领域知识变成基础设施。lint、CI、测试等传统自动化会同时放大每个 agent 的产出，而 CLAUDE.md、REVIEW.md、skills、代码注释和记忆，则可以把过去只存在于资深成员脑中的规则编码下来。他甚至把新贡献者因选错框架或违反架构模式而被拒绝视为“自动化失败”，因为理想状态应是 agent 在无需提问者补充上下文的情况下就能正确工作。

来源：https://x.com/bcherny/status/2077460395279692197

### OpenAI Codex 与 ChatGPT 团队 Thibault Sottiaux

Thibault Sottiaux 说明了 GPT-5.6 极少数误删文件报告的常见链路：用户开启 full access、关闭 sandbox 或 auto review，模型又试图覆盖 `$HOME` 作为临时目录，随后误把真正的 home 目录删除。OpenAI 正在更新 developer message、引导使用更安全的权限模式并增加 harness 防护，后续还会发布详细复盘。他同时征集 Codex Plus/Pro 取消 5 小时限制后的使用反馈，以及 ChatGPT 与 Codex 合并后的下一步产品整合方向。

来源：https://x.com/thsottiaux/status/2077630111499882637

来源：https://x.com/thsottiaux/status/2077632589498913087

来源：https://x.com/thsottiaux/status/2077627035418239230

### AI 教程创作者 Peter Yang

Peter Yang 认为 OpenAI 当前最大的错失机会，是 ChatGPT Live 与 Codex 两款强产品彼此不通。他希望语音助手能直接调用已连接的 plugins、tools 和 browser，在实时对话里完成回邮件、排会议、改文档和写代码，而不是只能聊天却无法行动；第一步应让 ChatGPT Live 感知用户已经连接的 plugins。

来源：https://x.com/petergyang/status/2077572198655754583

### Meta AI 高级总监 Madhu Guru

Madhu Guru 给 AI 味过重的文字提出了几个形象说法：“semantic nausea”“uncanny prose valley”和“synthetic shudder”。他的实践调整也很明确：AI 主要留在 brainstorming 阶段用于打磨想法，最终成文则由人来写，以避免标准化的 AI 表达渗入个人文风。

来源：https://x.com/realmadhuguru/status/2077413491586253025

来源：https://x.com/realmadhuguru/status/2077414312180932668

### Anthropic Claude Code 团队 Thariq

Thariq 把理想 prompting 概括为“薄 prompt、厚 artifacts 与 context、薄 skills”：少用冗长指令，把可靠信息沉淀到可复用上下文和产物中，同时让 skills 保持轻量。他进一步强调，软件工程本质上是自动化职业，这与把领域知识编码为 agent 可执行基础设施的方向一致。

来源：https://x.com/trq212/status/2077539537992229076

来源：https://x.com/trq212/status/2077490092290253259

### Vercel CEO Guillermo Rauch

Guillermo Rauch 分享 Vercel Sandbox 的增长数据：DAU 月环比增长 100%，每天创建超过 350 万个 sandbox，并采用 Active CPU 计价模式。Web Analytics API 的实际价值也不只是看流量，它可以让 agent 把访客、自定义购买或结账事件，与部署和性能变化关联起来，还能与 Stripe、Resend 数据放在同一自定义界面中分析。

来源：https://x.com/rauchg/status/2077559189015335019

来源：https://x.com/rauchg/status/2077426190386946539

### Box CEO Aaron Levie

Aaron Levie 总结企业 agent 落地的几个现实瓶颈：变革管理和数据准备仍是核心，跨部门工作流会迅速触及复杂的权限与数据建模问题，因此 agent 需要独立角色和权限；越来越多 IT 团队把工程师直接嵌入业务部门，以避免数月的低效试验。企业也在构建按任务路由的多模型系统，用 frontier model 编排、低成本或调优模型执行；长期看，企业软件必须 headless，无法友好服务 agent 的传统厂商面临明显风险。

来源：https://x.com/levie/status/2077526010753581156

来源：https://x.com/levie/status/2077471148699439152

### Y Combinator CEO Garry Tan

Garry Tan 认为 skill 文件的可移植性可以降低对某一个 frontier model 的依赖。它把流程和知识放到模型之外，使团队能在不同模型之间迁移，而不必每次重建全部工作方式。

来源：https://x.com/garrytan/status/2077626565517590618

### Builder Zara Zhang

Zara Zhang 的观点是，企业若真想让 agent 工作，就必须把公司设计成“可被读取”的系统。她举出 Shopify 的做法：agent 不设私聊功能、只进入公开频道，意外带来的副作用是促进同伴学习。她还把 coding agent 视为创造和自我表达工具，形容 GitHub 就像自己的 Substack。

来源：https://x.com/zarazhangrui/status/2077417579837309040

来源：https://x.com/zarazhangrui/status/2077388091044635010

### OpenClaw 与 OpenAI 的 Peter Steinberger

Peter Steinberger 转引并认同一个很强的工程判断：陌生代码库中的 PR 因不符合框架或架构惯例而被拒绝，本质上暴露的是自动化不足。他也评价 GPT-5.6 “relentless”，呼应了 agent 能力快速提升带来的新工作方式。

来源：https://x.com/steipete/status/2077544756390088777

来源：https://x.com/steipete/status/2077614430658191825

### Every CEO Dan Shipper

Dan Shipper 提炼 Granola CEO Chris Pedregal 的判断：会议纪要并不是最终战场，真正的竞争是成为 AI-native 工作世界的核心界面。即使 Notion、OpenAI 和 Zoom 复制了类似功能，Granola 的增长并未因此改变；更值得关注的是 proactive AI、会议前上下文，以及“bring your own agent”的 API/MCP 路线。

来源：https://x.com/danshipper/status/2077410279474770229

## OFFICIAL BLOGS

### Claude Blog

#### Claude Code now supports artifacts

Claude Code 现在可以把会话中的工作进展生成为 artifact，也就是持续更新、可分享的可视化网页。它能利用会话完整上下文，包括代码库、connectors 和对话，把 PR walkthrough、系统说明、dashboard、release checklist，甚至事故调查时间线组合在一个页面里；每次发布都会在同一链接更新，并保留版本历史。

其核心价值是把 agent 的过程状态变成团队共享界面：“team members and stakeholders don’t have to ‘walk us through what the agent found’。”artifact 默认仅作者可见，可分享给组织成员，但不能公开；管理员可控制组织级开关、角色范围、保留策略和 compliance API。该功能目前以 beta 形式面向 Claude Team 与 Enterprise 组织，可从 Claude Code CLI 和桌面端使用，页面可在任意浏览器查看。

来源：https://claude.com/blog/artifacts-in-claude-code

## PODCASTS

### AI & I by Every：The Founder of a $1.5B AI Company on What Comes After the First Wave of AI Apps

**核心结论：AI 应用第一波的功能优势很容易被复制，真正持久的机会是重做人与 AI 协作的工作界面。**

Granola 联合创始人兼 CEO Chris Pedregal 领导着一家估值 15 亿美元、团队已扩张到约 60 至 70 人的 AI 公司。他的反直觉观点是，公司高速增长并不会让创业变轻松：“Turns out they're really hard even when they're working as well.” 增长只是把生存战从寻找浪潮，变成站上浪头后努力不被甩下去。

对竞争，他并不把会议纪要视为最终价值。Notion、OpenAI 和 Zoom 推出类似能力后，Granola 的增长并未明显受影响，因为大家今天争夺的功能远小于下一阶段机会。更大的问题是：AI-native 世界里，人们究竟通过什么界面完成工作、组织上下文并与 agent 协作。Granola 因此把赌注放在会议周边上下文、proactive features，以及让用户自带 agent 的 API/MCP 路线上。

组织方法同样在变化。Dan Shipper 提出早期产品可由“pirate”快速探索价值，再由“architect”把有效原型变成可持续、可扩展的系统；Chris 则采用 shaping、validation、scaling 的阶段法，先探索多种解法，再用少量用户验证是否真的有用，最后才投入可靠性与规模化。两者都指向同一件事：AI 降低了构建成本，但团队仍必须把产品判断、架构边界和工作上下文设计清楚。

来源：https://www.youtube.com/playlist?list=PLuMcoKK9mKgHtW_o9h5sGO2vXrffKHwJL

Generated through the Follow Builders skill: https://github.com/zarazhangrui/follow-builders
