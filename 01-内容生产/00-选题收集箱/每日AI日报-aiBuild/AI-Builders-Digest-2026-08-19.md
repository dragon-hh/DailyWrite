# AI Builders Digest：2026-08-19

## X / TWITTER

### AI builder Swyx（关联 smol.ai、Cognition、AI Engineer 与 Latent Space）

Swyx 认为，Trajectory 在雄心与执行品味之间找到了不错的平衡。其 Continual Learning 路线直面剩余的数据难题：GRPO 并不足够，因此团队转向 on-policy 方法，同时处理由此引出的新问题。这是一条来自早期实践者、比泛泛谈论持续学习更具体的技术路径。

原文：<https://x.com/swyx/status/2089393073327653344>

### Google VP Josh Woodward

Josh Woodward 公布了 Gemini 一组直接面向体验的进展：改版后的 Workspace 工具预计一到两周内测试，3.7 Flash 的工具调用已有提升，新版 Projects 已完成设计并进入实现。Gemini 目前支持 49 个 connectors，多个后端与前端事项也已完成或开始推进，同时修复了最严重的过度触发问题。

原文：<https://x.com/joshwoodward/status/2089520767281324112>

### AI 实用教程作者 Peter Yang

Peter Yang 正在测试用 HyperFrames 编辑 YouTube talking-head 开场，包括镜头推进、字幕动画、Logo 和 B-roll。他真正想要的工作方式，是通过与 Codex 或其他 harness 对话完成整套剪辑，而不是在传统时间线上逐项操作。

原文：<https://x.com/petergyang/status/2089519732336787619>

### Meta AI 高级总监 Madhu Guru

Madhu Guru 给出了一条很实用的 evals 学习路线：先选一个自己非常熟悉的 workflow，把质量变成可测量的指标，再研究真实用户的 prompt 序列、每一步的理想响应和端到端结果。随后把产品失败案例做成 traces，例如混乱的工具返回与上下文缺失，并让 eval 能反复自动运行；最后还要持续校准，使它跟得上真实流量中不断变化的用户行为。

原文：<https://x.com/realmadhuguru/status/2089480958571331623>

### Anthropic Claude Code 团队成员 Thariq

Thariq 的判断很大胆：最近的程序生成艺术、视频编辑与 3D 游戏 demo，让他更相信 LLM coding models 在许多创意工作上可能优于 diffusion models。关键优势不是一次生成得多漂亮，而是代码更容易被编辑、微调并导出到现有工具链；Claude Code 的 `/design` 命令正是这一方向的直接入口。

相关原文：

- <https://x.com/trq212/status/2089415712007938315>
- <https://x.com/trq212/status/2089415713098522688>
- <https://x.com/trq212/status/2089529798850969805>

### Replit CEO Amjad Masad

Amjad Masad 指出，真正 AI-native 的团队未必会把“AI”写进宣传语，但能以远少于传统公司的人员规模获得 AI 式增长。与此同时，代码安全不能停在漏洞扫描上，还必须用 penetration testing 主动尝试攻破系统，才能验证防线是否真实有效。

相关原文：

- <https://x.com/amasad/status/2089525819567739264>
- <https://x.com/amasad/status/2089435606338416884>

### Vercel CEO Guillermo Rauch

Guillermo Rauch 宣布，开发者现在可以把代码仓库托管在 Cursor Origin，并从 Cursor Origin 直接部署到 Vercel。这个组合把代码托管与部署链路进一步收拢到 AI coding 工作流中，而 Cursor Origin 本身也托管在 Vercel 上。

原文：<https://x.com/rauchg/status/2089409162270965858>

### Box CEO Aaron Levie

Aaron Levie 认为，“数据是新石油”正在从比喻变成资产事实：AI 对数据的需求如此强烈，以至于几乎任何形式的信息都可能产生价值。企业未来的竞争力，将越来越取决于它能否管理并挖掘组织内部的 intelligence，信息甚至应被视作资产负债表上的资产。

原文：<https://x.com/levie/status/2089499887905997272>

### Y Combinator 总裁兼 CEO Garry Tan

Garry Tan 开源了一套用于构建个人 AGI 的 agent repo，包含 70 个经过验证的 skills，以及一个 Karpathy 风格知识 wiki 的起点。项目采用 MIT License，可直接配合现有 Claude Code 或 Codex 订阅使用；在新目录启动工具并按说明操作，即可快速搭起个人 agent 工作区。

相关原文：

- <https://x.com/garrytan/status/2089438298540519821>
- <https://x.com/garrytan/status/2089425134339961173>
- <https://x.com/garrytan/status/2089424620764168485>

### FPV Ventures 合伙人 Nikunj Kothari

Nikunj Kothari 用一串反讽提醒市场：如果模型、IDE、harness、应用、推理服务、语音层和基础设施都“没有 moat”，那真正稀缺的可能不是技术标签，而是持续建立认知与信任的能力。他进一步预测，brand marketing 会成为未来十年的关键差异化资产，但前提仍是“先有 retention，再谈 attention”；能长期定义公司立场、又能每周把它讲清楚的人，可能从二线岗位走到联合创始人或核心决策席位。

相关原文：

- <https://x.com/nikunj/status/2089486802356961364>
- <https://x.com/nikunj/status/2089374392295842086>

## PODCASTS

### No Priors：Chasing Trillion-Dollar Companies, Founder Ambition, Token Budgets, and Regulatory Capture with Sarah &amp; Elad

**核心结论：AI 的机会依然巨大，但创始人和企业必须同时对增长速度、token 预算与监管代价做更冷静的回报计算。**

Elad Gil 与 Sarah Guo 从“三到五年内还会出现多少家万亿美元公司”谈起。Elad 的反共识判断是，Anthropic、OpenAI 与 SpaceX 在短期内快速跃升，可能更像技术史中的一次爆发期，而不是可线性外推的常态。许多市场当然能诞生千亿美元公司，但万亿美元估值通常需要单家公司支撑 500 亿到 1000 亿美元收入，市场规模与抵达这个规模的速度不能混为一谈。

对创始人而言，退出也不该成为情绪或身份问题。AI 世界一年可能相当于传统周期三到四年，公司应该定期重新审视真实预期、未来稀释、剩余工作年限，以及能力提升和成本下降究竟是在放大还是侵蚀自身价值。Elad 的一句话抓住了代价：“the biggest opportunity cost is your time.” 有些公司应该继续下注，有些则可能已经进入最适合出售的十二到十八个月窗口。

企业内部的下一道管理题是 token 预算。算力成为稀缺资源后，组织会从“所有人都去试 AI”转向衡量 return on invested tokens，把更多算力分配给能产生最高边际结果的人和项目。这并不自动意味着 SaaS 消失，因为把 token 用于核心产品、利润提升或高价值任务，往往比重做低成本 SaaS 更划算。

两人也把这种回报思维延伸到监管：只衡量风险而忽略收益，会让安全要求演变成监管俘获，拖慢能源、医药和 AI 的正面价值。真正困难的选择不是“要不要安全”，而是社会愿意把风险、收益与进步之间的刻度放在哪里。

原视频：<https://www.youtube.com/watch?v=6l8oAO_LBx4>

Generated through the Follow Builders skill: https://github.com/zarazhangrui/follow-builders
