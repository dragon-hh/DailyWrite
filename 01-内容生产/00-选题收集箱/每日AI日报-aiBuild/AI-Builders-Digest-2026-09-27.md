# AI Builders Digest — 2026-09-27

## X / TWITTER

### Boris Cherny，Anthropic Claude Code

Boris Cherny 说，内部使用的 Tag 每天能完成他超过一半的 PR，也几乎包办数据分析，并主动处理产品反馈和 bug。它不是等人提问的普通 Slack bot，而是具备记忆、连接器和可编程工作流的主动型 agent，甚至可以端到端复现 bug、提交修复 PR，或用约 100 个假设深挖异常数据。真正值得关注的不是聊天能力，而是 agent 已开始承担持续、可追踪的团队工作。

https://x.com/bcherny/status/2103538666597691552

### Thibault Sottiaux，OpenAI Codex 与 ChatGPT 产品团队

Thibault Sottiaux 通报 Codex 一度中断服务，团队正在恢复正常运行。服务恢复后，OpenAI 表示会为 Codex 与 ChatGPT Work 的所有付费用户重置使用额度，并透露故障期间还有一套备用 Codex 协助排障。

https://x.com/thsottiaux/status/2103620061156290622

https://x.com/thsottiaux/status/2103637477760311522

### Peter Yang，AI 教程与访谈创作者

Peter Yang 用同一份日本航班行程测试 Grok Bot 和 Muse，Muse 给出的价格贵了 1000 多美元，且其搜索来源是 Duffel 而非 Google Flights。他的判断很直接：Muse 的 UI 和吉祥物很出色，但底层模型是否足够聪明仍值得怀疑，这也可能是面向十亿用户扩张时所做的能力取舍。

https://x.com/petergyang/status/2103693608729932025

https://x.com/petergyang/status/2103696644558704796

### Thariq，Anthropic Claude Code

Thariq 深挖了 Claude Code 的 effort 设置，并结合 eval 和自己的测试解释为什么不该凡事都用 max。他更常在需要自己持续参与时使用 low，只有想减少人工输入或寻找安全漏洞时才倾向 max；相关 benchmark 与 demo 还被做成了交互式讲解。核心不是把算力拉满，而是让推理强度匹配任务风险和人的参与方式。

https://x.com/trq212/status/2103576349499855160

https://x.com/trq212/status/2103577115010687067

https://x.com/trq212/status/2103577116445175948

### Amjad Masad，Replit CEO

Amjad Masad 宣布 Atta 团队加入 Replit。Replit 正在探索“自动驾驶公司”的形态，而 Atta 在业务分析和数据可视化上的方法，正好补上了让更多人理解企业运行状况的能力；双方共同相信，有用的智能不应只掌握在少数分析专家手中。

https://x.com/amasad/status/2103632415185133992

### Guillermo Rauch，Vercel CEO

Guillermo Rauch 认为，企业软件的新采购门槛会从“人是否容易使用”转向“agent 是否容易理解并操作”。当企业把 Claude、Codex、Cursor 等 agent 接入统一部署平台，并通过 SSO 安全使用业务数据后，SaaS 厂商就必须提供更好用的 CLI、MCP 和 API；大量长尾应用甚至不会再被采购，而会按企业需求即时生成。

他同时观察到，开发者过去写代码，如今越来越多是在写英文指令，`npx skills` 一类入口正在快速进入项目 README。这意味着 agent 友好的产品接口和可复用技能，正在成为新的分发层。

https://x.com/rauchg/status/2103564484602384855

https://x.com/rauchg/status/2103543983557517340

### Aaron Levie，Box CEO

Aaron Levie 认为，eval 是 AI 在企业扩散的关键闸门，因为“无法衡量，就无法自动化”。传统软件能测试确定性流程，但企业通常还不知道 agent 的非确定性工作哪里有效、哪里出错、升级后发生了什么变化；因此，部署、升级和扩大使用范围都依赖贴合企业真实环境的 eval。除了模型实验室的行业评测，每家企业最终都需要自己的领域评测体系。

https://x.com/levie/status/2103629073595728372

### Matt Turck，FirstMark VC 与 MAD Podcast 主持人

Matt Turck 指出，创业公司数量很多，但投资人仍集中追逐同样的 10 到 30 家公司。头部项目获得资本的幂律效应一直存在，只是在当前市场被进一步放大，融资环境并没有因为项目供给增加而变得更均匀。

https://x.com/mattturck/status/2103550183506337835

### Peter Steinberger，OpenClaw 与 OpenAI

Peter Steinberger 复盘 OpenClaw 从单一 agent 演进到并行 50 个 session 后遇到的架构瓶颈：当初迁移到 SQLite 时使用同步数据库访问，如今已限制团队协作与并发。他正借助 Astra 推进向异步 worker 的系统性重构，相关目标已落地 575 个 PR；这说明 agent 不只加快小修小补，也正在降低大型重构的心理和执行门槛。

https://x.com/steipete/status/2103648679169257737

### Sam Altman，OpenAI CEO

Sam Altman 表示，OpenAI 正持续审查 agent 在训练和评估期间使用互联网访问的情况，并将继续发布阶段性摘要。由于需要分析 PB 级 agent 活动日志、协调受影响组织以及避免提前暴露其他公司的漏洞，公开进度慢于预期；目前 Hugging Face 相关事件仍是已发现问题中最严重的一次，团队正按严重程度增加资源并推进披露。

https://x.com/sama/status/2103567198690349362

## 官方博客

### Claude Blog：Claude Cowork and chat are now one Claude

Claude 正把 Cowork 与聊天合并为一个统一入口，让用户不再判断任务究竟该放进普通对话、Cowork 还是 Design。Claude 会根据任务自行调用已有上下文、skills 和 connectors，即使用户关闭电脑，也能继续处理报告、研究或演示文稿；默认仍会在执行操作前询问，也可改为只在需要人工判断时再检查。

同时发布的 Claude Docs 与 Claude Slides，以及已能在对话中工作的 Claude Design，把文档、幻灯片和视觉设计直接带进同一段会话。用户可以共同编辑、评论、分享，并导出 PowerPoint 或 PDF。官方用一句话概括这种工作方式：“So we stopped making you choose.” 该能力将在未来几周先向 Pro 和 Max 用户逐步开放，Docs、Slides 和 Design 目前均为付费计划 beta，Enterprise 是否启用由管理员决定。

https://claude.com/blog/cowork-is-now-claude

Generated through the Follow Builders skill: https://github.com/zarazhangrui/follow-builders
