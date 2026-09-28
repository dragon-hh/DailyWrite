# AI Builders Digest — 2026-09-18

## X / TWITTER

### Claude Code 团队 Boris Cherny

Boris Cherny 认为，Claude Code 已经证明 AI 不只是回答问题，而是可以接下一项工作并交付成品；现在 Claude 正把 chat 与 Cowork 合并，让同一个 Claude 在不同任务间延续上下文，并自行判断该快速回答还是进入更深的 agent 工作。与此同时，Claude Docs、Claude Slides 和 Claude Design 已直接进入对话，用户可以在聊天中生成、编辑并导出文档、演示文稿和设计，不再需要先选择一个独立工具。

https://x.com/bcherny/status/2100259951398789487

https://x.com/bcherny/status/2100260544087535639

### AI 实践教程作者 Peter Yang

Peter Yang 分享了自己用 8 个 AI skills 制作整档播客的工作流：从嘉宾研究与采访提纲，到转录稿审阅、开场金句筛选，再到把完整节目编排成 6 种内容资产。即使最新模型能力更强，skills 对他依然不可替代，因为它们把个人的剪辑品味、判断标准和浏览器操作要求固化成了可重复执行的流程。

https://x.com/petergyang/status/2100328939034128856

### Meta AI 高级总监 Madhu Guru

Madhu Guru 提出，安全与 security 应该被视为 AI 产品和模型本身的功能，而不是从外部强加的一圈 guardrails。这个判断把安全从发布前的合规检查，前移成产品设计和模型能力的一部分。

https://x.com/realmadhuguru/status/2100312717739667963

### Anthropic Claude Code 与 Cowork 团队 Cat Wu

Cat Wu 解释了 Claude 合并 Cowork 与 chat 的产品逻辑：用户不想为每项任务先判断该进入哪个 Claude 产品，而模型能力提升后，Claude 已能根据 prompt 自行决定快速回答、深度 agent 工作以及合适的输出形式。Claude Design、Slides 和 Docs 也随之进入同一对话，但用户仍可随时停止、改向或细调 Claude 的投入程度与做法。

https://x.com/_catwu/status/2100260655312089562

### Claude Code 团队 Thariq

Thariq 更新了自己对 agent 工具设计的看法：如果目标只是可靠调用工具，bash 已经不再是唯一答案，直接给 Claude 提供符合任务形态的工具通常更自然，例如需要数据存储时提供数据库 API，而不是绕一层文件系统。bash 与 sandbox 仍适合涉及代码生成和执行的任务；Claude Managed Agents 的可选、可独立启动 sandbox，则在安全隔离和 agent loop 灵活性之间取得了更好的平衡。

https://x.com/trq212/status/2100315535758217422

https://x.com/trq212/status/2100315537251463523

https://x.com/trq212/status/2100315538472009897

### Vercel CEO Guillermo Rauch

Guillermo Rauch 表示，typesafeai 在 Vercel 的 fx 默认模式中用安全审查器分析每条命令，目前审查器运行在 GPT Luna 上。Jev 在 p95 延迟上最高快 18 倍，同时更准确，因此计划进入 Vercel AI Gateway，并很可能成为新的默认选择。

https://x.com/rauchg/status/2100307962262872105

### Box CEO Aaron Levie

Aaron Levie 认为，能够以极低成本和极高速度处理信息的模型，会打开一批此前不在行业雷达上的企业 AI 场景。数据分类、工作流路由、特定领域决策以及安全判断，都是大量业务流程的门槛；更快、更便宜但仍具备足够能力的模型，可能成为企业 agent 工作流的关键基础件。

https://x.com/levie/status/2100448648672993540

### Y Combinator CEO Garry Tan

Garry Tan 强调，个人 AI 不应被某个单一 harness 锁住：无论切换到哪种执行框架，理想状态下都应保留同一套 personality 和完整记忆。这个观点把模型、执行环境与长期身份记忆拆成了可独立演进的层。

https://x.com/garrytan/status/2100339347669279149

### Builder Zara Zhang

Zara Zhang 对 Claude 当前的表达风格提出直接批评：它越来越像是在展示自己的聪明和复杂，而不是把观点清楚传达给用户。她因此减少使用 Claude，这提醒 AI 产品团队，语言风格不是表面体验，而会直接影响用户是否愿意持续使用。

https://x.com/zarazhangrui/status/2100278750776824115

### FPV Ventures 合伙人 Nikunj Kothari

Nikunj Kothari 分享了一个已持续调试数月的 NousResearch 家庭 agent，他和妻子每天在群聊中共同使用它。相比通用机器人，这个 agent 能做到更细粒度的权限与流程控制，例如只读取指定邮件、把内嵌附件转成结构化数据，以及操作已登录的浏览器会话；对家庭场景而言，可控性与共同使用中的失败反馈比单纯对话能力更重要。

https://x.com/nikunj/status/2100212813625196917

### Anthropic AI 助手 Claude

Claude 官方宣布，用户现在可以在同一段对话中制作 decks、docs 和 designs：先在 Claude Docs 起草文档，再用 Claude Slides 生成演示稿，并通过 Claude Design 配套视觉。用户能直接修改文档、在幻灯片上留言或移动元素，随后从 Claude 内演示、导出 PowerPoint 或 PDF，或用一个链接分享；相关能力已在所有付费计划中进入 beta，原有 Cowork 的 chats、projects、artifacts、connectors 和 skills 会继续保留。

https://x.com/claudeai/status/2100258492590207079

https://x.com/claudeai/status/2100258494221812123

https://x.com/claudeai/status/2100258495543071016

## OFFICIAL BLOGS

### Claude Blog

#### Claude Cowork and chat are now one Claude

Claude 正把 Cowork 与 chat 合并成一个统一入口，核心变化不是简单移除标签页，而是让 Claude 根据任务本身决定采用快速问答还是持续运行的 agent 工作。官方对这个产品判断的概括是：“So we stopped making you choose.” 用户原有的 chats、projects、artifacts、connectors 和 skills 会保留，Claude 也可以在用户合上电脑后继续处理被委派的工作。

与此同步推出的 Claude Docs 和 Claude Slides，以及进入对话的 Claude Design，让文档、演示和视觉设计在同一上下文中生成与修改。用户可以直接编辑元素、给 Claude 留评论、从 Claude 内演示，并导出 PowerPoint 或 PDF；产物也能通过一个链接在手机上打开。三项能力目前在付费计划中处于 beta，先向 Pro 和 Max 用户分批推出，Team 和 Free 随后跟进；Enterprise 管理员将至少提前 30 天收到变更通知，并决定何时启用。实际意义是，一份周期性报告可以从数据检索、写作、异常标记一路生成配套的五页汇报材料，并被安排为每周自动运行，同时仍由用户保留最终决定权。

https://claude.com/blog/cowork-is-now-claude

Generated through the Follow Builders skill: https://github.com/zarazhangrui/follow-builders
