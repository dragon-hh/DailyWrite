# AI Builders Digest — 2026-09-25

## X / TWITTER

### Swyx

Swyx 将 Claude Opus 5.5 与 6 Sol 并排用于 Latent Space 的 AI News 后，认为两者差距非常明显。Opus 5.5 的报道更简洁、更有品味，AI 味更少，因此将成为 AI News 的默认模型。

https://x.com/swyx/status/2102650014552182920

### Anthropic Claude Code 团队 Boris Cherny

Boris Cherny 解释了 Claude 查找复杂代码缺陷的一种工作方式：先为棘手的状态机或易发生竞态的部分建立模型，再寻找反例、复现问题并修复代码。这不是对整个代码库做形式化验证，而是把建模和反例检查集中到最危险的局部。

https://x.com/bcherny/status/2102898067133595992

他还分享了 Claude 网页版和桌面端近期提速背后的工程实践，提醒正在优化自家应用响应速度的工程师关注相关技术细节。

https://x.com/bcherny/status/2102854267782705648

### OpenAI Codex 与 ChatGPT 团队 Thibault Sottiaux

Thibault Sottiaux 已经把 Voice 当成日常工作入口：直接与 ChatGPT 通话，处理邮件、写代码和管理日历，并让语音能力贯穿包括第三方插件在内的完整生态。这展示了语音交互正在从单次问答，转向跨工具的工作编排界面。

https://x.com/thsottiaux/status/2102814202117411196

### AI 教程创作者 Peter Yang

Peter Yang 认为 Claude Opus 5.5 同时具备聪明、快速、好交流、写作好和限额友好等特点，但产品体验仍取决于 harness。他的判断是，目前一家实验室拥有更强的模型，另一家拥有更好的 harness，Claude Code 尤其需要更成熟的实时语音、浏览器和 computer use 能力。

https://x.com/petergyang/status/2102946952740741394

https://x.com/petergyang/status/2102952201350254667

### Meta AI 高级总监 Madhu Guru

Madhu Guru 反驳了“消费者总想亲自完成任务”的单一假设。他指出，同一个人可能享受逛衣服，却厌恶找屋顶维修商时的搜索、电话沟通、保险协调、比价与排期；真正有价值的 agent 应该识别这种差异，在适合的任务里把摩擦降到接近零，而不是统一替代所有体验。

https://x.com/realmadhuguru/status/2102777931764498536

### Anthropic Claude Code 团队 Thariq

Thariq 拆穿了“Claude 一次生成”的表面叙事：所谓 one-shot 背后，往往是一份上万字符、包含清晰判断、skills、示例和 API keys 的精心 prompt。结果看似一步完成，真正的工作却提前发生在上下文和工具准备上。

https://x.com/trq212/status/2102870353781641416

他还表示，团队正在尝试一种新型技术文章，公开可复用的具体 prompts 与工作方法，而不只展示最终结果。

https://x.com/trq212/status/2102857025206255902

### Replit CEO Amjad Masad

Amjad Masad 认为，年轻人最重要的价值是打破范式、质疑根深蒂固的观念并尝试不可能之事，理想的大学应该专门培养这些能力。这个判断把教育的重点从传递既有答案，转向形成挑战既有系统的勇气与能力。

https://x.com/amasad/status/2102799031038878172

### Vercel CEO Guillermo Rauch

Guillermo Rauch 把成熟 agent 拆成三个部分：作为大脑的模型与 harness，作为双手的工具、浏览器与计算机，以及承载记忆、skills 和代码仓库的文件。把三者塞进一台持续运行的机器最简单，但云端要兼顾成本、安全与审计，就需要将计算、工具和存储解耦；Vercel 推出的 Drives 正是可按需挂载的 agent 外部磁盘。

https://x.com/rauchg/status/2102820148629614685

他还用 ShellPerfBench 展示了一个很小但实用的优化场景：Opus 5.5 找到了其他模型遗漏的 shell 启动优化，用户可以让 agent 检查 `.zshrc` 等配置，减少每次打开终端时被忽略的等待。

https://x.com/rauchg/status/2102947745132924993

### Box CEO Aaron Levie

Aaron Levie 认为，AI 降低制作门槛和成本后，影视作品会变多，工作室也能承担更多创作风险。就像声音、彩色和计算机动画曾扩展电影边界一样，新工具不会消灭创意与品味，反而会让更多人用这些能力探索新的叙事形式。

https://x.com/levie/status/2102934874470617303

### Cursor、Notion 与 Stripe 前设计师 Ryo Lu

Ryo Lu 警告，AI 最大的危险未必是让人懒惰，而是让人永远忙碌：在找到意图和品味之前，就获得无限生产与执行能力。他主张真正的前沿应是辨别力，知道什么不该做、何时停止，让工具为人腾出生活、想象力和自由，而不是把生活本身变成生产工具。

https://x.com/ryolu_/status/2102933485795369213

### Y Combinator 总裁兼 CEO Garry Tan

Garry Tan 提出创业公司获客正在同时发生两种变化：一方面要让 software agents 主动想要并选择你的产品，另一方面要使用 agents 帮助真实用户产生购买意愿。AI 因此既改变了客户是谁，也改变了销售和营销的执行方式。

https://x.com/garrytan/status/2102955139875397806

### South Park Commons 合伙人 Aditya Agarwal

Aditya Agarwal 认为，判断团队时只看人数是常见错误，成员共同工作的年限更能解释产出与韧性。一个协作超过三年的团队，往往比刚组建的同规模团队吞吐更高、更稳定，因此投资者和求职者都应该关注团队的长期共事面积，而不是静态 headcount。

https://x.com/adityaag/status/2102782451643040074

### Anthropic 的 AI 助手 Claude

Claude 宣布上线 Claude Marketplace，用户可以发现并添加 Slack、Notion 等 connectors 和 plugins，购买 Cursor、CrowdStrike 等公司的 agents 与产品，也可以寻找 Accenture、Deloitte 等服务伙伴。这个市场把工具接入、agent 产品和企业实施服务放进了同一个发现入口。

https://x.com/claudeai/status/2102840851538080172

## 官方博客

### Anthropic Engineering

#### How we contain Claude across products

Anthropic 认为，agent 越强、权限越大，理论上的爆炸半径就越大，安全设计的重点因此不能只靠人工逐次审批。其遥测显示用户大约会批准 93% 的权限请求，频繁弹窗会带来审批疲劳；更可靠的方向是用 sandbox、VM、文件系统边界与网络出口控制，直接限制 agent 能接触什么。文章把风险分为用户误用、模型误行为和外部攻击，并强调环境、模型与外部内容三层防线必须重叠，尤其要让凭证从一开始就不进入不可信执行环境。

https://www.anthropic.com/engineering/how-we-contain-claude

#### An update on recent Claude Code quality reports

Anthropic 将近期 Claude Code 质量下降追溯到三个彼此独立的产品层变更，而非 API 或推理层退化：默认 reasoning effort 从 high 降到 medium、闲置会话清理 thinking history 的 bug，以及限制输出长度的 system prompt。三个问题分别造成模型显得变笨、遗忘重复和编码质量下降，并已在 4 月 20 日的 v2.1.116 前全部修复。后续改进包括让更多员工使用与用户相同的公开版本、扩大逐模型 eval 与 ablation、增加 soak period 和渐进发布，并强化 system prompt 变更审计。

https://www.anthropic.com/engineering/april-23-postmortem

#### Scaling Managed Agents: Decoupling the brain from the hands

Anthropic 的 Managed Agents 将长期运行 agent 拆成三个可替换接口：记录完整事件的 session、负责调用模型和路由工具的 harness，以及执行代码和编辑文件的 sandbox。把“脑”“手”和持久会话解耦后，容器或 harness 都能在故障后替换，凭证也可以留在 sandbox 之外；session log 则成为独立于 context window 的可恢复上下文。该架构让无需 sandbox 的任务不再等待容器启动，使 p50 TTFT 下降约 60%，p95 下降超过 90%，并支持一个大脑连接多个执行环境。

https://www.anthropic.com/engineering/managed-agents

Generated through the Follow Builders skill: https://github.com/zarazhangrui/follow-builders
