# AI Builders Digest - 2026-09-03

## X / TWITTER

### Anthropic Claude Code 团队 Boris Cherny

Boris Cherny 介绍了 Fable 5.1 的三项直接改进：写作语气更自然，团队正继续减少典型的“Claude 味”；生物安全机制对正常请求的误触发下降约 85%，Claude Code 每次会话中的网络安全干预预计减少约 60%；企业、API 与 SDK 客户的价格也降低了，缓存读取从每百万 token 1 美元降至 0.25 美元，典型 Claude Code 会话最高可便宜 38%。这组更新的共同方向很清楚：模型能力之外，成本、误拦截和表达体验正在同时成为产品竞争力。

- 写作语气更新：https://x.com/bcherny/status/2094864064648536068
- 安全机制误触发下降：https://x.com/bcherny/status/2094864063478276288
- 价格与缓存读取成本：https://x.com/bcherny/status/2094864062186426373

### AI 教程创作者 Peter Yang

Peter Yang 建议不要囤积大量 AI skills，而应只保留真正使用的少量能力，并尽量把每个 skill 写短。他也指出一种常见风险：根据单次失败让 AI 反向修改 skill，很容易对当前对话过拟合，长期积累后会让规则漂移。针对 Fable 5.1，他推荐用 `/claude-api prompt-audit` 清理旧 skill 中的冗余规则，但修改仍应经过人工审核。

- 精简并定期删除不用的 skills：https://x.com/petergyang/status/2094999358525821099
- 单次迭代导致 skill 过拟合的问题：https://x.com/petergyang/status/2094995775952740795
- 使用 prompt-audit 审计旧规则：https://x.com/petergyang/status/2094987791566622971

### OpenAI 产品人员 Nan Yu

Nan Yu 认为，agent 的重要机会不只是能力更强，而是“没那么烦人”。用户必须先愿意持续使用，才能真正获得价值；如果交互让人频繁愤怒退出，再强的能力也无法转化为产品价值。他进一步判断，UX 设计师可以向对话设计和修辞设计延伸，把措辞、节奏与边界感当成 agent 体验的核心组件。

- “减少烦人感”是 agent 的产品机会：https://x.com/thenanyu/status/2094928205753040999

### Meta AI 高级总监 Madhu Guru

Madhu Guru 认为，企业应建立自己的 post-training 系统、评测体系和数据飞轮，而不是只消费通用模型能力。他把“自我改进产品”拆成五块基础设施：清晰的主指标、次指标与护栏指标；明确的战略和路线图；历史产品决策知识库；对内部 dashboard、API、MCP 和工具的连接；以及理解端到端产品开发流程的 harness。复杂度不高的团队可以先用轻量版本验证，再复用现有软件工程 agent 扩展。

- 企业自建 post-training 与数据飞轮：https://x.com/realmadhuguru/status/2094973690576576675
- 自我改进产品的五块基础设施：https://x.com/realmadhuguru/status/2094817857821704659

### Anthropic Claude Code 团队 Thariq

Thariq 对 Fable 5.1 的实用建议是，不需要大量核验、边界情况较少的任务可以先用较低 reasoning effort，以换取更合适的成本和速度。现在切换 effort 不再破坏 prompt cache，这让同一工作流按任务风险动态调整推理强度变得更可行。

- reasoning effort 与 prompt cache 建议：https://x.com/trq212/status/2094945951865520458

### Vercel CEO Guillermo Rauch

Guillermo Rauch 宣布 Vercel 将支持 Tanner Linsley 团队及其 React、开源和 Web 生态工作，并承诺同时为 Next.js 与 TanStack 用户提供高质量服务。Fable 5.1 也已接入 Vercel AI Gateway。更长期的技术方向是 Fluid：把 Build、Sandbox、Function 与 Server 统一到共享 Dockerfile、安全边界、网络和文件系统之上，让构建性能、并发可靠性、长时 Function 和 agent 防逃逸能力共享同一套计算底座。

- Vercel 与 Tanner Linsley 团队合作：https://x.com/rauchg/status/2094901483414372716
- Fable 5.1 接入 Vercel AI Gateway：https://x.com/rauchg/status/2094867652573528074
- Fluid 统一计算平台构想：https://x.com/rauchg/status/2094831747037085978

### Anthropic 研究员 Alex Albert

Alex Albert 重点介绍了 Enterprise Frontier Safeguards。传统 zero data retention 难以跨会话识别 agent 在企业内部系统中的风险模式，而 EFS 让数据留在企业自己的云中，同时增加自动监控层，由企业团队接收风险信号；他判断这类可观测性与风险缓解能力会成为企业部署强大 agent 的标准要求。他还展示了 Fable 5.1 通过代码和 headless Blender，从一张地块图片完成住宅设计、渲染与电影感漫游视频，体现模型把视觉任务拆成可执行工具链的能力。

- Enterprise Frontier Safeguards：https://x.com/alexalbert__/status/2094889286990446769
- 通过代码生成建筑漫游视频：https://x.com/alexalbert__/status/2094860187743986169

### Box CEO Aaron Levie

Aaron Levie 判断，AI 网络安全正在快速走向垂直化：模型越来越擅长发现和利用漏洞，而企业本来就已被海量安全发现淹没，未来只能依靠更多 AI 做分流和自动修复，再配合人工监督。他还披露 Box 的企业任务评测结果：Fable 5.1 相比 Fable 5 总体提升 7 个百分点，金融服务任务提升 17%，技术任务提升 37%，公共部门任务提升 16%；优势主要来自识别歧义、正确安排计算顺序，以及避免早期小错误级联放大。

- AI 网络安全的垂直化趋势：https://x.com/levie/status/2095024699441119612
- Box 企业任务评测结果：https://x.com/levie/status/2094851976769257770

### FPV Ventures 合伙人 Nikunj Kothari

Nikunj Kothari 认为 WebMCP 仍被严重低估。它让网站原生向 agent 提供 tool calls，并保留完整 UI、交互元素和人类编辑；他的 El Niño 追踪器 demo 中，agent 可以自行生成视图、保留人工修改并创建可分享链接。这意味着网站不再只给人类浏览，也能成为 agent 可操作、可协作的应用表面。

- WebMCP 与 El Niño 追踪器 demo：https://x.com/nikunj/status/2094922789128196314

### OpenAI CEO Sam Altman

Sam Altman 表示，OpenAI 整个夏天都在集中推进安全优先事项，并将很快发布下一款模型 Astra。Astra 已完成训练，在能力和 alignment 上都有显著提升，但团队认为当前阶段需要更谨慎，因此后续模型会在必要时放慢进度，以留出足够的安全和 alignment 工作时间。他的核心判断是，没人完全理解高能力 AI 的后果，最可行的路径是让社会与技术在持续迭代中共同演进，而不是把能力发展和安全治理割裂开来。

- Astra、能力进展与安全节奏：https://x.com/sama/status/2094934592062959832

### Anthropic AI 助手 Claude

Claude 官方宣布 Fable 5.1 已全面上线，面向网络防御和生命科学的 Claude Mythos 5.1 则通过受信任访问计划提供。新版本把网络安全正常请求的误报减少约 60%，基础生物与医疗问题的 fallback 率降低约 85%。同时推出的 Enterprise Frontier Safeguards 会从今年秋季开始分阶段落地，在保持与 zero data retention 相同隐私水平的同时，帮助企业防范对 agent 的恶意使用。

- Fable 5.1 与 Claude Mythos 5.1：https://x.com/claudeai/status/2094848592812917122
- 网络安全与生物医疗 safeguards 改进：https://x.com/claudeai/status/2094848591617483020
- Enterprise Frontier Safeguards 上线计划：https://x.com/claudeai/status/2094848590245965931

Generated through the Follow Builders skill: https://github.com/zarazhangrui/follow-builders
