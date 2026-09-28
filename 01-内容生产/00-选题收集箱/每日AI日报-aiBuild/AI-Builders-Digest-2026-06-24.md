AI Builders Digest - 2026-06-24

X / TWITTER

Swyx（AI Engineer / Latent Space 相关）
Swyx 提出一个很有意思的判断：SpaceX 作为 NeoCloud + NeoLab 的组合，可能已经通过 Cursor 的 compute deal 收回了约一半投资。他认为，这种“领先模型实验室 + GPU NeoCloud”的组合非常有效，但前提是 GPU 供给规划足够稳，能覆盖内部训练顺利和不顺利两种情况。
来源：https://x.com/swyx/status/2069301071965741388

OpenAI Codex / ChatGPT 团队的 Thibault Sottiaux
Thibault Sottiaux 把重点放在 OpenAI 的安全方向更新：Codex Security、GPT-5.5-Cyber，以及“Patch The Planet”。他的表达很直接，这是一次面向 cyber defense acceleration 的发布，强调 Codex 不只是发现安全问题，还要帮助修复问题。
来源：https://x.com/thsottiaux/status/2069152290326630518

AI 教程作者 Peter Yang
Peter Yang 一边吐槽自己还没看懂 Claude Code 里的 dynamic workflow 到底是什么、什么时候该用，一边在找适合上播客的人，想聊如何用 Codex / Claude Code 做有趣的 pixel 或 Three.js 游戏。对 builder 来说，这两个点连在一起很有意思：大家已经不只关心“AI 能写代码吗”，而是在追问怎么组织长任务、怎么把 AI coding 变成可教学、可复用的创作流程。
来源：https://x.com/petergyang/status/2069267139576693028
来源：https://x.com/petergyang/status/2069118077313425840

Vercel CEO Guillermo Rauch
Guillermo Rauch 发布了两个和 AI builder 工具链直接相关的更新：Claude Design 可以“一键到 Vercel”，WebSocket 和 socket.io 也已经在 Vercel 上从 CDN 到 Fluid 获得支持。这两条都指向同一个趋势：AI 生成的界面、实时应用和部署链路正在被压缩成更短的闭环。
来源：https://x.com/rauchg/status/2069219190834127276
来源：https://x.com/rauchg/status/2069109057433035171

Box CEO Aaron Levie
Aaron Levie 认为，几乎所有 AI model 和 agent 进步都在 evals 下游：open weights 的领域 post-training、应用层 agent 改进、企业 agentic deployment，核心都取决于 evals。他还发布了 Box 对 HTML 内容的新支持：可以预览、编辑、管理版本并安全分享 HTML，这对 agent 生成内容的即时协作很实用。
来源：https://x.com/levie/status/2069228335255949775
来源：https://x.com/levie/status/2069140445205348432

Cursor 设计师 Ryo Lu
Ryo Lu 分享了他在 Cursor Compile 的 talk，主题是 AI 时代我们如何构建，以及什么不会改变。JSON 里没有 talk 正文，但从他的描述看，重点不是单个工具技巧，而是 builder 在 AI 环境里继续保留判断、设计和产品感。
来源：https://x.com/ryolu_/status/2069218497272717661
来源：https://x.com/ryolu_/status/2069218604449771989

Builder Zara Zhang
Zara Zhang 发布了一个 11 分钟 walkthrough，讲她的 Frontend Slides skill：如何用 Claude Code 创建漂亮的 HTML slides、她如何创建这个 skill、别人如何创建自己的 skill，以及如何插入图片 / 视频、发布、复盘经验。这个内容对想把“临时 prompt”沉淀成可复用 skill 的人很有价值。
来源：https://x.com/zarazhangrui/status/2069311440692072481
来源：https://x.com/zarazhangrui/status/2069311581985665385

Peter Steinberger（OpenClaw + OpenAI）
Peter Steinberger 转发并强调“Patch the Planet”。JSON 里只有这句短文本，没有更多上下文，但它和今天多条 Codex Security / GPT-5.5-Cyber 相关内容互相呼应：安全修复正在从“发现漏洞”走向“自动补丁”。
来源：https://x.com/steipete/status/2069132838356840857

Sam Altman
Sam Altman 明确说 OpenAI 想帮助所有公司变得更安全，并提到完整版 GPT-5.5-Cyber 在 CyberGym 上达到 state of the art。他同时把 Patch The Planet 和 Codex Security 放在一起，强调目标是解决安全问题，而不只是发现问题。
来源：https://x.com/sama/status/2069121360744550796

OFFICIAL BLOGS

今天 JSON 里没有新的官方博客内容。

PODCASTS

AI & I by Every: How Anthropic Uses Claude Fable 5 With Mike Krieger

The Takeaway：Mike Krieger 的核心观点不是“AI 让软件工程结束了”，而是软件生产的重心正在从手写代码转向意图表达、架构判断、任务委派和验证闭环。

Mike Krieger 是 Anthropic Labs 负责人、Instagram 联合创始人。他的经验特别有参考价值，因为他既经历过 Instagram 早期那种“几天通宵手写全栈产品”的时代，也在 Anthropic 内部深度使用 Fable 级别模型做真实构建。他说自己第一次用这类模型时，感觉像“total newbie”，因为旧的 prompt、任务拆解和交互节奏都过时了。

几个具体变化很值得记：第一，强模型更像能被委派长任务的 teammate，甚至能在远程服务挂掉时先搭 scaffold、记录问题、等服务恢复后继续修。第二，前期架构讨论变得更重要，因为模型能快速执行，团队反而更需要先对 intent 和系统边界达成一致。第三，成本不能只看单轮 token，而要看“把任务做到满意为止”的总成本；Fable 的优势在于少很多“不是这个意思，再改一下”的后续轮次。

他对软件工程的回答很清醒：“software engineering is different.” 不是结束，而是变成更接近 software production：人仍然要负责产品意图、ownership、生产事故、tradeoff、验证和最终 accountability。Krieger 特别强调 verification loop：每个 PR 最好带 screenshot 或 video，复杂 flow 要尽量用真实数据和 staging 环境跑起来，视频甚至能让 Claude 发现截图看不到的动画卡顿。

最有启发的是 dynamic workflow 的例子：他让模型把一个 Python 内部项目迁移成 TypeScript / Bun，workflow 会先深度理解、写 spec、逐模块翻译、增量测试、做 adversarial check，再列出没迁移的部分。这里的关键不是“模型更聪明”四个字，而是长任务需要可见、可复核、可分阶段执行的脚手架。

来源：https://www.youtube.com/playlist?list=PLuMcoKK9mKgHtW_o9h5sGO2vXrffKHwJL

Generated through the Follow Builders skill: https://github.com/zarazhangrui/follow-builders
