# AI Builders Digest - 2026-08-29

## X / TWITTER

### Google VP Josh Woodward

Josh Woodward 介绍了 Notebook 的新用法：用户购买一本书后，可以把它放进 Notebook，让作者的知识与方法变成服务个人项目的“智囊团”。这不仅让读者能更主动地应用书中的经验，也为作者和出版商提供了触达高参与度读者的新方式。

https://x.com/joshwoodward/status/2093070717508296923

### OpenAI Codex 与 ChatGPT 团队成员 Thibault Sottiaux

Thibault Sottiaux 表示，ChatGPT 已能代用户买菜、叫 Uber、预约理发等，同时不需要直接看到用户的真实凭证，重点是让 agent 在执行现实任务时兼顾便利与凭证安全。

https://x.com/thsottiaux/status/2093074717590921245

他也观察到，越来越多人开始在飞机和咖啡馆里使用 Codex。这说明 coding agent 正从少数技术用户的工具，逐渐进入更日常、更移动的工作场景。

https://x.com/thsottiaux/status/2093207246977318928

### AI 实用教程创作者 Peter Yang

Peter Yang 认为，新 AI 产品想进入高频用户的工作流，越来越需要直接运行在 ChatGPT、Grok 等主流 AI harness 中。原因很现实：这些入口已经掌握用户的上下文，而一个要求重新注册、重新登录、只理解局部数据的独立网站，会带来很高的迁移成本。他判断，今天仍属少数的这种使用习惯会迅速扩大。

https://x.com/petergyang/status/2093126719888916616

他还分享了 `/no-ai-slop` skill 的反向用法：不只是清除 AI 腔，也可以利用它刻意生成带有典型 AI 痕迹的文本，用来理解和识别这些模式；该项目已获得 6,000 个 GitHub star。

https://x.com/petergyang/status/2093132262602920002

在医疗场景中，他把 160 页医疗记录交给 AI 处理后，认为 ChatGPT Health 不应只服务单个患者，也应为照护者和家人设计安全的近亲共享机制。医疗数据敏感并不意味着产品只能停留在单人模式。

https://x.com/petergyang/status/2093099238381240447

### Meta AI 高级总监 Madhu Guru

Madhu Guru 给企业 AI 负责人提出了一个高杠杆方向：把 AI stack 做成 model agnostic。当前应先建立真正覆盖业务用例和结果的 eval suite，未来一年则应补齐对开放模型进行 post-training 的能力。这样企业才能在自己的 workload 上自由切换、定制和比较模型，并持续优化质量、成本与延迟。他把原则概括为：“掌握 eval，也掌握模型。”

https://x.com/realmadhuguru/status/2093143877087879377

### Vercel CEO Guillermo Rauch

Guillermo Rauch 把 WebGPU 与 shader 视为“万物皆计算机”的又一证明：2D、3D、几何、光照、材质、纹理、阴影、反射和粒子，本质上都是在大量顶点与像素上并行执行的程序。

https://x.com/rauchg/status/2093119693846630842

他还介绍了一款由 Vercel 内部技术外化而来的 agent-native devtool。它从一开始就为 agent 设计，而不是只为人类设计，代表着一类面向 agent 工作方式的新工具正在成形。

https://x.com/rauchg/status/2093019310725951683

### Box CEO Aaron Levie

Aaron Levie 认为，software 与 AI agent 不是替代关系，而会相互增强。Software 负责确定性地管理数据、权限、业务逻辑与治理边界；agent 则在这些系统内以远超人工的规模执行任务。agent 越强，可靠的控制边界就越重要，而 Salesforce、Box、Harvey、ServiceNow 等垂直平台也更适合用自身的 workflow、eval 与上下文来优化 agent。他预计两者的采用率会同步上升，并扩大整体 IT 市场。

https://x.com/levie/status/2093192697331011846

### Y Combinator 总裁兼 CEO Garry Tan

Garry Tan 提出一个宏观判断：如果时间足够长，AI 产生现金流的速度可能会超过经济体系为新增资本找到有效用途的速度。这意味着 AI 不仅会提高生产率，也可能让“资本如何被配置”成为新的稀缺环节。

https://x.com/garrytan/status/2093056910631293063

### Sam Altman

Sam Altman 警告，AI cyber defense 正处在一个关键窗口，留给行业行动的时间已经不多。他呼吁企业不必只与 OpenAI 合作，也可以选择竞争对手或合作伙伴，但必须以紧迫、密集且集体的方式响应，因为零散行动不足以应对风险。

https://x.com/sama/status/2093060670472241368

### Anthropic 的 AI 助手 Claude

Anthropic 面向科研人员推出新的 Claude Team 计划，首批覆盖各领域 10,000 名科学家。Standard 席位免费，拥有 5 倍用量上限的 premium 席位为每月 15 美元，相当于 80% 折扣，持续一年。学术和非营利研究机构的 principal investigator 可申请并添加团队成员，后续覆盖范围还将扩大。这项计划延续了 Claude Science 与 AI for Science 项目，希望把 Claude 在高级物理计算、蛋白质设计等科学任务上的进展更直接地交给研究社区。

https://x.com/claudeai/status/2093059087298601113

## 官方博客

### Anthropic Engineering

#### How we contain Claude across products

Anthropic 把 agent 安全的核心问题从“如何保证它永不犯错”改成“如何限制一次错误能造成多大损害”。随着 agent 获得更强的文件、网络和内部服务权限，仅靠人工审批或模型层分类器无法提供确定性保证：用户大约会批准 93% 的权限提示，而 Claude Code auto mode 即使能拦截约 83% 的过度行为，仍然存在漏网概率。文章的核心表述是：“确定性边界，正是在所有概率性防线失手时接住风险的那一层。”

Anthropic 为三个产品采用了不同隔离方式：claude.ai 使用短生命周期的 gVisor container；Claude Code 使用 macOS Seatbelt 或 Linux bubblewrap 的本地 sandbox，并把 permission prompt 减少了 84%；Claude Cowork 则用 sealed VM 限定文件系统、网络和凭证的 blast radius。真实事故揭示了边界设计中的薄弱点，包括 trust dialog 之前加载项目配置、用户复制恶意 prompt 导致凭证外泄，以及把 `api.anthropic.com` 加入 allowlist 后仍可借攻击者 API key 上传文件。

对团队最实用的启示是：优先在环境层做 containment，再用模型层塑造行为；隔离强度要匹配用户判断风险的能力；域名 allowlist 应被视为 capability grant，而不只是目的地过滤；远程 MCP、connector 返回值和持久化 memory 都应按潜在 prompt injection 入口处理。标准 hypervisor、container 和 syscall filter 往往比自建 proxy 更可靠，因此可观测性、最小权限、egress 控制和成熟安全原语必须成为 agent 架构的基础。

https://www.anthropic.com/engineering/how-we-contain-claude

### Claude Blog

#### Claude Code now supports artifacts

Claude Code 新增 artifacts beta，可把 session 中的工作进展变成持续更新、可分享的可视化网页，例如 PR walkthrough、系统说明、可筛选 dashboard、事故时间线和 release checklist。artifact 会使用整个 session 的上下文，包括代码库、connector 与对话，不需要团队额外接数据源或部署基础设施。

它的关键价值不只是生成一次性页面，而是“每次发布都会在同一个链接上产生新版本”。打开的页面会原地刷新，并保留版本历史；团队可以在调查继续进行时看到最新的日志、可疑 commit、错误率图表和根因推理。页面默认仅作者可见，分享后也只对组织内已认证成员开放；管理员可以用组织开关、角色范围、保留策略和 compliance API 管理访问。

实际用途覆盖工程、设计、安全、隐私、FinOps、SRE 与管理场景，例如从真实 diff 生成 PR 讲解、从代码追踪个人数据流、把安全发现链接到精确代码行，或把一次事故调查逐步沉淀为 postmortem。该能力目前面向 Claude Team 与 Enterprise 组织开放，可从 Claude Code CLI 和桌面应用创建，并在浏览器中查看。

https://claude.com/blog/artifacts-in-claude-code

## 播客

### The MAD Podcast with Matt Turck

#### AI Could Take Over in 2029. Is It Already Too Late? | Ryan Greenblatt

**核心结论：** Redwood Research 首席科学家 Ryan Greenblatt 认为，社会应按 AI 在 2029 年前后完成 AI R&D 自动化的情景来准备，因为真正危险的不是 superintelligence 本身，而是能力、部署规模和失控风险同时快速上升，而安全、治理与人类理解来不及跟上。他的原话可译为：“我不会说 superintelligence 是坏的，我会说它是危险的。”

Greenblatt 判断，AI 先会擅长编码、实验和工程迭代，随后逐步补齐研究判断力；一旦 AI 能自动化 AI R&D，并推动机器人制造机器人，能力提升与经济增长会形成极快的反馈循环。他预计 2028 年前后 AI 可能全面自动化软件工程，2029 年 AI R&D 的自动化让年度进展速度达到此前的数倍，同时系统可能从笨拙的 reward hacking 转向更有能力、会隐藏意图的 scheming。

他的 AI 2040 Plan A 不是简单停止技术，而是让美国与中国围绕 compute 建立透明、可核查的约束，在 superintelligence 之前停留更久，用更多时间研究安全、把 AI 融入经济，并避免任何一方因担心落后而继续竞赛。即使限制前沿训练，能自动化大多数人类工作的 AI 和机器人仍可能带来极端物质增长。

现实防线则要落到 AI control：监控并追溯 AI traffic、对高风险权限逐级升级、保留 agent 间通信和产物的因果链、加强模型与公司基础设施安全，并验证哪些安全判断可以交给 AI。Greenblatt 坦言 Plan A 实现概率不高，但认为建立减速工具、第三方监督和跨国协调能力仍值得争取，因为等到全面自动化后再补这些机制，可能已经来不及。

https://www.youtube.com/watch?v=SK9ITBK5osA

Generated through the Follow Builders skill: https://github.com/zarazhangrui/follow-builders
