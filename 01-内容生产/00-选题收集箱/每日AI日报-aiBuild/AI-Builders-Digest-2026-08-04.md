# AI Builders Digest：2026-08-04

## X / TWITTER

### Andrej Karpathy

Andrej Karpathy 继续扩展 Simon Willison 提出的「骑自行车的鹈鹕」测试。他把源码上传成可直接在浏览器运行、也可 fork 的版本，让这类生成式世界与游戏实验不只停留在演示视频，而是成为可复现、可改造的样例。

原帖：https://x.com/karpathy/status/2083948654377996480

### Swyx

AI Engineer、Latent Space 等项目相关的 Swyx 展示了 Codex computer use agent 代替他处理客服聊天的过程。agent 不仅主动要求升级处理，还在客服试图归责时给出完整证据链；在他看来，真正值得关注的是，对面的真人甚至没有意识到自己正在和 bot 交涉。

原帖：https://x.com/swyx/status/2084156733027701164

### Peter Yang

AI 实用教程创作者 Peter Yang 认为，Hermes 的关键优势是能为工作自动构建 skills，但自动积累也会制造「slop」。Nous Research 联合创始人 Karan Malhotra 给出的解法是 Hermes Curator：让后台任务定期清理 skills 与 memory，而且用户可以自定义什么算低质量内容，再让 agent 按这套标准重写自己的清理循环。

原帖：https://x.com/petergyang/status/2083968605432267139

### Thariq

Anthropic Claude Code 团队的 Thariq 认为，AI 在数学领域已经触发 Jevons paradox：工具让数学活动更多、更容易理解，也让数学家能把时间用于更高抽象层次的讨论。因此，AI 未必减少对数学人才的需求，反而可能提高对「会思考、懂数学的人」的需求，这与计算机进入国际象棋后的演化有相似之处。

原帖：https://x.com/trq212/status/2083977795290734975

### Replit CEO Amjad Masad

Replit CEO Amjad Masad 把自己的 LLM 国际象棋引擎接入 LiChess，让它自主与真人和 bot 对弈，当时 Elo 为 1253。它甚至能同时进行三盘比赛，用户可以直接在网站观看，说明这个实验已从离线 demo 进入真实、持续运行的环境。

原帖：https://x.com/amasad/status/2083926395403821427

补充：https://x.com/amasad/status/2083936067355635948

### Vercel CEO Guillermo Rauch

Vercel CEO Guillermo Rauch 介绍了驱动公司内部运营的 V agent：财务、沟通、文档、营销、工程和商业分析等日常工作都通过它完成，且它会为每位用户维护 memory、workflow 与 schedule。他强调，公司应完整控制 agent 的 source、runtime、data 与 token，而不是把公司的智能基础设施交给外部厂商。

V agent 同时充当统一入口和 router，把 sub-agent、skills 与其他网络 agent 收拢到一个「公司主域名」式体验中，只让少量专用 agent 保留独立入口。Rauch 也提醒，AI 并不会替代专业功底：真正拉开差距的是 mastery、creativity 与 AI 的组合。

原帖一：https://x.com/rauchg/status/2084042561690456157

原帖二：https://x.com/rauchg/status/2084060157085143512

原帖三：https://x.com/rauchg/status/2083969120270450911

### Box CEO Aaron Levie

Box CEO Aaron Levie 提出一个反直觉判断：世界上某些最难的工作，可能最先被自动化。数学、网络安全和编程虽然难，却有客观可验证的答案，既能给模型提供清晰 reward signal，也能规模化检验结果；法律、营销、销售和预算决策反而受情境、偏好与滞后反馈影响，没有唯一正确答案。

这意味着，模型能力增长之外，applied AI 层仍需重构流程、补齐上下文，甚至发明长期「测试」知识工作的全新机制。

原帖：https://x.com/levie/status/2083965372747882741

### Cursor 设计师 Ryo Lu

Cursor 设计师 Ryo Lu 回顾 Rdio、Mailbox 与 Apple 如何通过新交互模式，让软件变得更简单、更适合触摸。他把问题推向后 app 时代：当 app 逐渐退场，软件还有哪些部分会保持可见，以及未来的软件体验究竟应该「感觉」成什么样。

原帖：https://x.com/ryolu_/status/2083939454017053179

### Y Combinator CEO Garry Tan

Y Combinator CEO Garry Tan 对 AI 的核心判断是「增长是好事」：AI 会创造难以想象的经济增长，而人们的惊奇感却恰好在技术奇观呈指数上升时消失。他也把创业中的 meritocracy 解释为「领土比地图重要」，市场最终看的不是叙事，而是你是否真的做出了人们想要的东西。

原帖一：https://x.com/garrytan/status/2083957110711386439

原帖二：https://x.com/garrytan/status/2083923385193828612

原帖三：https://x.com/garrytan/status/2083920039208693996

### FPV Ventures 合伙人 Nikunj Kothari

FPV Ventures 合伙人 Nikunj Kothari 判断，早中期 VC 已经变成「vibes capital」：融资结果与基本面脱节，热门赛道即使没有实质进展也可能拿到夸张轮次，而看似稳妥的公司反而融不到钱。他预计 dry powder 与 AI tailwind 会让这种状态至少持续 12 至 18 个月；长期仍是盈利能力、干净 cap table 和自主掌控命运的公司胜出，但短期资本已成为超高竞争中的武器。

原帖：https://x.com/nikunj/status/2083873335998333227

### Every CEO Dan Shipper

Every CEO Dan Shipper 把 AI 接管原本需要人全程参与的任务称为「agency rupture」：人先感到自己的身份与价值被抹去，随后看见模型背后仍需要大量 human scaffolding，最终重建主体性，把 AI 当作默认且逐渐隐形的工具。能否把这种断裂消化成玩心与好奇心，可能是一个人是否适应 AI 经济的领先指标。

他进一步提出，技术不仅改变人能做什么，也会改变人认为自己「应该」做什么，因此 AI 会在重塑能力的同时重塑道德直觉。

原帖一：https://x.com/danshipper/status/2084038453831020916

原帖二：https://x.com/danshipper/status/2084024211539116466

## PODCASTS

### Training Data：《Building the Automated AGI Lab: Core Automation's Jerry Tworek and Rohan Anil》

**核心结论：** Core Automation 押注的不是把现有 Transformer 再放大一次，而是寻找能在部署中持续学习的新架构，并用高度自动化的实验室加速搜索。

Jerry Tworek 曾任 OpenAI VP，参与 Strawberry 与 reasoning 团队；Rohan Anil 曾是 Gemini pre-training 负责人，也在 Google Brain 与 Anthropic 从事基础研究。Tworek 的反思来自一线经验：大规模 RL 能持续推高 benchmark，却没有覆盖真实世界中混乱、变化且难以预先收集的任务分布。in-context learning 受 context 长度限制，持续 fine-tuning 又会遭遇 catastrophic forgetting，因此模型必须在 test time 真正学习，而不只是临时记住。

两人认为 Transformer 的问题还包括 computational depth 不足，以及 chain of thought 依靠逐 token 生成来换取更多计算，推理成本很高。Anil 主张把 pre-training、RL、optimizer、architecture、hardware kernel 当成端到端系统共同优化；一个理论更优却无法在 GPU 上高效运行的架构没有实际价值。

Tworek 直言：「强化学习不是从经验中学习的终点。」踢足球式的反复试错接近 RL，但理解数学依赖另一种更深层的内在连接，未来需要更丰富的学习算法。他对 AGI 的定义也更严格：模型必须能在没有人类介入的情况下改进自身。Core Automation 因而计划让 agent 扩大每位研究者的实验能力，从每天一个实验逐步走向十个、上百个，并以系统能否长期适应、能否在团队休假时仍产出更好结果作为现实检验。

原视频：https://www.youtube.com/watch?v=2RJiaf0SY8s

Generated through the Follow Builders skill: https://github.com/zarazhangrui/follow-builders
