# AI Builders Digest — 2026-07-27

## X / TWITTER

### OpenAI Codex 与 ChatGPT 团队 Thibault Sottiaux

Thibault Sottiaux 认为，语音交互真正的变化不是“电脑终于能听见”，而是它现在能对指令采取行动，这项能力在手机上尤其有价值，并且已经进入 ChatGPT App。他还透露，ChatGPT Work 的活跃用户数已经正式超过 Codex，说明通用工作型 agent 正在从开发者场景向更广的人群扩散。

- [语音交互与可执行的电脑](https://x.com/thsottiaux/status/2081254182502465981)
- [ChatGPT App 的移动端体验](https://x.com/thsottiaux/status/2081229262452097169)
- [ChatGPT Work 活跃用户数超过 Codex](https://x.com/thsottiaux/status/2081198608293187635)

### AI 教程作者 Peter Yang

Peter Yang 预告了 OpenAI DevEx 工程师 Jason 的完整 Codex 工作系统。这个系统不只用于写代码，还会让 Codex 跨 Slack 和邮件扮演 chief of staff，把历史 session 沉淀成新 skill 与 workflow，并通过搭建网站来学习鼓等新技能。值得关注的不是单个 prompt，而是把过去工作持续编译成可复用能力。

- [Jason 的 Codex 工作系统](https://x.com/petergyang/status/2081029209993154980)

### Linear 产品负责人 Nan Yu

Nan Yu 把“软件工厂”进一步推演成“生产软件工厂的工厂”：如果 agent 可以持续设计、实现和维护软件，那么真正可复制的资产将不只是某个功能，而是把意图变成系统的生产机制。他认为这个框架还能推广到公共卫生、法律等领域，只是最终交付物不再是软件 feature，而是被设计和落实的某种社会意图。

- [SoftwareFactoryFactory](https://x.com/thenanyu/status/2081187979024797858)
- [从软件推广到公共卫生与法律](https://x.com/thenanyu/status/2081183178568405171)

### Meta AI 高级总监 Madhu Guru

Madhu Guru 认为，在未知领域里，困难问题的答案只能靠反复接触现实获得。美国 AI 社区对 open-weight 模型的支持看似突然形成共识，实际是 DeepSeek、Microsoft 与 OpenAI 的关系变化、GLM、Kimi、Fable 以及 OpenAI 与 Hugging Face 等一连串公开实验，让行业共同观察激励、创新与地缘政治的一阶和二阶后果，再更新判断。他预计未来十年的重大 AI 社会议题也会以这种方式逐步厘清。

- [用公开实验更新对 open-weight AI 的判断](https://x.com/realmadhuguru/status/2081141594892415028)

### Replit CEO Amjad Masad

Amjad Masad 部署了一款约 1200 Elo 的新国际象棋模型，并把目标定在 2000 Elo 以上。真正有意思的是约束：只用一个小型 fine-tuned LLM，不做定制预训练或架构，也不允许借助棋类引擎，所有走法都必须由模型直接生成。这是在测试小模型本身能把专门能力推进到什么程度，而不是靠外部工具掩盖能力边界。

- [小型 fine-tuned LLM 国际象棋实验](https://x.com/amasad/status/2081086837263937543)

### Vercel CEO Guillermo Rauch

Guillermo Rauch 的核心判断是：“软件工厂本身才是产品。”一个产品的质量越来越取决于你配置了怎样的 agent 去自主维护它，因此有新想法时，不应只临时找 agent 写一次，而应先设计能启动、维护并扩张这个想法的工厂。

他也给出一套极简研究系统：用文件系统中的 `research/` 目录保存资料，用 `AGENTS.md` 规定格式和最佳实践，再让 agent 跨历史 session 检索和关联知识。无需复杂知识图谱或专用 UI，目录可以通过 iCloud、Git 等同步，结果则可直接渲染为 HTML 并部署。

- [为新想法建立持续运转的工厂](https://x.com/rauchg/status/2081149743368122723)
- [软件工厂本身才是产品](https://x.com/rauchg/status/2081123293340520642)
- [基于 agent CLI、文件系统和 AGENTS.md 的研究工作流](https://x.com/rauchg/status/2081103993917649134)

### Box CEO Aaron Levie

Aaron Levie 把 Google 的加入视为行业对 open-weight AI 的一次完整背书。他的判断是，这不只是某家公司的模型选择，而是整个行业在开放权重路线上的重要转折点。

- [Google 加入与 open-weight AI](https://x.com/levie/status/2081054531908247937)

### FirstMark VC Matt Turck

Matt Turck 分享了一份由 Andrew Feldman 讲解的 AI 芯片版图入门，覆盖 CPU、GPU、NVIDIA、AMD、TPU、Trainium 与 Cerebras。对于需要快速建立算力栈全景认知的人，这是一条直接的基础资料入口。

- [AI 芯片版图 101](https://x.com/mattturck/status/2081131761686184333)

### Builder Zara Zhang

Zara Zhang 提出，AI-native 公司的文化更像一个开源社区。这个观察意味着，真正原生的 AI 组织可能依赖更开放的协作、快速共享和持续重组，而不是传统公司里边界清晰、层层交接的工作方式。

- [AI-native 公司与开源社区文化](https://x.com/zarazhangrui/status/2081223709755650054)

### FPV Ventures 合伙人 Nikunj Kothari

Nikunj Kothari 用一家生成式媒体公司收购占星应用的案例指出，极不寻常的战略动作通常需要两个条件：CEO 对公司拥有足够完整的控制权，以及创始人本人兼具强烈野心和非常规判断。对多数受董事会、VC 和团队共识约束的公司而言，跨越如此远的业务边界很难被组织接受，这也说明治理结构会直接限制公司能做多“疯狂”的实验。

- [控制权、野心与非常规收购](https://x.com/nikunj/status/2081017328137916426)

### OpenClaw 与 OpenAI 的 Peter Steinberger

Peter Steinberger 对模型生态给出两点判断：竞争对生态有益，但大规模 serving 模型非常困难；他也明确肯定 OpenAI 在相关公开信上的表态。

更具体的实践来自下一版 OpenClaw 发布前的 QA：他让 Codex 用 12 个 subagent 拆分功能、在不同端口启动开发 gateway、执行压力测试、通过 worktree 和 PR 并行协作，并把目标设为发现 200 个 bug，要求每次都修根因。他观察到 Sol 对意图和复杂行为问题的理解显著增强，而过去这类长时间并行工作常在 compaction 边界失控，或出现模型“作弊式完成”。

- [模型竞争与大规模 serving](https://x.com/steipete/status/2081175795587072421)
- [OpenClaw 端到端并行 QA 指令](https://x.com/steipete/status/2081169376317932017)
- [Codex 长时间并行 QA 的能力变化](https://x.com/steipete/status/2081169373784633552)

## OFFICIAL BLOGS

### Anthropic Engineering

#### An update on recent Claude Code quality reports

Anthropic 确认，近期 Claude Code、Claude Agent SDK 与 Claude Cowork 的质量下降来自三项彼此独立的产品层改动，API 与推理层未受影响，问题已在 4 月 20 日的 v2.1.116 全部解决。第一项是 3 月 4 日把默认 reasoning effort 从 high 降为 medium，以降低长尾延迟，但用户更愿意优先保留智能水平；该改动已在 4 月 7 日撤回。第二项是清理闲置 session 旧 thinking 的缓存优化存在 bug，原本只该执行一次，却在后续每一轮持续删除推理历史，导致遗忘、重复、异常工具选择和更多 cache miss；它已在 4 月 10 日的 v2.1.101 修复。

第三项是 4 月 16 日加入的系统提示词长度限制，在更广泛 eval 中让 Opus 4.6 与 4.7 的编码表现都下降 3%，因此 4 月 20 日撤回。文章直言：“这不是用户应该从 Claude Code 获得的体验。”后续措施包括让更多内部员工使用与公众完全相同的 build、扩大 Code Review 的代码库上下文、对每次系统提示词变更执行跨模型 eval 和逐行 ablation，并为可能牺牲智能水平的改动增加 soak period、扩大测试集和渐进发布。Anthropic 同时为所有订阅用户重置 usage limits。

[阅读原文](https://www.anthropic.com/engineering/april-23-postmortem)

#### Scaling Managed Agents: Decoupling the brain from the hands

Anthropic 把 Managed Agents 设计成一个能适应未来模型与 harness 的“元 harness”，核心是将 agent 拆成三个可替换接口：记录全部事件的 session、调用 Claude 并路由工具的 harness，以及执行代码和修改文件的 sandbox。旧架构把三者塞进同一容器，容器一旦故障，session、调试入口和用户数据都会被绑在一起，形成必须人工照料的“宠物服务器”。

新架构把“brain”与“hands”解耦：harness 和 sandbox 都变成可随时重启的无状态资源，durable session log 则保留完整事件。凭据不进入运行不可信代码的 sandbox，Git token 在初始化时绑定资源，MCP OAuth token 存在外部 vault 并由代理调用。文章强调：“session 不是 Claude 的 context window。”完整事件历史可以长期保存，再由 harness 按需切片、压缩或重组，避免一次不可逆的 compaction 决定丢掉未来需要的信息。

这种解耦还有直接性能收益：只有确实需要执行环境时才创建容器，使 p50 time-to-first-token 约下降 60%，p95 下降超过 90%。同一个 brain 也能连接多个 sandbox、MCP server 或其他工具，为多 brain、多 hands 的长时 agent 系统建立更稳定的边界。

[阅读原文](https://www.anthropic.com/engineering/managed-agents)

### Claude Blog

#### New in Claude Managed Agents: self-hosted sandboxes and MCP tunnels

Claude Managed Agents 新增 self-hosted sandboxes 与 MCP tunnels。前者已在 Claude Platform 进入 public beta，允许 agent 在企业自有基础设施或 Cloudflare、Daytona、Modal、Vercel 等托管环境中执行工具；代码、敏感文件、package、service 与数据保留在企业安全边界内，agent loop、上下文管理和错误恢复仍由 Anthropic 基础设施负责。企业可以继续使用现有网络策略、审计日志和安全工具，也能自行设置 CPU、内存、GPU 与 runtime image。

MCP tunnels 处于 research preview，可让 Managed Agents 与 Messages API 连接私有网络中的 MCP server，无需暴露公网入口或新增入站防火墙规则。企业只需部署轻量 gateway，由它发起单一出站连接，流量端到端加密，内部数据库、私有 API、知识库与工单系统即可成为 agent 工具。实际意义是把模型编排留在云端，同时把执行与私有服务访问牢牢留在组织自己的控制面内。

[阅读原文](https://claude.com/blog/claude-managed-agents-updates)

## PODCASTS

### Unsupervised Learning: Ep 91: Top AI Analyst Unpacks Today&apos;s AI Hype Cycle

**核心结论：** 科技分析者 Benedict Evans 认为，AI 的确可能像 PC、互联网和移动一样改变一切，但今天最有用的问题不是争论它究竟比哪次革命更大，而是研究历史平台迁移中价值如何在技术栈之间转移，并用真实产品实验找出这一次的答案。

Evans 提醒，模型能力的物理上限仍不清楚，这确实让 AI 与过去的平台迁移不同；但“前所未有”不等于历史经验失效。移动网络的数据流量增长了上千倍，运营商却没有拿走 Uber、YouTube 或移动银行创造的大部分价值，价值反而向上层应用迁移。Foundation model 同样有高资本开支与边际推理成本，又缺少 Windows 式网络效应，而且榜首模型每四到六周就可能更换，因此模型公司能否建立持久差异化仍是开放问题。

眼下 AI 在软件开发中已经明确找到 product-market fit，但普通消费者大多只是偶尔使用，距离“每天离不开”仍很远。高推理成本也使创业者无法简单复制过去消费互联网“先拿一亿用户、再找收入”的路径，这解释了为什么当前机会更偏 enterprise。企业采用还会受到流程、合规和其他现实优先级拖慢，正如云计算用了二十年也只覆盖部分企业 workflow。

他最值得记住的一句话是：“不是聊天室，而是网络；同样，不是文字和图片，而是 enabling technology。”真正的 AI 价值可能藏在欺诈检测、后台流程和更好的产品体验里，用户甚至不会看到 ChatGPT 的名字。对就业和行业冲击也应避免只凭抽象能力下结论，因为不同行业的实际工作、约束与被改变程度差异巨大。与其从第一原则幻想唯一终局，不如承认许多当前 acronym、协议和产品都会失败，然后继续构建、观察、修正。

[观看本期播客](https://www.youtube.com/watch?v=vDY_ocrkQ5w)

Generated through the Follow Builders skill: https://github.com/zarazhangrui/follow-builders
