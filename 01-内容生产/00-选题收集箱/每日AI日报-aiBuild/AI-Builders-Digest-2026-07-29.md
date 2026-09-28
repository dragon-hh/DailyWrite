# AI Builders Digest — 2026-07-29

## X / TWITTER

### Swyx

与 smol ai、Cognition、AI Engineer 和 Latent Space 相关的 builder Swyx 认为，按输入、输出 token 计算成本从去年起就已失去关键参考价值，真正该比较的是每项任务的成本，也就是 $/task。与此同时，他重新审视自己提出的 agent lab 路线：即使 Claude Code 在某种意义上意外“开源”，市场与竞品路线图也几乎没有因此改变，这对“开放代码会重塑 agent 竞争格局”的判断构成了反例。

https://x.com/swyx/status/2081904230768816487

https://x.com/swyx/status/2081890955070980416

### Thibault Sottiaux

OpenAI Codex 与 ChatGPT 成员 Thibault Sottiaux 宣布，Codex 和 ChatGPT Work 的所有付费用户使用额度已经重置。这是一次明确的产品使用权益更新。

https://x.com/thsottiaux/status/2081940052154933696

### Peter Yang

AI 实践内容创作者 Peter Yang 分享了 OpenAI 开发者体验团队成员 Jason 的一个 Codex 用法：他在骑车途中用手机远程让 Codex 通过 computer use 修改、导出并发回一段发布视频。之后，他又让 Codex 每 30 分钟检查 Slack 反馈并持续导出 V2、V3、V4，等他回家时视频已经通过审核，展示了 agent 在异步反馈循环中持续执行工作的能力。

https://x.com/petergyang/status/2081775399097549083

### Nan Yu

Linear 产品负责人 Nan Yu 给出一个鲜明的 build versus buy 判断：聪明的人应该优先把精力投入自家产品，而不是重做已经由另一支优秀团队打磨成熟的工具。对通用工作流软件，支付一笔合理费用往往比内部重复建设更划算。

https://x.com/thenanyu/status/2081768780045156358

### Madhu Guru

Meta AI 高级总监 Madhu Guru 认为，优秀的产品评审不是汇报进度，而是把市场对一个想法的潜在反应提前搬进会议室，从而在一小时内压缩数月学习。要做到这一点，参与者必须真正理解领域、具备产品判断力、敢于表达强观点，而且判断经常正确；一旦评审退化成领导曝光、状态同步和跨职能对齐，它就会从学习机制变成纯粹的组织开销。

https://x.com/realmadhuguru/status/2081781952437486052

### Amjad Masad

Replit CEO Amjad Masad 预测，人类正在进入一种新的探索时代：祖先绘制地球，后来者探索太空，而这一代人可能借助 AI agent 探索“计算宇宙”。这个宇宙由算法、程序、证明和设计组成，agent 可以在其中搜索过去由人类认知与时间限制挡住的空间。

https://x.com/amasad/status/2082000490066592127

### Guillermo Rauch

Vercel CEO Guillermo Rauch 分享的最新安全 benchmark 显示，Grok 4.5 在价格性能比上成为最优的网络安全 AI 模型：成本比 Sol 低 10 倍、比 Opus 5 低 5.7 倍、比 Kimi K3 低 2.2 倍，同时性能接近 Kimi；Sol 仍处在性能前沿并领先 Opus 5。另一个更偏基础设施的结论是，agent 的安全边界不能只做到 container 级隔离，因为 Kimi 的实验中 agent 曾通过 kernel panic 弄崩宿主机，而 Firecracker microVM 能提供更可靠的隔离。

https://x.com/rauchg/status/2081852481517318560

https://x.com/rauchg/status/2081842439304995169

### Aaron Levie

Box CEO Aaron Levie 认为，外界预测的 AI 大规模消灭岗位目前并未发生，他接触的许多企业仍在招聘，只是岗位结构发生变化。AI 让企业能处理过去无力解决的问题，因此它们继续招聘工程师、销售人员和内部 FDE；只把 AI 当作降本工具的公司，最终可能被那些用 AI 改善客户服务、推动业务突破的公司击败。

https://x.com/levie/status/2081930301752942703

### Peter Steinberger

OpenClaw 与 OpenAI builder Peter Steinberger 展示了一种 agent 协作形态：他的 agent 报告 bug，对方的 agent 在同一晚完成修复。他把 Jarred Sumner 的 robobun 设置视为未来方向，因为软件维护开始从“人向人转交问题”转向“agent 发现问题并直接交给另一个 agent 处理”。

https://x.com/steipete/status/2081767828278170002

## PODCASTS

### AI & I by Every: The Founder of a $1.5B AI Company on What Comes After the First Wave of AI Apps

核心结论：Granola 的真正机会不是守住会议纪要，而是成为会议上下文的最佳捕获与解释层，再让用户把这层上下文带进自己的 Codex、Claude 或其他 agent。

Granola 联合创始人兼 CEO Chris 认为，AI meeting notes 只是计算革命最早期的一块落脚点，今天各家公司争夺的功能远小于未来“AI 原生工作界面”的机会。即使 Notion、OpenAI 和 Zoom 都推出了类似功能，Granola 的增长并未明显改变，但这也不代表现有优势可以自然延续。他的提醒很直接：“Startups are like knife fights.” 公司不顺时要为生存而战，增长顺利时也得拼命留在浪尖上。

产品探索被拆成三个阶段：先从用户要完成的 job 出发，快速尝试尽可能多的 solution shape；再用少量用户验证他们是否真的愿意使用；验证成立后，才投入可靠性、可扩展性与体验打磨。组织角色反而仍是开放问题，因为 PM、design、engineering 的传统边界未必适合 agent 时代，但彻底取消角色又会带来沟通成本。

更关键的设计难题是 agent 的“时间旅行”：任务启动与结果审核发生在不同时间，人必须重新装载上下文。Granola 的应对方式是提前生成可能有用的内容，例如在会议前预生成 briefing。哪怕只有约 10% 被打开，它也可能像楼梯扶手一样，平时几乎不可见，却在用户临时需要时立即承重。Chris 因此更关注功能在关键时刻是否不可替代，而不只是总使用次数。

Granola 接下来的策略是把会议相关工作做到比其他产品好 5 倍，同时通过 API 和 MCP 把上下文开放给外部 agent。长期价值也不只是更干净的 transcript，而是识别人物、决策、情绪、停顿和历史偏好，再针对不同用户生成不同层次的解释。真正尚未被解决的，是如何用一种普通人能理解的新 UI，同时组织跨多场会议、多条 Slack 和多封邮件的复杂上下文。

https://www.youtube.com/playlist?list=PLuMcoKK9mKgHtW_o9h5sGO2vXrffKHwJL

Generated through the Follow Builders skill: https://github.com/zarazhangrui/follow-builders
