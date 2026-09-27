# AI Builders Digest — 2026-09-26

## X / TWITTER

### Swyx（Latent Space、AI Engineer 等项目）

Swyx 把自己的内容策略概括为“Scaling without Slop”：不是靠批量低质内容换增长，而是在保持质量的前提下扩大产出。他说团队花了 3 年才把 YouTube 做到第一个 10 万订阅，但从 10 万到 20 万只用了 1.2 个月，AEO、SEO 和订阅增长也出现了类似加速；这将成为 Latent Space、AINews 及其团队下一阶段内容业务的起点。

原帖：https://x.com/swyx/status/2103361254433993165

### Google、Google Labs、Gemini App、Google AI Studio VP Josh Woodward

Josh Woodward 介绍了 Google Labs 的新实验 Dreambeans。它每天提供固定数量的“beans”，目的不是让人继续盯着屏幕，而是把用户引向现实世界，帮助他们和真实的人一起参与自己关心的活动。这是一个少见的产品取向：AI 不只是增加线上停留时长，也可以主动把注意力送回线下关系与行动。

原帖：https://x.com/joshwoodward/status/2103182635992514569

### Anthropic Claude Code 团队成员 Thariq

Thariq 根据用户反馈重新设计 Claude Code 的 plan mode：有人本来就会自己规划，不需要单独模式；也有人喜欢进入一个只思考、只头脑风暴的状态。他计划把 plan mode 做成内置 mod，并允许 mod 新增模式、覆盖 Shift+Tab，甚至让用户重新绑定这个快捷键。重点不只是增加一个设置，而是把工作模式本身开放成可定制、可分享的扩展层。

原帖：https://x.com/trq212/status/2103212051065921632

补充：https://x.com/trq212/status/2103212052391354794

### Replit CEO Amjad Masad

Amjad Masad 宣布 Muse 现在可以直接在 Replit 上创建应用。信息很短，但产品含义明确：Muse 的创作能力开始接入一个可运行、可继续开发和部署的应用环境，降低从生成想法到实际产品的转换成本。

原帖：https://x.com/amasad/status/2103129037011120525

### Vercel CEO Guillermo Rauch

Guillermo Rauch 公布了 Vercel AI Gateway 最近两个月的真实用量变化。Anthropic 的支出占比仍居第一，但从 69% 降至 40%；OpenAI 从 10% 升至 24%，并在 token 数量上领先，GPT-6 Astra 与 GPT-5.6 Sol 增长强劲。Anthropic 流失份额约有一半被 Kimi K3 和 DeepSeek 拿走，而 Opus 5.5 上线两天已占到 10% 支出；图像生成中 OpenAI 占 62%。这组数据说明，多模型路由正在让企业用量快速分散，模型竞争已经具体反映在生产支出里。

原帖：https://x.com/rauchg/status/2103216656747262419

### FirstMark VC Matt Turck

Matt Turck 把注意力放在 Jensen Huang 所说 AI 五层蛋糕中最容易被忽视的软件基础设施层。VAST Data 已成长为一家估值 300 亿美元、服务 SpaceX AI、CoreWeave、Nebius、Mistral AI 等公司的基础设施企业；它处理的不只是存储，还包括推理与 fine-tuning 的不同负载、trillion-scale vector、KV cache、RAG、agent memory、身份权限和机密计算。最实用的判断是，AI 工厂白天做 inference、夜间做 fine-tuning 后，数据层必须支持持续共享与流动，旧数据库和传统云架构未必能承受这种工作方式。

原帖：https://x.com/mattturck/status/2103167531917721866

### FPV Ventures Partner Nikunj Kothari

Nikunj Kothari 分享了一个针对小企业软件的判断：未来每个小企业，尤其是 trades 行业，都可能拥有量身定制的软件。真正的差异化并不一定发生在通用模型或底层平台，而是在最后一公里，企业如何为客户与员工设计独特体验。AI 降低定制软件成本后，小企业也可能从购买标准 SaaS 转向拥有自己的业务系统。

原帖：https://x.com/nikunj/status/2103360292973633770

### OpenClaw、OpenAI 的 Peter Steinberger

Peter Steinberger 给出了一个很具体的 agent 使用技巧：如果只让 agent“清理代码”，它通常会过早停止；更有效的做法是给出有力度、可验证的目标，例如“删除 20% 最无用的测试，同时让代码覆盖率变化保持在 2% 以内”。他还用 Daybreak 检查开源依赖，发现了 8 个长期存在的内存泄漏，提醒开发者别只维护自己的代码，也要持续审视依赖链。

原帖：https://x.com/steipete/status/2103148444701610233

补充：https://x.com/steipete/status/2103200311641076100

## 官方博客

### Claude Blog

#### Claude for Small Business launches new workflows, integrations, and training programs

Claude for Small Business 新增 43 个 workflows 和 27 个 integrations，覆盖 Shopify、Salesforce、TikTok、Atlassian、Zoom、Xero、Gusto、Square、Stripe、Zapier 等小企业常用工具。产品重点也从自动化后台运营扩展到业务增长，包括线索生成、回复咨询、撰写提案和日常经营报告。自 5 月发布以来，这套方案已安装超过 90 万次；Anthropic 还计划在美国 10 个城市举办免费工作坊，150 多家认证培训机构将在社区中开展 750 多场活动，14 家集成伙伴也会提供免费 webinar。

真正值得关注的是工作流开始直接连接收入与经营节奏。一位餐饮创业者说：“过去一个半月，我用 Claude 制作专业提案赚了 2 万美元。”另一家企业让 Claude 每天早上 6 点读取 CRM、汇总待办并发送优先级简报。对小企业来说，实用路径不是先设计宏大的 AI 转型，而是连接现有工具，从每周经营简报、夜间线索响应、语音生成报价单、营销审核和月末对账这些高频任务开始。

原文：https://claude.com/blog/claude-for-small-business-launches-new-workflows-integrations-and-training-programs

Generated through the Follow Builders skill: https://github.com/zarazhangrui/follow-builders
