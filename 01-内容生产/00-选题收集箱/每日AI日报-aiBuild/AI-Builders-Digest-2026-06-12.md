AI Builders Digest — 2026-06-12

# AI Builders Digest — 2026年6月12日

## 今日要点

- **Anthropic 的 Mike Krieger 深度分享**：Instagram 联合创始人、现任 Anthropic Labs 负责人，揭秘他日常使用 Claude Fable 5 的真实体验——从"新手感"到将 AI 当作真正的队友托付复杂任务
- **OpenAI Codex 消费激增**：Thibault Sottiaux 确认过去 48 小时 Codex 的 token 消费量出现 unusually strong spike，企业采用加速
- **Fable 5 成为开发者新宠**：从 Replit 的 Amjad Masad 到 Every 的 Dan Shipper，顶级 builder 们都在分享用 Fable 构建项目的惊人体验
- **Google Project Genie 扩大开放**：Google Labs 宣布向 AI Ultra 5X 订阅者开放更多 Genie 访问权限

---

## 播客 · Podcasts

### AI & I by Every：Anthropic 如何使用 Claude Fable 5 —— Mike Krieger 专访

🔗 https://www.youtube.com/watch?v=XWpTgCvgYaE

Instagram 联合创始人、现任 Anthropic Labs 负责人的 Mike Krieger 做客 AI & I 播客，分享了他从"CPO 转回 builder 模式"后使用 Claude Fable 5 的深度体验。以下是核心要点：

**1. 从"新手感"到重新学习如何与 AI 协作**

Krieger 坦言，第一次使用 Fable 时，他感觉自己"像个 total newbie"——过去熟悉的 prompt 方式和任务分解思路都过时了。现在的关键不再是"一步一步指令"，而是更完整地表达意图，让模型理解全局上下文。

**2. Fable 已经成为他的"队友"**

Krieger 描述了一个典型场景：晚上给 Claude 布置一个复杂任务（如 monoclast 项目），然后去睡觉。凌晨两点醒来时，任务通常已经完成。即使遇到远程服务宕机，Claude 也会自己搭建 scaffolded backend、记录问题、等服务恢复后自动修复。这种"complete the swing"的能力让他重新思考"与 AI 一起 productive"意味着什么。

**3. 工作流演变：从单线程到多并发会话**

他现在的日常是：先用 Fable 进行架构规划对话，让 AI 把讨论整理成 HTML 页面或图表，方便与团队对齐。然后同时开启多个 Claude 会话处理不同任务——有时是一个长期运行的 Cloud Code 主线程，让子 agent 在后台 fork 执行；有时是五六个并行标签页处理不同模块。

**4. 关于模型选择的产品思考**

Krieger 透露自己上周把 iOS 应用默认模型切回了 Sonnet——因为"用 Fable 回答简单问题就像用火箭筒打蚊子"。他认为未来产品形态需要更自动化的模型选择：不同场景（移动端快速问答 vs 桌面端深度编码）应该自动匹配不同模型，而不是让用户手动选择。

**5. 周末项目：自修改的媒体追踪应用**

他展示了自己用 Fable 一个周末构建的个人媒体追踪应用（电影、游戏、TV show）。核心亮点是"agent-native architecture"——不仅可以通过对话让 Claude 添加内容，还能长按聊天按钮让 AI 直接修改应用本身。通过 Vercel live preview 实时预览 diff，甚至能直接在 iOS 设备上 live reload。从想法到可迭代的产品，这个流程让他感受到了"意图与执行之间的 gap"正在消失。

**6. 软件工程的未来**

当被问及"软件工程是否终结"时，Krieger 认为：**传统意义上的软件工程（大量时间写代码、调试、部署）确实在剧变**，但"软件生产"本身——理解需求、做出判断、承担责任——仍然是非常 human 的 endeavor。他观察到很多优秀工程师既有"失去写代码乐趣"的 sadness，也有"能同时做 insane 多倍工作"的 excitement。两者同时存在是正常的。

**7. 信任与验证**

Krieger 强调，即使有 Fable 级别的自主能力，验证仍然至关重要。他现在的做法是：每个 PR 都附带 screenshot gallery，Claude 运行真实 staging 账号的完整 flow（不是 mock 数据），用视频录制检查动画 jank 等时序问题。他特别提到：在会议中有人会突然问"这个 PR 里你做了 X 还是 Y？"——然后对方会 pause 一下说"我不确定，让我 forward 去确认"。这种"不完全理解就 merge"的 norm 需要被修正。

**8. Bug 闭环的新高度**

通过 Slack MCP，Claude 可以拉取 bug 反馈线程，自动修复后**以 Mike 的身份回复**"Hey, this is Mike's Claude, I fixed it. Here's the PR."——但更重要的是，它会接着说"Hold tight, it's not in production yet. I'll follow up when it deploys."几小时后自动跟进确认。这种 long-horizon follow-through 是前所未有的。

---

## X/Twitter 动态

### Box CEO Aaron Levie

🔗 https://x.com/levie/status/2064922814688481678

Fable 在编码及相关任务上的能力飞跃有大量证据。它也在那些需要**长时思考、深度推理、非确定性问题求解**的任务上表现出色。AI 能力的跃升路径正在从"快思考"扩展到"慢思考"。

---

### OpenAI · Thibault Sottiaux (Codex & ChatGPT)

🔗 https://x.com/thsottiaux/status/2064911328087810308

确认过去 48 小时 Codex 的 token 消费出现 unusually strong growth spike。企业开发者的采用正在加速。

🔗 https://x.com/thsottiaux/status/2064900105032135010

"Simplify until there is nothing to simplify"——分享设计哲学。

🔗 https://x.com/thsottiaux/status/2064869401359417799

欢迎 Clint 和 Michael 加入团队，为 cyberspace 做出贡献。

---

### Replit CEO Amjad Masad

🔗 https://x.com/amasad/status/2064864439275536495

发布教程：用 Replit 自动化你的求职搜索。

🔗 https://x.com/amasad/status/2064864076430504282

🎉🎉🎉 庆祝时刻（配图暗示重大发布或里程碑）。

🔗 https://x.com/amasad/status/2064806473352540643

祝贺 Markie Wagner 的企业 agent 新方案上线，认为这是一个非常有趣的 enterprise agents 探索方向。

---

### Vercel CEO Guillermo Rauch

🔗 https://x.com/rauchg/status/2064777495422161205

🎪🎭 伦敦来电！下周 Vercel Ship 大会即将到来，"有一些特别的 announcements"。

🔗 https://x.com/rauchg/status/2064732935484514729

关于硅谷的观察："我喜欢硅谷的一点是，未来是 open for grabs，任何人都可以来 build。"

---

### YC CEO Garry Tan

🔗 https://x.com/garrytan/status/2064947145652994510

Nessie 成为从 ChatGPT、Perplexity 等平台迁移所有上下文、记忆和历史的最佳方式——一键导入所有对话历史。

---

### Every CEO Dan Shipper

🔗 https://x.com/danshipper/status/2064916544417829027

"absolutely insane game"——分享他用 Fable 构建的博尔赫斯《无限图书馆》3D 游戏版本，直接在浏览器中运行，能找到任何一篇 essay。

🔗 https://x.com/danshipper/status/2064777216656097445

引用去年在 Lenny's Podcast 上的预测：个体生产力提升 → 公司需要更少的人 → 对 productivity software 的需求减少。这正在发生。

🔗 https://x.com/danshipper/status/2064767202767602122

"fable maxxing on the plane to SF"——在飞往旧金山的飞机上全力使用 Fable。

---

### Anthropic · Boris Cherny (Claude Code)

🔗 https://x.com/bcherny/status/2064885111477219664

"Hello from Code with Claude Tokyo!!"——Claude Code 东京活动。

---

### Anthropic · Thariq (Claude Code)

🔗 https://x.com/trq212/status/2064826394589442448

发布视频教程：如何用 Fable 编辑自己的 launch video。展示了从剪辑到后期的工作流。

🔗 https://x.com/trq212/status/2064826541947940910

分享视频中的 deck 幻灯片，供观众自行查看。

---

### Linear 产品负责人 Nan Yu

🔗 https://x.com/thenanyu/status/2064733338779177459

分享 "gangprompting"（可能是多人协作 prompting 的新模式或梗）。

🔗 https://x.com/thenanyu/status/2064711789556732316

引用关于"船主定律"：拥有船最好的两天是买船那天和卖船那天——暗示某件新事物的兴奋与后续现实。

---

### Google Labs VP Josh Woodward

🔗 https://x.com/joshwoodward/status/2064869366290841716

Gemini 服务 outage 已恢复，"Update: Everything is back up and running, sorry again!"

🔗 https://x.com/joshwoodward/status/2064762269674918013

此前发布的 outage 通知："Heads up: Gemini is currently experiencing an outage. We're on it."

---

### Google Labs 官方

🔗 https://x.com/GoogleLabs/status/2064801929339752527

🧞 Project Genie 访问权限进一步扩展！即日起向 Google AI Ultra 5X 订阅者开放更多名额。

---

### Practical AI · Peter Yang

🔗 https://x.com/petergyang/status/2064799855059616172

"Give yourself permission to build."——传统职业阶梯把所有人都推向 leader，但做 builder 本身就是一种正当选择。

🔗 https://x.com/petergyang/status/2064760792684335133

"This shit is actually working unbelievable"——表达用 AI 构建某物时的震撼。

🔗 https://x.com/petergyang/status/2064748427892945313

"用 Codex 越多，我的请求越 ambitious。或者这还不够 ambitious？"——展示 Codex 构建的复杂项目截图。

---

### Zara Zhang (Follow Builders 作者)

🔗 https://x.com/zarazhangrui/status/2064843560248332577

"This is so good"—— increasingly，一个 agency 的输出看起来更像是一文件夹的 agent 文件，而不是传统交付物。

🔗 https://x.com/zarazhangrui/status/2064835289559023958

建议人们为跨职能团队构建 agent/skills。例如设计团队可以有一个"design agent"来处理设计系统、生成变体、做 accessibility check。

🔗 https://x.com/zarazhangrui/status/2064825302359150870

观察：旧金山大多数初创公司都在互相卖产品。当她问创始人目标客户是谁时，答案往往是"其他 AI 初创公司"。

---

### FirstMark VC Matt Turck

🔗 https://x.com/mattturck/status/2064806681612362113

2026 年的 VC 是 brutal grind：从 Davos 开始，Aspen 冻僵，Upfront 打卡，Milken 求生，然后……（对 VC 奔波日历的吐槽）。

---

### Claude 官方

🔗 https://x.com/claudeai/status/2064757539762295177

发布 The Problem Solvers 系列新内容：聚焦用 Claude 解决难题的创始人。

🔗 https://x.com/claudeai/status/2064757537992249734

Michael Truell (Cursor 联合创始人) 的故事：12 岁爱上编程，Cursor 现在是……（被截断，但显然是 Cursor 成功故事）。

🔗 https://x.com/claudeai/status/2064741184547795408

Claude Platform 新功能上线：定时部署和环境变量管理（vaults）。

---

### 其他 Builder 动态

**Nikunj Kothari (FPV Ventures)**：
🔗 https://x.com/nikunj/status/2064901295383990417
"TIL: You can just roast your way into getting some legit coffee at the Cognition office ☕️"——在 Cognition 办公室通过"吐槽"换来了正经咖啡。

**Madhu Guru (前 Google Gemini 产品负责人)**：
🔗 https://x.com/realmadhuguru/status/2064794601320481150
指出企业用户从 Gemini 早期就常常在 quality/cost tradeoff 上犯错——过度优化成本而牺牲质量。

**Swyx (Latent Space)**：
🔗 https://x.com/swyx/status/2064698525917827092
"wooh"——简短兴奋回应（可能是某产品发布或里程碑）。

---

## 趋势总结

1. **Fable 5 正在改变 builder 的工作方式**：从 Aaron Levie 到 Dan Shipper，从 Mike Krieger 的播客到 Thariq 的教程，顶级 builder 们正在形成一个共识——Fable 不是更快的工具，而是需要重新学习如何协作的"队友"。

2. **Codex 企业采用加速**：Thibault Sottiaux 的数据和 Peter Yang 的"越来越 ambitious 的请求"形成呼应，说明企业开发者正在从"试用 AI"转向"依赖 AI 做核心工作"。

3. **Agent-native 架构萌芽**：Mike Krieger 的"自修改应用"和 Zara Zhang 的"agent 文件夹替代 agency 交付物"指向同一个方向——软件正在被重新设计为"可被 agent 消费和修改"的形态。

4. **验证和问责成为新瓶颈**：随着 AI 能完成更多工作，"你真的理解你 merge 了什么吗？"成为核心问题。Krieger 的 screenshot gallery、staging 测试、视频录制验证方法代表了最佳实践方向。

---

Generated through the Follow Builders skill: https://github.com/zarazhangrui/follow-builders
