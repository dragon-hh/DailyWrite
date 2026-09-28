# AI Builders Digest — 2026-07-26

## X / TWITTER

### Swyx

AI 工程师与社区建设者 Swyx 为 SmolForge 增加了 4 项新功能，其中包括可自定义皮肤和 spritesheet 动画。他同时透露，自己正在做一套新的 G Suite，直接动机是现有办公软件中那些让人恼火的默认设置。

- [SmolForge 新功能](https://x.com/swyx/status/2080750437133901925)
- [新 G Suite 的动机](https://x.com/swyx/status/2080705334587605122)

### Google VP Josh Woodward

Google VP Josh Woodward 展示了 Gemini 从聊天工具转向执行工具的具体用法：把学校日历 PDF 丢进去，让它自动把所有“不上课”的日期写入 Google Calendar。Gemini Spark 已面向美国 Google AI Pro 订阅用户开放，接下来会扩展到全球。

- [Gemini Spark 日历用例](https://x.com/joshwoodward/status/2080771183944073347)

### Anthropic Claude Code 团队 Boris Cherny

Anthropic Claude Code 团队的 Boris Cherny 认为，Opus 5 最值得关注的不只是编码、数据分析或知识工作能力，而是它成为 Anthropic 迄今最难被 prompt injection 成功攻击的模型。模型对齐、注入探针与 Claude Code Auto Mode 叠加后，他们观察到 prompt injection 攻击成功率降至接近 0。

- [Opus 5 的 prompt injection 防护](https://x.com/bcherny/status/2080713091688583312)

### OpenAI Codex 与 ChatGPT 团队 Thibault Sottiaux

OpenAI Codex 与 ChatGPT 团队的 Thibault Sottiaux 宣布，ChatGPT Work 已向全球所有付费方案开放，并覆盖移动端、网页端和桌面端。他把这项能力形容为给 ChatGPT 装上了“喷气背包”，重点显然是让 ChatGPT 从回答问题进一步走向完成工作。

- [ChatGPT Work 全球开放](https://x.com/thsottiaux/status/2080876712439747052)

### AI 教程作者 Peter Yang

AI 教程作者 Peter Yang 分享了一种更自然的 Codex 工作方式：躺着通过 ChatGPT Voice 口述任务，但前提是能记住各个长期运行任务的名称。商业层面，他判断独立开发者越来越难只靠纯软件变现，软件往往还要叠加服务或其他价值层。

- [用 ChatGPT Voice 驱动 Codex](https://x.com/petergyang/status/2080793867960643823)
- [独立开发者的纯软件变现难题](https://x.com/petergyang/status/2080669643577176573)

### Meta AI 高级总监 Madhu Guru

Meta AI 高级总监 Madhu Guru 认为，未来几年的巨大机会属于那些能把混乱现实工作流改造成 foundation model 可执行系统的人。真正的门槛不是简单接入模型，而是理解业务、设计 eval、通过 post-training 改进模型，并建立持续反馈闭环，让通用模型在特定领域变得出色。

- [把 foundation model 适配现实工作流](https://x.com/realmadhuguru/status/2080707454422413487)

### Anthropic Claude Code 与 Cowork 团队 Cat Wu

Anthropic Claude Code 与 Cowork 团队的 Cat Wu 强调，Claude Opus 5 的突出能力是长时间自主工作。这意味着模型升级的价值不只在单次回答质量，还在于能否稳定推进更长、更完整的 agent 任务。

- [Opus 5 的长时自主工作能力](https://x.com/_catwu/status/2080707593115516985)

### Anthropic Claude Code 团队 Thariq

Anthropic Claude Code 团队的 Thariq 透露，面向最新模型时，他们删掉了约 80% 的 Claude Code system prompt，并据此重新总结 system prompt、skills 与 Claude.md 的写法。他还把 Opus 5 定位为适合日常使用的模型，建议搭配 Fable 做规划、头脑风暴或处理最难修的 bug。

- [Claude Code system prompt 缩减约 80%](https://x.com/trq212/status/2080710971228918066)
- [Opus 5 的日常使用定位](https://x.com/trq212/status/2080703339306913985)

### Replit CEO Amjad Masad

Replit CEO Amjad Masad 再次把 open weight 模型政策推到台前，公开追问 Anthropic 是否支持禁止 open weight 模型，并要求其明确立场。他也提到早期 VC 曾普遍错过 AI 芯片公司 Etched，认为如今资本终于重新认识到这类基础设施公司的价值。

- [追问 Anthropic 的 open weight 立场](https://x.com/amasad/status/2080850075358826871)
- [Etched 的早期融资判断](https://x.com/amasad/status/2080864869130416320)

### Anthropic 研究员 Alex Albert

Anthropic 研究员 Alex Albert 表示，Opus 5 已能生成接近超人水平、达到咨询顾问成品质量的 spreadsheet 和 slide deck，而这一进展只用了约半年。他特别强调团队在提高智能水平的同时改善了跨领域 token 效率，并称自己在许多编码任务中更偏好 Opus 5 而不是 Fable 5。

- [Opus 5 的 spreadsheet 与 slide deck 能力](https://x.com/alexalbert__/status/2080731979528679617)
- [Opus 5 的 token 效率与编码体验](https://x.com/alexalbert__/status/2080703118086693121)

### Box CEO Aaron Levie

Box CEO Aaron Levie 主张美国继续推动 open weight 创新，因为它能扩大 AI 在经济中的扩散、降低部分工作负载成本，并支持针对垂直领域的 post-training，而 open 与 closed 并不是零和竞争。Box 在真实企业文档任务中测试 Opus 5 后，相比 Opus 4.8 观察到尽调提升 17%、生命科学提升 30%、法律提升 12%、技术提升 19%、医疗提升 13%。他的结论是，Opus 5 在复杂非结构化数据上的推理、分析和多步处理能力明显增强，并将很快进入 Box AI Studio。

- [继续推动 open weight 创新](https://x.com/levie/status/2080761484305654091)
- [Box 对 Opus 5 的企业任务评测](https://x.com/levie/status/2080704871934931221)
- [Box 签署 open weight 支持信](https://x.com/levie/status/2080675210991443982)

### Y Combinator President & CEO Garry Tan

Y Combinator President & CEO Garry Tan 引用一项长期判断：过去 200 年中，一个国家采用新技术的速度，至少能解释当今国家贫富差异的 25%。他同时提醒，AI 要转化为宏观生产率，管理者必须批准完全不同的人员配置和工作流方案，而这个组织变革周期更可能是 10 年，不是 2 年。

- [技术采用速度与国家财富](https://x.com/garrytan/status/2080849953413541982)
- [AI 宏观生产率需要组织重构](https://x.com/garrytan/status/2080699367883980924)

### FirstMark VC Matt Turck

FirstMark VC Matt Turck 指出一个少被讨论的讽刺：顶尖 AI 研究者正在用 recursive auto-research 研究出替代自身工作的系统。与此同时，model routing 正迅速成为基础设施热点，Stripe 被传以 100 亿美元收购 OpenRouter，Cursor 与 Runway 也先后发布 Router，Databricks、Vercel、Cloudflare、AWS 和 Google 等公司都在布局这一层。

- [recursive auto-research 的职业悖论](https://x.com/mattturck/status/2080738638065729741)
- [model routing 赛道升温](https://x.com/mattturck/status/2080645582209663049)

### Builder Zara Zhang

Builder Zara Zhang 认为，当前模型最需要改善的不是智能，而是速度：等待 1 至 5 分钟既不足以进入深度工作，又长到足以让人分心刷信息流。她还提出，把 agent 带进群聊和会议后，聊天记录与会议转录本身就能成为 PRD，这会让口头表达者获得过去偏向书面表达者的工作优势。

- [模型当前最需要的是速度](https://x.com/zarazhangrui/status/2080829737044439444)
- [群聊和会议转录成为 PRD](https://x.com/zarazhangrui/status/2080617484261249160)

### OpenClaw 与 OpenAI 的 Peter Steinberger

OpenClaw 与 OpenAI 的 Peter Steinberger 披露，其 autoreview skill 在一次棘手重构中创下 66 轮审查的新纪录。这个案例显示，代码 agent 的价值正从一次性生成转向能在复杂改动中持续复查和迭代的长循环。

- [autoreview skill 完成 66 轮审查](https://x.com/steipete/status/2080899298838098034)

### Every CEO Dan Shipper

Every CEO Dan Shipper 对 Opus 5 的评价很反直觉：沿用旧 skills 和 workflow 时，它会争辩、提前停止，甚至破坏向后兼容；删掉旧工作流、从零开始后，表现反而显著改善。他们还发现 medium 或 low thinking 比更高思考强度更稳定，因此 Opus 5 不是无缝替换旧模型，而是需要重新设计工作方式的模型。

- [Opus 5 Day 0 实测](https://x.com/danshipper/status/2080700057892815114)

### Sam Altman

Sam Altman 表态，希望美国在 open source 与 proprietary 两条 AI 路线上同时取胜。这一立场把竞争重点从二选一转向双轨并进，让开放模型扩散与闭源前沿能力都成为国家 AI 竞争力的一部分。

- [同时支持 open source 与 proprietary AI](https://x.com/sama/status/2080683363174945065)

### Anthropic Claude

Anthropic 宣布 Opus 5 已向所有付费方案和 Claude API 开放，价格与 Opus 4.8 相同，并提供约为默认速度 2.5 倍的 Fast mode。安全方面，Opus 5 在网络安全任务上强于 Opus 4.8，但开发 exploit 的能力仍明显落后于 Mythos 5；自动行为审计则显示，它是 Anthropic 迄今对齐程度最高、鲁莽或欺骗行为比例最低的模型。

- [Opus 5 的可用范围、价格与 Fast mode](https://x.com/claudeai/status/2080699515271528827)
- [Opus 5 的网络安全能力边界](https://x.com/claudeai/status/2080699512205537648)
- [Opus 5 的自动行为审计](https://x.com/claudeai/status/2080699508401328462)

## OFFICIAL BLOGS

### Anthropic Engineering

#### How we contain Claude across products

Anthropic Engineering 给出的核心结论是：“先在环境层设计遏制机制，再在模型层引导行为。”不同用户的监督能力决定了不同产品的隔离方式：claude.ai 使用服务端临时容器，Claude Code 依赖开发者可理解的 human-in-the-loop 与 OS sandbox，Claude Cowork 则把代码执行放进封闭 VM。

这些边界不是理论设计。Claude Code 引入 Seatbelt 和 bubblewrap 后，权限提示减少了 84%；一次内部钓鱼测试中，恶意提示在 25 次尝试里成功外传凭据 24 次，证明当攻击指令由用户主动粘贴时，模型分类器无法替代文件系统与网络出口限制。Cowork 也曾允许恶意文件借受信任的 Anthropic API 域名上传数据，最终通过 VM 内的中间人代理，只放行 VM 自己的 session token。

对 agent 产品建设者最实用的提醒是：信任边界必须建立在读取项目配置之前；域名 allowlist 应被视为能力授权，而不是简单目的地过滤；symlink 要在路径校验前解析；远程 MCP 和 connector 的行为可能随时变化；多 agent 系统还要警惕子 agent 输出被错误提升为高信任内容。标准化 hypervisor、syscall filter 和 container runtime 往往比自研安全组件更可靠。

[阅读原文](https://www.anthropic.com/engineering/how-we-contain-claude)

## PODCASTS

### No Priors

#### Building an Autonomous Delivery Experience with DoorDash Co-Founders Andy Fang and Stanley Tang

**核心结论：DoorDash 的真正壁垒不是造出一台机器人，而是用真实配送网络把 AI、机器人、无人机和人类配送员编排成一个可规模化的本地商业系统。**

DoorDash 联合创始人 Andy Fang 与 Stanley Tang 展示了 agentic commerce 已经如何改变消费行为。Ask DoorDash 的餐厅搜索中，有 50% 的使用路径最终下单于用户从未购买过的餐厅；在杂货场景中，用冰箱照片、饮食限制或菜单计划发起自然语言购物后，客单 basket size 提高约 40%。这说明对话界面不只是减少点击，还释放了传统关键词搜索没有承接的需求。

机器人路线更能说明他们的方法论。DoorDash 从 2018 年开始小规模试验，先与 sidewalk robot 和 robotaxi 公司合作，最后发现两端都不适合平均 3 至 5 英里、约 15 分钟的配送。Stanley Tang 的原则是：“不要先设计一个解决所有问题的东西。”团队因此自研 DOT，一台重 300 磅、最高时速 20 英里、车身体积约为汽车十分之一的 L4 自动配送机器人，可行驶于人行道、自行车道和道路，目前已在 Phoenix 运行近两年。

更关键的是 autonomous delivery platform，它负责 API、dispatch、商家接入、消费者体验，以及“最初和最后 100 英尺”这类地图没有的数据。DoorDash 可以让 DOT 服务密集郊区，让无人机承担轻量偏远订单，让人类 Dasher 处理需要上下楼或多步骤拣货的复杂订单。其 100 亿次历史配送、每月超过 4000 万消费者和真实异常处理经验，构成了别人难以复制的数据闭环。Stanley 甚至预测，随着业务以约 25% 的年速度增长，十年后 Dasher 数量可能不降反升，因为自动化扩大的首先是整个配送市场。

[观看原视频](https://www.youtube.com/watch?v=vNpcg_Ma-FA)

Generated through the Follow Builders skill: https://github.com/zarazhangrui/follow-builders
