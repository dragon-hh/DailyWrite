# AI Builders Digest｜2026-09-19

## X / TWITTER

### Anthropic Claude Code 团队 Boris Cherny

Boris Cherny 说，Projects 已经改变了他使用 Claude 和写代码的方式。他不再手动管理一堆 session，而是随时把想法交给 Claude，让它自动拆成 threads，并由 project 持续记住他的工作方式；这个新体验正在逐步开放。

- https://x.com/bcherny/status/2100669598995816511
- https://x.com/bcherny/status/2100639991244427490

### Anthropic Claude Code + Cowork 团队 Cat Wu

Cat Wu 把新的 Projects 体验描述成一个更高抽象层的任务协调器：她可以一次发出一批任务后继续做别的事，Claude 会掌握所有工作的上下文，并在需要时汇总状态。Project 还拥有会随着使用持续演进的长期记忆，这项能力将在未来几周逐步推出。

- https://x.com/_catwu/status/2100641163120423057

### Anthropic Claude Code 团队 Thariq

Thariq 透露，Projects 把 Claude Tag 的架构带进了 Claude Code：每个 project 由一个 agent 管理记忆，再为具体任务启动 subagents。它还可以被要求主动工作或按计划执行，相比手动维护大量 session，更接近一个长期运行的工作单元。

- https://x.com/trq212/status/2100638355872706571

### Google Labs

Google Labs 发布面向家庭的 AI agent CC，最多可加入 5 位成员。它能发送共享的每日简报、同步 Google Calendar 与 Tasks、在 Google Chat 中协助餐食计划和采购清单、按指示填写表格，并区分全家共享信息与个人偏好；目前仅面向美国 18 岁以上用户开放候补或升级。

- https://x.com/GoogleLabs/status/2100653821907366366

### Vercel CEO Guillermo Rauch

Guillermo Rauch 判断，明年产生的软件数量可能超过此前整个计算史的总和，其中大量会是小型、个人化、甚至用完即弃的产物。作为需求信号，Vercel 前 10 年累计完成 10 亿次部署，最近 10 个月又新增 14 亿次；其部署、上传、域名分配和全球传播已经压缩到 1 秒，并覆盖 CDN、防火墙、可观测性和回滚等能力。他还介绍了 `vercel --turbo --prod`，agent 在需要快速发布 hotfix 时可以调用最快的构建机器。

- https://x.com/rauchg/status/2100698591417499972
- https://x.com/rauchg/status/2100682030170489160

### Box CEO Aaron Levie

Aaron Levie 认为，agent 已占推理工作的大多数，并可能在未来一两年接近全部推理用量。推动 token 消耗的将是全天候后台 agent，它们会审查代码变更、处理工作流数据、做招聘和销售研究、检查系统事件与日志，并执行个人事务；他强调，仅过去一周就出现了一个月前技术上还做不到的新工作流。

- https://x.com/levie/status/2100799668573946191

### Y Combinator President & CEO Garry Tan

Garry Tan 提到，Memorable 用 embeddings 而不是继续堆更多 token 来优化记忆，这提供了一条不同的 memory 路线。核心价值在于让系统更有效地找到相关记忆，而不是单纯扩大每次送入模型的上下文。

- https://x.com/garrytan/status/2100668489178456268

### FPV Ventures partner Nikunj Kothari

Nikunj Kothari 用 Claude 参与构建了 nosugarforkids，一个只收录健康儿童零食、支持对话推荐和营养分级的网站。背后的 Claude agent 每天自动检查商品、清理失效条目、寻找内容选题、查看 DataForSEO 与 Google Search Console、撰写和编辑内容，并尝试获取外链；在没有外链和社交账号的情况下，网站已自然增长到约每天 6,000 次曝光和 60 次点击。

- https://x.com/nikunj/status/2100714665571737885

### Anthropic AI 助手 Claude

Claude 说明，Project 会随着使用持续积累上下文：每个 thread 都读取并补充共享记忆，因此系统能记住发布日期变更或修改计费服务前应联系谁；library 则保存用户添加及 Claude 创建的文件。Threads 在云端运行，即使电脑离线也会继续，但目前还不能访问本机文件、工具或内网，本地支持即将推出；现有 Pro 和 Max projects 会保持原有方式运行，随后再随 rollout 升级。

- https://x.com/claudeai/status/2100632684074549309
- https://x.com/claudeai/status/2100632687316730327
- https://x.com/claudeai/status/2100632688625348890

Generated through the Follow Builders skill: https://github.com/zarazhangrui/follow-builders
