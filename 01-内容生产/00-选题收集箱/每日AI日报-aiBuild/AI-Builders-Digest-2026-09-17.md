# AI Builders Digest — 2026-09-17

## X / TWITTER

### Google VP Josh Woodward

Josh Woodward 介绍了 Gemini Notebook 面向学生的新功能：用户可以用约 100 种语言，围绕课堂材料进行实时语音问答；也可以随手录下讲座和笔记，音频会自动保存到指定 notebook。大学生目前还可在 140 多个国家和地区免费获得 Google AI Plan，以取得更高额度并使用更多 Google 产品。

https://x.com/joshwoodward/status/2099921866014306633

### AI 教程创作者 Peter Yang

Peter Yang 从一批真实需求中总结了 bot 最适合接手的工作：找潜在客户、写外联邮件、把成果整理成案例，监控广告账户与注册或支付流程，跟踪 Jira 阻塞，分流客服工单，以及持续测试酒店预订链路。研究和内容侧也出现了很具体的用法，例如监控 AI builders、核验来源并转成脚本，或把信息噪音整理成每日简报。

https://x.com/petergyang/status/2100027487681953834

他给 solopreneur 的建议不是一味追求收入最大化，而是先设计一种能让自己长期做喜欢之事的业务；枯燥工作交给 bot，或者干脆不做，否则独立创业就失去了意义。

https://x.com/petergyang/status/2099968897323778416

### Anthropic Claude Code 团队 Thariq

Thariq 的判断很直接：多数集成场景里，MCP 已经比 CLI 更合适。原因是模型的 tool calling 能力明显提升，工具可以延迟加载，而 MCP 现在又可以保持无状态；如果仍需组合或过滤数据，可以把 `query` 一类参数直接设计进 MCP tool。

https://x.com/trq212/status/2099958388230873165

### Replit CEO Amjad Masad

Amjad Masad 对一个已知输出域的方案提出更简单的技术路径：既然候选集合预先确定，为什么不直接训练模型，对枚举值输出 logprobs？这把问题从生成自然语言，改写为在有限答案空间内做概率判断，可能更直接也更高效。

https://x.com/amasad/status/2100056178705514703

### Vercel CEO Guillermo Rauch

Guillermo Rauch 看好 WebAssembly 在未来 Web 中的作用。Safari 27 已支持 JSPI，这项能力让同步原生代码可以挂起并等待异步 Promise；随着更多代码转向原生形态，浏览器内的 Wasm 与原生 fetch stack 会越来越重要。

https://x.com/rauchg/status/2099974859023683975

Vercel 同时正式推出 Vercel Labs，作为公开研究与实验阵地。相关项目累计已有 2.47 亿次下载，团队会公开正在支持和研究的方向，也会分享没有奏效的实验。

https://x.com/rauchg/status/2099911447598059812

他还明确主张未来属于 multi-model：隐藏模型选择反而会让用户困惑，也剥夺了用户利用模型竞争红利、为不同任务选择最佳工具的机会。

https://x.com/rauchg/status/2099905740505055680

### Box CEO Aaron Levie

Aaron Levie 认为，模型能力与企业真正想自动化的 workflow 之间仍有巨大鸿沟，而这正是 applied AI layer 的机会。企业需要把智能接进流程，重构作业方式，聚合正确上下文，引入 human-in-the-loop，并处理 change management、领域 eval、安全和治理；模型越强，可处理的任务越复杂，这一层反而越重要。

https://x.com/levie/status/2099976021311398230

### Y Combinator CEO Garry Tan

Garry Tan 分享了一个直接的效率对比：他用 Capy.ai 配合 GStack/GBrain 处理积压 issue 和 PR 的修复批次，在使用同样 frontier models 的情况下，把原本需要一天的 Codex/Claude Code 工作压缩到约半天。真正的增益来自更好的工作流编排，而不只是更换底层模型。

https://x.com/garrytan/status/2099964487667454097

### FPV Ventures 合伙人 Nikunj Kothari

Nikunj Kothari 提醒创始人，不要把下一轮融资当成必然事件。资本是加速武器，不该成为企业生存的唯一条件；团队应先找出无需新增资本也能活下去并形成良性循环的默认路径，再分别推演资本充裕与紧缩时业务会怎样变化，因为未来 6 到 18 个月的资本市场无法预知。

https://x.com/nikunj/status/2100008917980102863

### Every CEO Dan Shipper

Dan Shipper 透露 Every 测试了一种不直接生成文字、而是输出概率的模型约一周。他认为这类模型特别适合充当 judge：在原本需要 Fable 级模型的判断任务中，其内部测试速度快 25 倍，价格低 600 倍，并可能在 6 到 12 个月内成为不可或缺的基础能力。

https://x.com/danshipper/status/2099947471518474522

### SPC General Partner Aditya Agarwal

Aditya Agarwal 用 Profound 的成长说明，早期投资有时先看到的不是点子，而是创始人组合。两位背景截然不同的创始人在 SPC 相识，先形成合作关系，之后才长出公司；如今 Profound 估值 18 亿美元，被三分之一的 Fortune 100 使用，并完成了 1.8 亿美元 Series D，成为增长最快的 AI marketing platform。

https://x.com/adityaag/status/2099939685657141257

### Claude

Salesforce in Claude 已开放 beta，把 accounts、opportunities 和 pipeline 带进 Claude，并提供 37 个预置 sales skills。销售人员可以在对话里准备客户电话、审查交易、创建 pipeline dashboard 或发送 forecast，无需离开当前工作界面。

https://x.com/claudeai/status/2099876514330206578

## 官方博客

### Claude Blog

#### Claude for Small Business launches new workflows, integrations, and training programs

Claude for Small Business 现在提供 43 个 workflows，并新增 27 项 integrations，覆盖 Shopify、Salesforce、TikTok、Atlassian、Zoom、Xero、Gusto、Square、Stripe 和 Zapier 等小企业常用工具。产品从处理后台事务进一步延伸到增长场景，包括筛选并回复 inbound leads、生成报价方案、整理日常经营报告；自 5 月推出以来，安装量已超过 90 万次。

这次升级直接来自超过 1,000 位、分布在 10 座城市的小企业主反馈。Anthropic 还将在秋季于 10 座美国城市举办免费 workshop，并由 150 多家认证培训机构在各自社区开展 750 多场培训。实际用户给出的效率变化很具体：“What used to take me 120 hours now takes me five minutes.” 对小企业而言，关键价值不是多一个聊天窗口，而是把 CRM、财务、营销和销售工具连接起来，形成能直接运行的业务流程。

https://claude.com/blog/claude-for-small-business-launches-new-workflows-integrations-and-training-programs

Generated through the Follow Builders skill: https://github.com/zarazhangrui/follow-builders
