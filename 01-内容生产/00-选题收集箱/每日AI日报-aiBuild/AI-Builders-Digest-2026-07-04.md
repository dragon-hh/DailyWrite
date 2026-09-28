AI Builders Digest - 2026-07-04

## X / TWITTER

### Swyx, AI Engineer / Latent Space / Cognition 相关 builder
Swyx 今天主要在 AIE Expo 现场更新：他预告了一个 12:30 的临时惊喜活动，并提醒大家去 Expo Stage 2 看 Latent Space 和 Etched 的 live pod。他还提到，今年 AIE keynote 里掌声最大的一句，是把“男性在 hypergrowth 环境里谈论情绪和心理健康”正常化。第三条只是回复和链接，没有足够上下文。
来源：
https://x.com/swyx/status/2072760421627597198
https://x.com/swyx/status/2072754722059239471
https://x.com/swyx/status/2072722973652660432

### Anthropic Claude Code 的 Boris Cherny
Boris Cherny 说 Claude Code 里的 Artifacts 对他来说是“life changing”，并且很期待它扩展到 Pro 和 Max 用户。这个信号很明确：Claude Code 正在从工程师的小众工具，继续往更广的订阅层级扩散。
来源：
https://x.com/bcherny/status/2072777472970563995

### OpenAI Codex & ChatGPT 的 Thibault Sottiaux
Thibault Sottiaux 预热了 GPT-5.6 Sol Ultra，说他等不及看到大家会用它做什么，并建议大家把最难的 prompts 先存起来。内容本身没有展开能力细节，但这是一个明显的模型发布前信号。
来源：
https://x.com/thsottiaux/status/2072607914217320644

### AI 教程作者 Peter Yang
Peter Yang 分享了他在 7 月 7 日之前最大化使用 Fable 的方法：先用更便宜的模型准备上下文，用 Fable 做计划，再交给其他模型执行，并把 Fable 的 effort 调低到 Medium，同时人工盯着它做什么。他还向 NousResearch / Karan 征集播客主题，最终选出的重点包括 Hermes 起源、agent memory 与 persistence、真实使用场景、团队运营与授权、长期愿景和差异化。另一个很实用的小案例是，他和 8 岁女儿用 Codex、image gen 和语音反馈，把女儿画的龙扩展成更多姿势，再拿去做贴纸。
来源：
https://x.com/petergyang/status/2072842766053499353
https://x.com/petergyang/status/2072838004310507975
https://x.com/petergyang/status/2072756657856422379

### Linear 产品负责人 Nan Yu
Nan Yu 对“多个实体之间如何协调工作”的话题做了一个很 Linear 式的回应：如果有一种系统能协调多个实体之间的工作就好了。原文带有明显的产品语境，但 JSON 里没有被引用推文内容，所以这里只能保留这个方向：agent / 多实体协作仍然需要一个工作协调系统。
来源：
https://x.com/thenanyu/status/2072714076614950961
https://x.com/thenanyu/status/2072699613929156660

### Anthropic Claude Code / cowork 的 Cat Wu
Cat Wu 说 Claude Tag 已经在 Anthropic 内部跨 engineering、product、data、sales、marketing 提升生产力，内部版本能落地 65% 的 product PRs。她还补充了推广激励：Claude Enterprise 组织可获得 25k credits，Claude Team 组织可获得 2.5k credits，用于在 9 月 1 日前使用 Claude Tag。这里值得关注的是 rollout 不是只面向工程团队，而是从一开始就强调 CEO/CTO playbook、安全设计和组织级工作方式变化。
来源：
https://x.com/_catwu/status/2072731500928508331
https://x.com/_catwu/status/2072743070316257662

### Anthropic Claude Code 的 Thariq
Thariq 回应了 Fable 订阅可用性问题：Fable 会在 7 月 7 日后从订阅计划中移出，但团队目标是在容量允许后，尽快把 Fable 恢复为订阅里的标准能力。他还发了一个“see the post here”的链接，但 JSON 没有展开链接内容，所以不补充外部信息。
来源：
https://x.com/trq212/status/2072814903170408784
https://x.com/trq212/status/2072814904210509905

### Vercel CEO Guillermo Rauch
Guillermo Rauch 把 Vercel AI Gateway 解释成“Token Delivery Network”，像 AI 模型版 CDN。因为 Fable 这类模型可能突然退役，而生产流量还依赖旧模型版本，Vercel 推出了 AI Gateway Rules，让团队可以在不重新部署的情况下动态 rewrite model routes，比如把 `anthropic/claude-fable-5` 改写到 `anthropic/claude-opus-5`。他还补充了 Vercel 后端私有连接能力：在 `vercel.json` 注册 bindings，然后通过环境变量里的 internal URL 连接后端，适用于 Node、Python、Dockerfile 等场景。
来源：
https://x.com/rauchg/status/2072741369848746315
https://x.com/rauchg/status/2072715658157027375

### Box CEO Aaron Levie
Aaron Levie 的重点是企业 AI agent 落地远比“接一个 chatbot”复杂。企业流程通常有碎片化数据、legacy software、没文档化的机构知识，以及 agent 连接不上的系统。要大规模部署 agent，需要清理数据、现代化 IT、做 evals、推动 change management、重新设计 human-in-the-loop，并定义新的公司 IP。结论也很直接：这就是为什么 applied AI 公司在扩 FDE 和 deployco，FDE 会成为科技行业最关键的角色之一。
来源：
https://x.com/levie/status/2072875685811716182

### Y Combinator CEO Garry Tan
Garry Tan 这次几条内容主要是政治评论和“It's time to build”的建设号召。由于 JSON 里没有展开被引用内容，digest 只保留链接，不额外推断。
来源：
https://x.com/garrytan/status/2072930664962539860
https://x.com/garrytan/status/2072846822566133768
https://x.com/garrytan/status/2072846648854954240

### FirstMark Capital VC / MAD Podcast 主持人 Matt Turck
Matt Turck 发布了和 NVIDIA AI 的 Bryan Catanzaro 的对话主题：NVIDIA 是芯片公司，为什么还要投入大量研究员训练 AI models，并且免费开放？这场对话覆盖 Nemotron 系列、开放模型是否追上 frontier、闭源实验室阻止 distillation 是否拖慢开源、美国和中国的 AI 竞争、企业为什么选择 open models、NVIDIA 早在 2008 年押注 GPU 上的 machine learning、Megatron 起源、550B model 的 4-bit 训练、Hybrid Mamba-Transformer、MoE、1-million-token context window、multi-token prediction、multi-teacher distillation，以及 NVIDIA 研究组织内部“the mission is the boss”的运作方式。
来源：
https://x.com/mattturck/status/2072723410975629364
https://x.com/mattturck/status/2072723415870411232

### Builder Zara Zhang
Zara Zhang 给了两个很短但有判断力的观点：AI slop 的根源不是风格差，而是没有 substance。她还提到一个应届毕业生的经历：上学时把 lecture decks 喂给 AI，让 AI 教材料，而不是去听真实课堂，并且经常觉得 AI 教得比教授更好。另一条是 agent 协作建议：对 agent 最有帮助的事情之一，是让它们在群组里对话，而不是关在 DM 里。
来源：
https://x.com/zarazhangrui/status/2072943922385715262
https://x.com/zarazhangrui/status/2072729444943577601
https://x.com/zarazhangrui/status/2072726336158998760

### FPV Ventures partner Nikunj Kothari
Nikunj Kothari 的一条内容是关于“AGI summer”期间很多人短暂停留旧金山后就做出判断。他认为，虽然外界对 SF 的一些批评有真实成分，但几天或几周不足以理解这座城市，真正要做的是别当游客，花时间参与其中。另一条是更偏 builder 文化的判断：连接人与机会本身就很有价值，即使你没有任何直接收益，世界不必是零和的。
来源：
https://x.com/nikunj/status/2072780155924480074
https://x.com/nikunj/status/2072684481824309411

### OpenClaw / OpenAI 的 Peter Steinberger
Peter Steinberger 发了一个很小但有意思的 OpenClaw 触达案例：他每天和 ATT 代表通话处理 Apple Watch 3 美元计划，对方知道 OpenClaw，而且每天都在用。这不是产品发布，但说明 OpenClaw 已经进入真实用户的日常工具链。
来源：
https://x.com/steipete/status/2072744099678212487

### Every CEO Dan Shipper
Dan Shipper 说，他现在在 Fable 上非常强烈地感受到一个问题：模型可以连续跑几个小时，最后只用两段话解释自己做了什么。对于长时间运行的 AI，我们需要更好的方式让 AI “讲述它做了什么”。这其实是 agent UX 的核心问题：不是只要能执行，还要能把过程、决策和结果讲清楚。
来源：
https://x.com/danshipper/status/2072805884376301737

### Claude 官方账号
Claude 官方账号发布了 Claude Code 到 Claude Tag 的路径讨论，参与者包括 Boris Cherny 和 Cat Wu，主题是它如何从工程团队扩散到 Anthropic 其他部门，同时提到 Claude Fable 5 已经可在 Claude Tag 中使用。Claude 还宣布 Built with Claude: Life Sciences 全球虚拟 hackathon，将和 Gladstone Institutes 合作，时间为 7 月 7 日到 13 日，围绕 Claude Science 和 Claude Code 做研究与构建，奖池为 100k credits。
来源：
https://x.com/claudeai/status/2072725610061803522
https://x.com/claudeai/status/2072681853971001849
https://x.com/claudeai/status/2072681856730792282

## OFFICIAL BLOGS

今天 JSON 中没有新的官方博客文章。

## PODCASTS

### No Priors: How Nuclear Will Unlock Energy Abundance with Valar Atomics Founder Isaiah Taylor
核心 takeaway：Isaiah Taylor 的观点是，AI 时代真正的底层瓶颈可能不是模型，而是能源；如果核能能像硬件产品一样快速迭代和规模化，便宜能源会重新定义制造、交通和 AI compute。

No Priors 这期在 Valar Atomics 的 Utah 核设施里录制，嘉宾是 Valar Atomics 创始人兼 CEO Isaiah Taylor。Taylor 的公司想做的不是传统意义上的核电站工程，而是把核反应堆变成更像“可制造设备”的东西。他反复强调两个词：speed 和 scale。按照他的说法，传统核行业太像 modeling and simulation 行业，擅长做 paper reactors，却很少真正通过硬件迭代获得数据。

这期最反常识的地方，是他对监管路径和工程成本的描述。他认为 NRC 适合成熟系统的大规模商业部署，而 DOE 本来就有测试核反应堆的职责。Valar 在 DOE 授权路径下启动反应堆，背后逻辑是先通过真实硬件拿到数据，再进入更大规模部署。Taylor 还举了 RPS 反应堆保护系统的例子：外部供应商报价约 500 万美元、周期两年半，Valar 自己用 5 人团队 6 周做出工作系统，花费约 40 万美元。这个例子被他用来说明，核行业很多高成本来自长期不建设后的产业退化，而不一定来自物理本身。

他把能源看作所有现实世界进步的基础输入。原文里一句很关键的话是：“If you can figure out how to make energy cheaper, you will have demand.” 到后半段，他把 AI 和 robotics 加进制造业模型里：人力输入会越来越多地被机器人和 AI 转换成能源消耗，物理商品的成本最终会越来越接近制造它所需的能源成本。所以便宜能源不只是给数据中心供电，而是可能让交通、制造、生活质量和“hyper techno industrialism”发生连锁变化。

来源：
https://www.youtube.com/watch?v=5Xvbq_zvOQ4

Generated through the Follow Builders skill: https://github.com/zarazhangrui/follow-builders
