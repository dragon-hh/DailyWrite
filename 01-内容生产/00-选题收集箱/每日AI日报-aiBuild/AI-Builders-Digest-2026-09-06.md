# AI Builders Digest — 2026-09-06

## X / TWITTER

### OpenAI Codex 与 ChatGPT 团队成员 Thibault Sottiaux

Thibault Sottiaux 认为，Astra 在尚未全面开放时就是团队最大的竞争优势之一。它带来的生产力提升，让部分原定明年年中的计划提前约 6 个月，改到 DevDay 发布；Astra 也已提前向用户推出，并为 Plus、Pro 和 Business 用户执行完整的 banked reset。

- https://x.com/thsottiaux/status/2096101429832552872
- https://x.com/thsottiaux/status/2096035437299237298

### AI 教程作者 Peter Yang

Peter Yang 提议 OpenAI 做一款 Apple Watch 应用，让用户直接向 Codex 任务语音输入，再用语音接收回复。这个设想的核心不是把手机界面搬到手表上，而是让 AI 工作流脱离屏幕，减少随身携带手机和沉迷屏幕的需要。

- https://x.com/petergyang/status/2096086845159563476

### Meta AI 高级总监 Madhu Guru

Madhu Guru 给 AI 产品建设者的周末练习很直接：挑一个自己熟悉的工作或生活流程，用 AI 从头到尾自动化。这个练习会迫使你定义真正优秀的端到端体验，决定 MCP 和工具怎么接、人应该留在哪些环节，并设计评估方法；他的判断是，完整做一次，比读一个月 AI 产品文章学得更多。

- https://x.com/realmadhuguru/status/2095907570540335174

### Replit CEO Amjad Masad

Amjad Masad 宣布 Astra 已进入 Replit，并用“奇点已经到来，只是分布不均”概括当前 AI 能力的落差。重点不是抽象预测，而是前沿模型能力正通过开发平台迅速进入普通构建流程。

- https://x.com/amasad/status/2095986658185453928
- https://x.com/amasad/status/2096022087035195647

### Vercel CEO Guillermo Rauch

Guillermo Rauch 看好 WebMCP，因为 agent 必须先适应现有 WWW 基础设施，而 WebMCP 能让网页直接暴露上下文相关的 agent 工具。例如 Next.js 开发页可以把当前标签页的调试能力直接交给 agent，不再要求开发者另找并配置 MCP server；他进一步判断，AI 软件工厂最终会产出更少缺陷、能够自我改进的软件。

- https://x.com/rauchg/status/2096065378598441431
- https://x.com/rauchg/status/2095926173293572467

### Y Combinator 总裁兼 CEO Garry Tan

Garry Tan 把 AsideAI 视为目前最顺手的 AI harness 与远程浏览器组合：他原本用 OpenClaw 接 Slack 花了约 2 小时，用 Aside 的集成、浏览器和默认访问控制不到 3 分钟就完成。GStack 也已把 Aside 浏览器设为首选远程会话浏览器，原因是它把网页访问、凭据、集成、harness 和 memory 放在同一套体验里。

- https://x.com/garrytan/status/2095971990645755941
- https://x.com/garrytan/status/2095948689823121872

### Builder Zara Zhang

Zara Zhang 提醒，很多人对 AI 写作能力的评价高于它的真实水平。这是一个值得内容团队警惕的判断：流畅不等于洞察，像人话也不等于真正理解。

- https://x.com/zarazhangrui/status/2096082116828406233

### SPC 合伙人、Bevel Health 联合创始人 Aditya Agarwal

Aditya Agarwal 描述了理解现代 AI 时的双重感受：理性上可以解释 RL、inference-time scaling 和数据验证循环，实际看到模型能力时仍会觉得像“巫术”。这恰好说明，理解机制与建立对能力边界的直觉，是两件不同的事。

- https://x.com/adityaag/status/2095910036652577028

### OpenAI 的 Sam Altman

Sam Altman 宣布 GPT-6 Astra 已在 Work/Codex 和 API 中面向 Pro、Enterprise 与 Business Premium 用户开放，随后也已覆盖全部 Plus 和 Business 用户。对开发者来说，关键信号是 Astra 已从分批 rollout 进入更广泛的实际构建阶段。

- https://x.com/sama/status/2095973658867171733
- https://x.com/sama/status/2096008528834244741

## OFFICIAL BLOGS

### Claude Blog

#### Claude in Chrome is generally available

Claude in Chrome 现已向所有付费 Claude 方案全面开放，并可在浏览器里自主执行部分操作，不再要求用户逐步批准。它能利用现有登录状态读取页面、输入文本、点击链接、跳转和填写表单，特别适合没有 connector 的内部仪表盘、旧系统和供应商门户。

真正重要的更新是安全机制。网页、邮件或表单可能暗藏 prompt injection，诱导 agent 执行用户没有要求的动作。Anthropic 通过持续扩充攻击样本、用 probes 扫描工具结果，以及在动作执行前用 classifier 对照原始请求，构成多层防线。文章给出的最新评估显示，在 probes 与自动批准安全分类器同时启用时，针对 Claude Sonnet 5 和 Opus 5 的攻击没有成功；Fable 5 的攻击成功率为 0.3%，且经人工核验均属于低严重度情境。

它的边界同样明确：目前只支持 Chrome，不支持其他 Chromium 浏览器或移动端；访问本机文件或其他桌面应用仍需 Claude desktop app。文章也强调，prompt injection 仍在持续演化，当前防护并不意味着风险已经消失。原文的核心提醒是：“Prompt injection remains a moving target.”

https://claude.com/blog/claude-in-chrome-generally-available

#### Claude gets its own browser in Cowork

Claude Cowork 在桌面应用中加入了独立的内置浏览器。任务需要访问网站时，浏览器会在侧边栏打开，Claude 可以浏览页面、读取内容、点击和输入；用户可以把报表研究、收集供应商发票或处理没有 connector 的门户交给它，同时继续做自己的工作。

这套内置浏览器与 Claude in Chrome 的定位不同。内置浏览器是 Claude 自己的隔离环境，默认看不到用户的标签页、书签和密码；用户可按站点从 Chrome、Edge 或 Firefox 导入登录状态，银行、邮箱和 SSO 站点默认不包含。Claude in Chrome 则更适合处理用户已经打开、已经登录的页面。文章用一句话概括这种边界：“It’s Claude’s browser, not yours.”

该功能正向 Claude desktop app 的 Pro、Max 和 Team 方案分批推出，Enterprise 管理员已经可以启用。它沿用 Claude in Chrome 的 prompt injection 防护与动作校验，但 Anthropic 明确表示风险无法完全消除，建议先从可信网站开始使用。即使用户在网页或手机端发起任务，只要桌面应用保持在线，也能驱动该内置浏览器。

https://claude.com/blog/cowork-built-in-browser

Generated through the Follow Builders skill: https://github.com/zarazhangrui/follow-builders
