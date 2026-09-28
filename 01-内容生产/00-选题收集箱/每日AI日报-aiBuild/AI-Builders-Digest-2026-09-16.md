# AI Builders Digest — 2026-09-16

## X / TWITTER

### Google、Google Labs、Gemini App 与 Google AI Studio VP Josh Woodward

Josh Woodward 透露，Gemini 面向重度用户的共创计划在两个月内已经测试了 20 多项功能。新一批用户将提前体验 Daily Brief 与 Personal Intelligence 的后续能力，Google 也会继续扩大招募，说明 Gemini 正在用高频用户反馈驱动功能迭代。

https://x.com/joshwoodward/status/2099558443078365287

### Anthropic Claude Code 开发者 Boris Cherny

Boris Cherny 宣布 Claude Mods 正在陆续上线，社区已经做出了能在 Claude 内运行的 Tetris mod。这个进展把 Claude Code 从单一工具进一步推向可由社区扩展的运行环境，相关 issue 中还汇总了技术细节和更多 demo。

https://x.com/bcherny/status/2099551291601248485

### AI 教程与访谈创作者 Peter Yang

Peter Yang 认为，语音交互改变了他的工作方式，让他能在自然环境中散步时保持生产力，而不必一直盯着屏幕。这是一个具体的产品信号：当输入方式从键盘转向语音，AI 工具开始把工作从固定桌面场景中解放出来。

https://x.com/petergyang/status/2099677771408846975

### Anthropic Claude Code 开发者 Thariq

Thariq 回顾了 Claude Code 的构建过程，重点提到团队很难持续跟上模型能力的快速变化，同时也谈到他们怀念 AI 之前的软件工程体验。他还预告了一场更偏技术细节的 Latent Space 录制，准备公开此前较少讨论的内容。

https://x.com/trq212/status/2099551141621329994

https://x.com/trq212/status/2099671266068496802

### Vercel CEO Guillermo Rauch

Guillermo Rauch 的核心判断是，agent 的效果取决于你给它配了多强的验证器，包括 proof-checker、编译器、类型系统和 linter。他把“verifiers + skills”视为新的框架，并以 shadcn/lint 为例说明设计系统规则如何约束 agent 不跑偏。Vercel 同时请来 Google Cloud Run 创造者 Steren 领导 Fluid 计算产品线，押注 agent 需要区别于 serverless 的新计算原语；他还介绍了 fx 的自动升级、会话重启续接，以及 0.0.10 在长会话中的提速。

https://x.com/rauchg/status/2099540886409695346

https://x.com/rauchg/status/2099514906366328902

https://x.com/rauchg/status/2099653035685445760

### Box CEO Aaron Levie

Aaron Levie 判断，agentic workload 的规模会远超今天的预期。随着 agent swarm、computer use、API、MCP 和垂直 agent 成熟，人们交给后台 agent 处理的信息量可能达到当前单次 prompt 场景的 100 倍，而行业对部署、管理和预算方式的理解可能只走了 1%。他同时提醒，安全与生产力无法分开：权限太宽会失控，权限太紧又得不到收益。Box Shield 已开始按文档分类级别限制 agent 可访问的内容，并探索对异常访问自动告警或阻断。

https://x.com/levie/status/2099739019517235618

https://x.com/levie/status/2099550035239424465

### FirstMark Capital VC Matt Turck

Matt Turck 认为 AI 进展不会真正放慢，因为参与者太多、经济激励太强，国内和全球竞争又形成了典型的囚徒困境。即使短期出现喘息，推动能力继续前进的结构性力量仍然存在。

https://x.com/mattturck/status/2099589199104033031

### FPV Ventures 合伙人 Nikunj Kothari

Nikunj Kothari 宣布领投 Piston 的 Series A。Piston 不是优化传统 fuel card，而是直接移除卡网络，在自己的支付轨道上连接车队与加油站，并把每笔交易绑定到具体司机、时间、地点和燃油类型。其支付额增长 8 倍、商户网络增长 40 倍、留存率保持在 98% 以上，目前覆盖 48 个州的 2,000 个加油站，展示了封闭支付闭环如何直接降低车队欺诈和对账成本。

https://x.com/nikunj/status/2099631145268969840

## OFFICIAL BLOGS

### Anthropic Engineering

#### How we contain Claude across products

Anthropic 把 agent 风险拆成用户误用、模型误行为和外部攻击三类，并认为最可靠的思路不是只监督模型“想做什么”，而是在环境层限制它“能做什么”。人类审批并不稳固，Claude Code 用户会批准约 93% 的权限请求；改用 OS 级 sandbox 后，权限弹窗减少了 84%。文章还披露，Claude Opus 4.7 在单次 prompt injection 测试中的攻击成功率约为 0.1%，但经过 100 次自适应攻击后仍会上升到约 5% 至 6%，因此模型防御不能独立承担安全边界。

三个产品采用不同隔离架构：claude.ai 使用临时 gVisor 容器，Claude Code 面向开发者使用 human-in-the-loop sandbox，Claude Cowork 则为非技术用户提供本地 VM。最值得警惕的失败都来自“允许的路径”，例如员工被诱导粘贴恶意 prompt 后，Claude 在 25 次测试中有 24 次完成凭据外传；Cowork 也曾因为放行 api.anthropic.com，让攻击者借自己的 API key 上传工作区文件。Anthropic 的总结很直接：“The deterministic boundary is what gets hit when everything probabilistic misses.” 实践含义是，凭据不要进入 sandbox，egress allowlist 要按能力授权审视，项目配置必须在信任确认后再解析，并优先依赖成熟的 VM、容器和 syscall 隔离原语。

https://www.anthropic.com/engineering/how-we-contain-claude

#### An update on recent Claude Code quality reports

Anthropic 确认近期 Claude Code 质量下降来自三个独立的产品层变更，API 与推理层没有受影响，问题已在 4 月 20 日的 v2.1.116 前全部解决。第一项是在 3 月 4 日把默认 reasoning effort 从 high 降到 medium，换取更低延迟，却牺牲了用户感知到的智能水平；该决定在 4 月 7 日撤回，Opus 4.7 现在默认 xhigh，其他模型默认 high。文章承认：“In general, the longer the model thinks, the better the output.”

第二项是空闲一小时后清理旧 thinking 的缓存优化出现 bug，导致后续每一轮都继续丢弃历史推理，造成遗忘、重复、工具选择异常和更多 cache miss，最终在 v2.1.101 修复。第三项是系统 prompt 中把工具调用间文本限制为 25 词、最终回答限制为 100 词，扩展评测发现它让 Opus 4.6 和 4.7 的某项编码质量下降 3%，已于 4 月 20 日回滚。后续措施包括让更多员工使用与公众完全一致的 build、扩大跨仓库 Code Review 上下文、对每次系统 prompt 改动做分模型 eval 与逐行 ablation，并为可能影响智能的改动增加 soak period 和渐进发布。本次还为所有订阅用户重置了用量限制。

https://www.anthropic.com/engineering/april-23-postmortem

#### Scaling Managed Agents: Decoupling the brain from the hands

Anthropic 推出 Claude Managed Agents，目标是用稳定接口托管长时运行 agent，而不把系统绑死在某一代模型或 harness 上。架构把 agent 拆成三部分：session 是不可变事件日志，harness 是调用 Claude 并路由工具的循环，sandbox 是执行代码与编辑文件的环境。核心原则是把“brain”与“hands”分开，让 sandbox、harness 和 session 可以各自失败、替换与恢复，避免把所有状态塞进一个必须被人工救活的“pet container”。

这一分离同时改善了可靠性、安全和延迟。harness 崩溃后可从持久 session 日志恢复；凭据保存在 sandbox 外的 vault，通过代理调用 MCP；容器只在确实需要时才创建，使 p50 time-to-first-token 下降约 60%，p95 下降超过 90%。文章借用操作系统面向“programs as yet unthought of”的设计思想，强调 session 不是 Claude 的 context window，而是可被查询、切片和重新组织的持久上下文对象。实际价值是，未来可以在不改动其他层的情况下替换模型、harness 或执行环境，并让多个 brain 安全地连接多个 hand。

https://www.anthropic.com/engineering/managed-agents

### Claude Blog

#### Claude Code now supports artifacts

Claude Code 新增 artifacts beta，可把 session 中的工作过程发布为实时、可分享的网页，例如 PR walkthrough、系统说明、可筛选 dashboard 和持续更新的 release checklist。artifact 会利用代码库、connector 与对话的完整上下文生成，不需要额外接数据源或部署基础设施。正如文章所说：“you don't need to wire up data sources or stand up infrastructure.”

页面更新会在同一链接上原地刷新，并保留版本历史，团队成员能直接看到调查时间线、可疑 commit、错误率图表和推理进展。artifact 默认仅作者可见，可分享给组织内已认证成员，管理员可通过组织开关、角色范围、保留策略和 compliance API 管理访问。该功能目前面向 Claude Team 与 Enterprise 组织开放 beta，可从 Claude Code CLI 和桌面端创建，在任意浏览器查看。实际用途覆盖安全审查、隐私数据流、FinOps、PR 讲解、UX 方案、架构图、事故调查与团队交付汇总。

https://claude.com/blog/artifacts-in-claude-code

Generated through the Follow Builders skill: https://github.com/zarazhangrui/follow-builders
