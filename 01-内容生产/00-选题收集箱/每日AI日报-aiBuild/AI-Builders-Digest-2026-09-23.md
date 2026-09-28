# AI Builders Digest - 2026-09-23

## X / TWITTER

### AI 教程作者 Peter Yang

Peter Yang 认为，以展示定向广告为核心的商业模式可能很快遭遇冲击：当 agent 代替人浏览网站并直接完成任务，人不再看到广告，原有的曝光和转化链路就会失效。这不只是流量入口变化，而是 agent 会把广告支持型互联网的底层经济模型一起改写。

原文：https://x.com/petergyang/status/2102215701255844074

他还分享了 ChatGPT Finances 的具体价值：系统能发现用户没注意到的异常扣款，并持续与客服交涉直至拿回退款。关键能力不是一次性回答，而是连接真实账户信息、监控后续回复并把跨多轮的事务执行到底。

原文：https://x.com/petergyang/status/2102186174911746151

### Vercel CEO Guillermo Rauch

Guillermo Rauch 宣布，Vercel AI Gateway 除了已有的 type-safe AI SDK API，现在也支持通过 HTTP 使用 Jev，为不走原生 SDK 的调用方式补上了接入路径。

原文：https://x.com/rauchg/status/2102205684544852121

他还用一个逆向分析运行中二进制文件的高难度任务测试了 Grok 4.7，认为它不仅成功解决问题，而且速度很快。这是一条基于实际复杂任务的模型能力信号，而不是泛泛的榜单评价。

原文：https://x.com/rauchg/status/2102089968860721335

### Box CEO Aaron Levie

Aaron Levie 判断，个人 agent 的商业化潜力会随着代理交易快速放大。用户会先把简单烦人的日常任务交给 agent，再逐步托管更复杂、金额更高的消费；当交易摩擦降低，总消费反而可能上升，因此机会既属于 agent 提供商，也属于为 agent 构建 commerce、本地服务和 B2B 服务接口的新平台。

原文：https://x.com/levie/status/2102253246807261579

他进一步预测，AI agent 使用软件的频率可能达到人的 100 倍。界面即使退到后台，CRM、ERP、数据平台、权限控制和业务编排仍会成为 agent 的关键基础设施；能提供安全护栏、可靠数据和工作流逻辑的平台，将获得新的增长窗口。

原文：https://x.com/levie/status/2102235949430354273

### Y Combinator CEO Garry Tan

Garry Tan 把 Capy 称为自己近期最喜欢的 agentic coding 工具之一，理由是它能跟踪多步骤工作流，并比单独使用 Codex 或 Claude Code 更快完成大型 PR。他展示的 GBrain 修复案例包含清晰的任务拆分、自动并行、GitHub PR 和 CI 流程，重点是把复杂修复波次组织成可检查的工程交付。

原文：https://x.com/garrytan/status/2102095924893827501

案例：https://x.com/garrytan/status/2102096495847551011

### FPV Ventures 合伙人 Nikunj Kothari

Nikunj Kothari 认为，Codex 配合 Computer Use 已经能把许多原本手工完成的工作流一次做完，但大众产品仍需要像 Instinct、Muse 那样做到零配置、尤其适配手机浏览器，才能真正降低 agent 的使用门槛。他对下一阶段产品的核心期待不是再展示能力，而是把能力讲清楚并让普通用户快速开始。

原文：https://x.com/nikunj/status/2102186665863463199

他也反对单纯追求 token 用量：那些炫耀 tokenmaxxing 的产品，体验往往更差。好产品依赖策展、修剪和明确约束，而不是把所有信息一股脑丢给 agent，期待模型自己整理出结果。

原文：https://x.com/nikunj/status/2102049065504739366

### OpenClaw 与 OpenAI 的 Peter Steinberger

Peter Steinberger 澄清，外界流传的“Meta 使用 OpenClaw”并不准确：Meta 是受到启发后构建了自己的 agent。他同时强调自托管 agent 的优势在于控制权仍在用户手里，外部平台无法轻易阻断你的使用。

澄清：https://x.com/steipete/status/2102116206371315854

自托管观点：https://x.com/steipete/status/2102044040397238286

## 官方博客

### Claude Blog：《Claude in Chrome is generally available》

Claude in Chrome 现已向所有 Claude 付费方案全面开放，并能在浏览器中自主执行部分操作，不再要求用户逐步批准。它可以沿用现有登录状态，读取页面、输入文字、点击链接、跨页面导航和填写表单，因此也能覆盖内部仪表盘、遗留系统和供应商门户等缺少原生连接器的工具。

真正值得关注的是它的安全架构。网页内容会先经过 prompt injection 探针检查，执行前再由分类器判断动作是否安全、是否与用户原始请求一致。文章把原则概括为：“操作在运行前会被验证。”在更强的专业红队攻击评测中，未加额外防护时 Opus 5 的攻击成功率为 3.8%；启用探针和自动批准安全分类器后，Sonnet 5 与 Opus 5 没有成功攻击，Fable 5 为 0.3%，且已人工确认均属低严重度场景。

实际限制也很明确：目前仅支持 Chrome，不支持其他 Chromium 浏览器和移动端；本地文件或其他桌面应用仍需 Claude desktop app。Enterprise 管理员可限制允许访问的域名。

原文：https://claude.com/blog/claude-in-chrome-generally-available

Generated through the Follow Builders skill: https://github.com/zarazhangrui/follow-builders
