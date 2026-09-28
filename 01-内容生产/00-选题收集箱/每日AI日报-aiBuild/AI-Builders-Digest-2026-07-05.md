AI Builders Digest - 2026-07-05

## X / TWITTER

### Swyx

Swyx 提了一个很尖锐的观察：过去十年 "tools for thought" 圈子做了很多漂亮的 canvas demo，但最后真正赢的，反而是低对比度、设计一般的 CLI，因为它们能直接替用户完成一部分“商品化思考”。这对 AI 工具创业者是个提醒：界面形态不一定是核心，替用户把认知劳动做掉才是核心。

来源：https://x.com/swyx/status/2073220591684096087

### Linear 产品负责人 Nan Yu

Nan Yu 关注的是“高质量训练数据”这个底层问题。他赞同一个判断：如果一个领域产不出好的训练数据，那这个领域本身可能就有很多虚假或低质量工作；同时他也认为，最佳医疗场景不是 AI 替代医生，而是医生真正花时间研究病例，并配备 LLM 来增强判断。

来源：https://x.com/thenanyu/status/2073070255031615877
来源：https://x.com/thenanyu/status/2073066919200956793

### Anthropic Claude Code / cowork 团队 Cat Wu

Cat Wu 给了一个实用提示：可以把 Claude Code 和 computer use 组合起来，让它根据 Claude Tag 文档，替团队连接 GitHub repo、data warehouse、Google Drive 和其他数据源。她也在征集大家用 Fable 5 做的 long weekend demo，说明 Anthropic 这波更关注“把模型接进真实工作流”的玩法。

来源：https://x.com/_catwu/status/2073149354412822738
来源：https://x.com/_catwu/status/2073147672106873001

### Anthropic Claude Code 团队 Thariq

Thariq 把重点放在“发现自己的 unknowns”。他的说法是，使用 Fable 最重要的部分，是先发现自己不知道什么，然后才能写出更好的 prompt；他还分享了用 HTML artifacts 帮助定位 unknowns 的例子，并提到这些内容来自他在 AIE talk 中打磨过的思路。

来源：https://x.com/trq212/status/2073101078145724589
来源：https://x.com/trq212/status/2073101079877943683
来源：https://x.com/trq212/status/2073101082428047681

### Replit CEO Amjad Masad

Amjad Masad 推了 Replit 上的视频生成能力，信号很直接：Replit 正在把更多多模态生成能力放进开发者工作流里，而不只是代码生成。

来源：https://x.com/amasad/status/2073003971287863717

### Vercel CEO Guillermo Rauch

Guillermo Rauch 认为 agentic self-improvement 的关键，是让 agent 能回看自己的历史运行，找出低效、错误和重复 tool call，然后产出新的 prompts 和 skills。他强调 Vercel 部署里的 agent observability 正是为了支持这种闭环：agent 不只是执行任务，还要能观察和改进自己的执行方式。

来源：https://x.com/rauchg/status/2073132174958841887

### Box CEO Aaron Levie

Aaron Levie 这条很值得看。他认为 AI 之战正在变成“上下文之战”：agent 的有效性取决于是否有正确的领域知识、上下文、工具接入，以及是否被嵌入到用户能审阅和接管的 workflow 中。真正有价值的 applied AI layer 不是 LLM wrapper，而是能治理关键知识、给 agent 提供更好上下文、在不同模型间路由任务，并在具体业务流程里完成 change management 的平台；他判断，能端到端解决具体业务问题的厂商会有最强 moat。

来源：https://x.com/levie/status/2073138135014502777

### Y Combinator CEO Garry Tan

Garry Tan 把 AI 和医疗等待时间放在一起看：专科医生等待时间正在变长，而 AI 可能会把 care quality 提升 100 倍。他没有展开技术方案，但这是一个清晰的应用方向判断：医疗系统的瓶颈越明显，AI 增强诊疗和分诊的价值越容易被看见。

来源：https://x.com/garrytan/status/2073053799791710301

### Builder Zara Zhang

Zara Zhang 的判断是：大家越来越不愿意为“工具”本身付费，因为如果只是工具，用户会觉得自己可以用 coding agents 搭一个。真正愿意付费的，是“雇到自己没有的 expertise”的感觉。她还分享了内容创作视角：每天发推不是任务，而是一种 lens；当你用这个镜头看一天和世界，想法会自然出现。

来源：https://x.com/zarazhangrui/status/2073295900395606401
来源：https://x.com/zarazhangrui/status/2073280650300596414

### FPV Ventures partner Nikunj Kothari

Nikunj Kothari 虽然批评 Gemini 的产品体验，但认为 Gemini 仍然是少数“一把 API key 做很多事”的平台：Flash 适合快速、便宜、长上下文结构化任务；Nano banana 做图像；还包括 search with grounding、realtime audio/video 等。他还观察到大模型实验室似乎喜欢在长周末前发布模型，让用户有时间折腾、被震撼，然后更深地陷入 token anxiety。

来源：https://x.com/nikunj/status/2073151491557478883
来源：https://x.com/nikunj/status/2073071325644816440

### Peter Steinberger

Peter Steinberger 给了一个很具体的设计工作流建议：如果你觉得 Codex 做设计不行，可以试试先让 imagegen 重新想象这个设计，再让 Codex 实现。这个思路本质上是把视觉探索和代码落地拆成两步，让图像模型先提供更强的视觉方向。

来源：https://x.com/steipete/status/2073277317464682723

### Every CEO Dan Shipper

Dan Shipper 关注 Fable 5 的实际使用和评测边界。他指出某个 benchmark 说法有误，模型本身相同，但更容易 fallback 到 Opus 4.8，所以测到的是 Fable 和 Opus 的混合结果。他也在推 Fable 5 prompt library，并用 token 成本举例说明：个人 iOS app 端到端 5M tokens，清掉产品 bug backlog 20M tokens，自动回复所有邮件/Slack/短信 30M tokens。

来源：https://x.com/danshipper/status/2073097796941484486
来源：https://x.com/danshipper/status/2073077325520838993
来源：https://x.com/danshipper/status/2073076447992746379

### Claude

Claude 官方分享了 Squidsoup，一个用声音、光和空间做沉浸式体验的艺术与设计团队，并提到他们在伦敦 Southbank Centre 与管弦乐队合作的大型现场项目。这里的重点不是模型参数，而是 AI 品牌继续向创意、艺术和体验设计场景扩展叙事。

来源：https://x.com/claudeai/status/2073028947478995406

## PODCASTS

### The MAD Podcast with Matt Turck: Why NVIDIA Is Giving Away AI Models | Bryan Catanzaro

核心 takeaway：NVIDIA 做开放模型不是慈善，也不只是 marketing，而是在为“更高效的 intelligence”下注，同时让整个生态更容易把 AI 接入真实行业。

Bryan Catanzaro 负责 NVIDIA 的 Nemotron 开放基础模型家族。他的核心判断是，如果行业已经在算力和能源上跑到极限，那么下一步提升 intelligence 的方式不是继续硬堆更多力气，而是提高效率。他在节目里说得很直白：“We can't get more intelligence by applying more force if we're already at the limit.” 这也是 Nemotron 的主线：speed first、agentic reasoning、开放生态。

这期最有价值的部分是 Nemotron 的技术拆解。Nemotron Ultra 和 Super 用 MVFP4 做了 4-bit pretraining，不只是部署时量化，而是在预训练阶段就用更低精度格式，这对数值稳定性要求很高；混合架构把 transformer 和 state space model 结合起来，用更低的 memory cache 压力提升长上下文效率；MoE 被视为 frontier AI 的默认路线之一，因为它在 intelligence 和 inference cost 之间更平衡；Latent MoE 通过压缩 token vector 降低 NVLink 通信量，在相同 inference cost 下换来更多 experts；multi-token prediction 则利用“读权重比算 token 更贵”的特点，一次预测多个 token，准确率越高，推理越快、越便宜。

另一个关键点是组织方式。Catanzaro 说 NVIDIA 不是单靠一个正式 org chart 推 Nemotron，而是 GPU、enterprise software、AI software 等多个团队共同参与，原则是 “mission is the boss”。multi-domain on-policy distillation 也不仅是技术方法，还是组织方法：十几个 domain teacher 分别把 science、math、coding、agent harness 等能力推到极致，再用密集监督训练一个 student，让不同团队的进展能合并进同一个模型，而不是互相拉扯。

来源：https://www.youtube.com/watch?v=Oojrfdl42LI

Generated through the Follow Builders skill: https://github.com/zarazhangrui/follow-builders
