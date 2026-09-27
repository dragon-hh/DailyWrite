# AI Builders Digest — 2026-08-03

## X / TWITTER

### Andrej Karpathy

Andrej Karpathy 认为，LLM 的测试正在从简单生成任务走向长时间、超定制的世界构建。他让 Opus 5 用约 100 万 token 和两小时生成 5500 行 three.js 代码，把《The Lord of the Rings》开篇做成程序化场景，这类过去没人愿意投入时间的定制内容，正因为 AI 的耐心和低成本而变得可行。但游戏也暴露了模型的短板：它无法高效、原生地观看视频或亲自游玩来审查结果，只能靠缓慢截图纠错。[原始推文](https://x.com/karpathy/status/2083749667410727319)

### Swyx

Swyx 关注的不是如何消灭 AI 生成的劣质代码，而是如何从语言和运行机制上重新设计软件，让系统能够容忍它。他认为，对 AI-native 编程语言来说，“容忍 slop”比“反对 slop”重要 100 倍，因为代码生成已成现实，真正的工程机会是让运行环境能接住不完美的产物。[原始推文](https://x.com/swyx/status/2083753582160191988)

### Peter Yang

AI 教程与访谈创作者 Peter Yang 认为，Opus 4.6 的人格感和写作风格优于 Opus 5。他的具体批评是，Opus 5 回复过长、频繁使用模式化的 Claude 表达，而且判断性更强，导致过去像可信朋友一样的交流体验变差。[原始推文](https://x.com/petergyang/status/2083755374994415904)

### Linear 产品负责人 Nan Yu

Linear 产品负责人 Nan Yu 提出一种减少开源“垃圾 PR”的机制：提 issue 的人先写清规格并质押 token，维护者接受后，由 GitHub 把原始 issue 交给云端 coding agent，成本由请求者承担。[原始推文](https://x.com/thenanyu/status/2083722999430050281)

她还描述了更连续的 agent 工作循环：agent 遇阻时在 issue 留下评论并附上全部上下文，人类补充信息后，agent 直接从原状态继续，而不是重新启动任务。[原始推文](https://x.com/thenanyu/status/2083534333428580501)

### Anthropic 哲学家与伦理学家 Amanda Askell

Anthropic 哲学家与伦理学家 Amanda Askell 用一句反讽回应“deep learning 撞墙论”：不要苛责这样想的人，因为每个人都需要一点希望。[原始推文](https://x.com/AmandaAskell/status/2083713770065637511)

她也批评一种精英自保式未来观：如果真相信社会会分成少数长生者和庞大底层，那么“只要我属于上层就行”并不值得赞许。她关注的不是如何让自己逃离“永久底层”，而是这种底层是否会被制造出来。[原始推文](https://x.com/AmandaAskell/status/2083649115901337644)

### Vercel CEO Guillermo Rauch

Vercel CEO Guillermo Rauch 分享了一款基于 Next.js 构建的开源 agentic CRM。它不绑定模型，既能自托管也能 serverless 部署，同时支持多渠道和 headless 架构，体现了 agent 应用基础设施向开放、可组合方向发展的路线。[原始推文](https://x.com/rauchg/status/2083684679362965605)

### Box CEO Aaron Levie

Box CEO Aaron Levie 预测，AI 在个人日常效率与数学、科学、法律、编程等深领域的进展将越来越分化。消费需求存在较容易满足的上限，而专业领域对能力几乎没有天然天花板，因此能力会先快速增长，再等待数据集和真实 workflow 把它转化为生命科学、自动化与网络能力上的突破。[原始推文](https://x.com/levie/status/2083589132660711452)

### Y Combinator 总裁兼 CEO Garry Tan

Y Combinator 总裁兼 CEO Garry Tan 观察到 2026 年一个明显转向：OpenAI 正在表现得更像开放平台。他区分了两条路线，一条把 intelligence 当作随取随用的公共能力，另一条则暗示必须一路向上做完整全栈整合；他认为 OpenAI 正向前者移动。[原始推文](https://x.com/garrytan/status/2083684825333105107)

### FPV Ventures 合伙人 Nikunj Kothari

FPV Ventures 合伙人 Nikunj Kothari 指出一个强烈反差：模型已开始解决 NP-hard 问题，传统企业却仍在纠结 token 投入的 ROI。他判断，未来几十年的主要工作不是继续证明模型能力，而是让这些能力真正扩散进企业和现实流程。[原始推文](https://x.com/nikunj/status/2083502573546263002)

### OpenClaw 与 OpenAI 的 Peter Steinberger

Peter Steinberger 展示了 agent 从建议工具走向代办行动的一个小案例：他长期受 Gmail 界面困扰，最终直接让 agent 为自己安装了替代工具。[原始推文](https://x.com/steipete/status/2083759812970786997)

他还在 ESP32 芯片上构建 claw node，并开放摄像头给 agent 做端到端测试。这个略显荒诞的调试现场说明，agent 已经开始跨出纯软件环境，直接参与语音唤醒与硬件交互的验证。[原始推文](https://x.com/steipete/status/2083694161933594703)

## 官方博客

### Anthropic Engineering: How we contain Claude across products

Anthropic 的核心结论是：agent 越有能力、权限越大，就越不能把安全完全押在人类审批或模型判断上，必须通过 sandbox、VM、文件系统边界和 egress control，先在环境层给潜在损害设置硬上限。真实数据说明了原因：Claude Code 用户会批准约 93% 的权限请求；即使 Opus 4.7 在单次 prompt injection 测试中把攻击成功率压到约 0.1%，100 次自适应攻击后仍会上升到约 5% 至 6%。

三种产品因此采用不同隔离模式：claude.ai 使用短生命周期容器，Claude Code 依赖适合开发者监督的本地 sandbox，Claude Cowork 则用 sealed VM 保护非技术用户。团队复盘的事故更值得注意：恶意仓库曾在“信任此文件夹”确认前触发项目配置；内部钓鱼提示在 25 次尝试中有 24 次成功诱导凭证外传；允许访问 api.anthropic.com 的白名单也曾被攻击者借自己的 API key 绕成数据外传通道。

文章把经验浓缩为一句话：“当一切概率性防线都漏掉时，真正承受冲击的是确定性的边界。”实际启示是优先使用经过长期攻防检验的 hypervisor、seccomp、gVisor 等组件，谨慎对待自研代理与编排层，并把 allowlist 视为能力授权，而不只是域名过滤。[原文](https://www.anthropic.com/engineering/how-we-contain-claude)

## 播客

### No Priors: Building an Autonomous Enterprise for Real-World Services with Netic Founder Melisa Tokmak

核心结论：AI 在现实服务业最大的机会，不是先替代上门劳动，而是把客户理解、调度、销售和运营变成自主运行的企业系统。

Netic 创始人兼 CEO Melisa Tokmak 曾在 Scale AI 负责政府和大型企业业务，也有 Meta 经历。她把 Netic 放在 HVAC、管道、电力、宠物服务、健身与汽车等企业和终端客户之间，让 agent 通过电话、短信和网站理解需求，再结合设备类型、紧急程度、客户价值和技师能力决定谁在何时上门。她说，超过 70% 的客户已经采用“Netic first”，即消费者第一次接触企业时先与 Netic agent 互动。

她的反直觉判断是，传统服务业并不落后，反而非常重视可量化价值；Netic 曾在 14 天内签下一份约 50 万美元的合同，并称 AI 处理的互动已为客户创造超过 6 亿美元收入。真正壁垒也不只是模型，而是最后一公里的 harness、orchestration、行业软件和现场理解。她直言：“如果只是等 AGI 再来解决 essential services，这在运营上和智识上都有点懒惰。”

长期愿景是让 Netic 自主处理企业中除实际服务劳动之外的一切。她认为机器人短期内仍难应对真实建筑、设备和人类情境的巨大差异，因此 AI 更现实的价值是先扩大蓝领服务能力、创造新增收入，而不只是降本。[观看本期播客](https://www.youtube.com/watch?v=wWbX3NL6_Uo)

Generated through the Follow Builders skill: https://github.com/zarazhangrui/follow-builders
