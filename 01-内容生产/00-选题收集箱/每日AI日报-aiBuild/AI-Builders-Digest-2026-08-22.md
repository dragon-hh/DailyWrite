# AI Builders Digest — 2026-08-22

## X / TWITTER

### Swyx

Swyx 重点介绍了一个被 NVIDIA 以 60 亿美元收购的“模型工厂”，称其正在持续产出表现超过 Thinky 的模型，并通过 Latent Space 播客拆解其价值。

https://x.com/swyx/status/2090577677916807429

他还推荐了 Matt Pocock 的 `/wayfinder`：当你身处信息迷雾、甚至不知道自己不知道什么时，它会编排研究与多轮追问，帮助你找到正确方向。

https://x.com/swyx/status/2090550020496040266

### Anthropic Claude Code 团队 Boris Cherny

Boris Cherny 表示，Mythos 级模型需要额外安全措施，也必须满足企业自己的隐私与合规要求。新方案允许客户拥有并控制自己的数据，Anthropic 不保留这些数据，计划于今年秋季推出。

https://x.com/bcherny/status/2090537902912815536

### OpenAI Codex 与 ChatGPT 团队 Thibault Sottiaux

Thibault Sottiaux 澄清，Codex 没有在未沟通的情况下调整正常订阅用户的用量限制。被标记的案例多与 sub2api 有关，即把订阅额度转成 API 流量后再次分发或多人共享；通过官方客户端或支持 Sign in With ChatGPT 的开源客户端使用订阅额度不受影响。

https://x.com/thsottiaux/status/2090675027670978569

GPT-Image-2 现在可在 ChatGPT 和 API 中生成透明背景图片；ChatGPT Site 也支持分享站点并与他人共同创作小游戏或网站。

https://x.com/thsottiaux/status/2090631723302469995

https://x.com/thsottiaux/status/2090518287532916854

### AI 实用教程创作者 Peter Yang

Peter Yang 提出一个简单的 agent 质量提升回路：让 manager agent 持续质疑 worker agent 的结果，例如要求它重新检查、再做一次并交付“11/10”的输出。关键不是增加一次更复杂的 prompt，而是用反馈循环逼出更好的结果。

https://x.com/petergyang/status/2090564541499498919

### Meta AI 高级总监 Madhu Guru

Madhu Guru 认为，企业 AI 系统表现不佳的核心原因往往不是模型不够强，而是缺少分层 eval 策略。她把 eval 分为四类：持续刷新、推动能力边界的 hill-climbing eval；防止现有产品退化的 regression eval；守住安全和基本正确性的 smoke test；以及更接近真实流量的 launch eval。四类 eval 分布在成本与真实性的不同位置，必须组合使用。

https://x.com/realmadhuguru/status/2090595384905113939

### Anthropic Claude Code 团队 Thariq

Thariq 宣布面向企业推出新的 Fable 安全方案，运行在客户自己的基础设施上，让企业控制数据存放位置与访问权限。该方案已与约 100 家公司共同开发，计划今年秋季扩大推出范围。

https://x.com/trq212/status/2090569474139439335

### Replit CEO Amjad Masad

Amjad Masad 表示 Replit 与 OpenAI 的合作“早该发生”，并回顾了 Replit 进入 YC 之前与 Sam Altman 的渊源。

https://x.com/amasad/status/2090514571513708874

他认为 Replit 新 Free Mode 最容易被低估的优势是速度，它让编程重新变得即时、可互动。

https://x.com/amasad/status/2090484698413740186

### Vercel CEO Guillermo Rauch

Guillermo Rauch 用一句“我们正在为 agent 构建 AWS”概括 Vercel 的基础设施方向：目标不只是托管应用，而是成为 agent 运行、调用工具和扩展工作负载的底层平台。

https://x.com/rauchg/status/2090520415336845595

### Box CEO Aaron Levie

Aaron Levie 认为，垂直 AI 公司会越来越多地采用 post-training，在特定任务上同时降低成本、提高准确率。当企业足够理解某个领域，并拥有大量相似任务时，就可以通过 reward shaping 鼓励更高效的工具调用和推理，在性能相当时减少推理 token。通用 frontier model 并不会消失，但当规模成本过高，或任务足够独特时，专门为工作流设计模型会成为应用层公司的重要优势。

https://x.com/levie/status/2090664811185205722

### Builder Zara Zhang

Zara Zhang 分享了一条改变她看待动力的提醒：“Motivation follows action more than it precedes it.” 动力更多是在行动之后出现，而不是行动之前；等待状态到来，往往不如先开始做。

https://x.com/zarazhangrui/status/2090399357145317837

### FPV Ventures 合伙人 Nikunj Kothari

Nikunj Kothari 从基金回报结构解释了为什么投资人如此看重“野心”。超大规模 AI 公司带来的回报抬高了 LP 的预期，也推动资金流向更大的基金；基金越大，单笔投资就越需要被推演到万亿美元级结果，小胜利在数学上难以影响整体回报。因此，热门项目中“错过”的代价往往被认为高于“投错”的代价，入场价格反而退居其次。创业者展示的市场上限，正在直接影响融资判断。

https://x.com/nikunj/status/2090585553947517298

## OFFICIAL BLOGS

### Anthropic Engineering

#### An update on recent Claude Code quality reports

Claude Code 近期质量下降并非模型或 API 被主动削弱，而是三个产品层变更叠加造成：3 月 4 日将默认 reasoning effort 从 high 降到 medium；3 月 26 日的缓存优化 bug 在闲置会话恢复后反复清除旧 reasoning；4 月 16 日加入严格限字的 system prompt，导致部分 coding eval 下降 3%。三项问题分别于 4 月 7 日、10 日和 20 日修复，最终版本为 v2.1.116，API 与推理层未受影响。

最值得注意的是，降低延迟的局部优化同时伤害了智能、记忆连续性和用量表现。Anthropic 承认默认 effort 的选择是“the wrong tradeoff”，并计划让更多员工使用与公众完全一致的构建版本，对每次 system prompt 改动运行更广的逐模型 eval、ablation、soak period 与渐进式发布，同时加强 Code Review 的跨仓库上下文。公司还为所有订阅用户重置了用量限制。

https://www.anthropic.com/engineering/april-23-postmortem

#### Scaling Managed Agents: Decoupling the brain from the hands

Anthropic 将 Managed Agents 设计成一种“meta-harness”：把 session、harness 和 sandbox 拆成稳定接口，让每一部分都能独立失败、替换与演进。核心思想是“Decouple the brain from the hands”。Claude 与 harness 是 brain，执行代码和工具的 sandbox 是 hands，完整事件日志则作为可持久恢复的 session。

这种解耦解决了三类问题。第一，容器从不可丢失的“宠物”变成可随时重建的“牲畜”，harness 崩溃后也能依据 session log 恢复。第二，凭据不再进入运行不可信代码的 sandbox，Git token 可在初始化时绑定资源，MCP OAuth token 则保存在外部 vault 并由代理调用。第三，session 不等于 context window，完整事件可以持久保存，harness 再按需切片、压缩或组织上下文，避免不可逆地丢失未来可能需要的信息。

性能收益同样明显：sandbox 只在真正需要时才配置，p50 time-to-first-token 约下降 60%，p95 下降超过 90%。这套架构也允许多个无状态 brain 动态连接多个 hands，并把模型能力变化留给 harness 演进，而不破坏外围接口。

https://www.anthropic.com/engineering/managed-agents

### Claude Blog

#### New in Claude Managed Agents: self-hosted sandboxes and MCP tunnels

Claude Managed Agents 新增 self-hosted sandboxes 公测和 MCP tunnels 研究预览。企业可以把代码执行、敏感文件、依赖、服务与数据留在自己的基础设施或 Cloudflare、Daytona、Modal、Vercel 等托管环境中；Anthropic 侧只保留 agent loop、上下文管理与错误恢复。这样，企业现有的网络策略、审计日志和安全工具可以直接覆盖 agent 的执行环境，并自行决定 CPU、内存、GPU 与运行镜像。

MCP tunnels 则让 Managed Agents 和 Messages API 访问私网中的数据库、API、知识库与工单系统，无需开放公网入口或配置入站防火墙。企业部署的轻量 gateway 只建立一条向外连接，流量端到端加密。实际意义是，agent 的“脑”可以由平台托管，而它的“手”和要触达的内部服务继续待在企业安全边界内。

https://claude.com/blog/claude-managed-agents-updates

## PODCASTS

### No Priors: From Restoring Sight to Reimagining the Brain, with Max Hodak

核心结论：把大脑当作可以工程化连接的计算系统，可能比等待我们彻底理解全部生物机制，更快带来恢复感官、延长健康寿命，甚至实现 substrate independence 的路径。

Science 创始人兼 CEO、Neuralink 前联合创始人 Max Hodak 正把这个判断变成医疗产品。Prima 是植入视网膜下方的微型芯片，配合带激光投影器的眼镜，绕过已经死亡的感光细胞，直接刺激视网膜。它已在欧洲获得商业销售许可，临床试验中有患者重新填写数独、做填字游戏，甚至阅读书籍。当前版本仍像“透过吸管看黑白世界”，但团队已有工程路线去扩大视野、增加灰阶，并尝试恢复红色和绿色。

Hodak 的反常识判断是：“the brain very literally, very clearly, plainly is a computer.” 这不是比喻，而是一种研发方法。相比可能花十年做药物发现后才得到失败答案，神经器件可以在明确反馈下持续迭代。Science 因此把视力、biohybrid neural interface 和 perfusion 组成一条 10 至 15 年路线，既追求可盈利的近期业务，也探索更长期的人体可替换部件。

他也不看好把 BCI 简化成“脑内键盘”。人的思考存在大约每秒 10 bit 的认知瓶颈，很多看似已经成形的想法，只有在说出或写下时才真正完成。更重要的方向是生成视觉、听觉、平衡和运动信号，重新划定大脑与外界的边界。AI 研究也可能反过来推动神经科学，因为大型模型的内部表示与大脑的概念表示呈现相似几何结构，甚至可以与动物神经记录对齐。

https://www.youtube.com/watch?v=7HXqMepjvy8

Generated through the Follow Builders skill: https://github.com/zarazhangrui/follow-builders
