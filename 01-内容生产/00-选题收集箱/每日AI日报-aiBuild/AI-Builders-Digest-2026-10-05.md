# AI Builders Digest - 2026-10-05

## X / TWITTER

### OpenAI Codex 与 ChatGPT 产品 Thibault Sottiaux

Thibault Sottiaux 说，团队接下来只把精力放在四件事上：简化产品、提高效率以支持更多使用、突破性功能，以及新模型。这个取舍来自明确的用户反馈：AI 产品需要变得更简单，而不是继续堆更多开关。[查看原帖](https://x.com/thsottiaux/status/2106610099720720811)

他还用自己的邮件箱做了一个很具体的 agent 实验：让 Codex 自动批量确认并删除无用邮件、按工作类型打标签，再找出待回复邮件并后台检索上下文。结果是他第一次实现 inbox zero，也顺手处理了大量用户反馈。[查看操作结果](https://x.com/thsottiaux/status/2106603980386394123)｜[查看 inbox zero 原帖](https://x.com/thsottiaux/status/2106602729875685780)

### AI 教程创作者 Peter Yang

Peter Yang 注意到，同一社交平台上的 CEO 使用方式差异很大：Google CEO 会亲自使用并回复反馈，而 YouTube CEO 更像把它当公告渠道。这个观察指向一个产品信号，领导者是否直接进入反馈回路，会改变用户对产品团队“是否真的在听”的判断。[查看原帖](https://x.com/petergyang/status/2106505635017986394)

### Meta AI 高级总监 Madhu Guru

Madhu Guru 判断，今天 AI 普及的主要瓶颈已经不是模型，而是产品设计。即使在那 2% 已经为 AI 付费的人群里，使用深度仍然很浅，因为大量产品像有 100 个操纵杆的飞机驾驶舱，用户要面对 connector、权限、模型选择和 token 用量；他预计未来 12 个月，产品团队会让这些体验明显变简单。[查看原帖](https://x.com/realmadhuguru/status/2106450089938157720)

### Vercel CEO Guillermo Rauch

Guillermo Rauch 认为，安全会在软件公司里承担越来越大的职能，它既是“代码是否真的安全”的验证工程，也是“有限 token 应优先检查哪里”的资源分配问题。AI 对手越来越强，让小团队更难获得信任，但全球网络安全的糟糕现状和中心化依赖，也给小团队留下了巨大的颠覆空间。[查看安全观点](https://x.com/rauchg/status/2106516538836856945)

他同时给出一个更激进的长期判断：AI 会让越来越多东西趋近免费，最终的最后一块多米诺骨牌是免费能源。[查看原帖](https://x.com/rauchg/status/2106503460384538793)

### Box CEO Aaron Levie

Aaron Levie 认为，agent 普及正呈现明显的两极分化：编程及其相邻任务已经起飞，其他知识工作仍处在很早期。真正的企业级落地不是加一个聊天框，而是重构工作流、重新连接数据，并补上决策责任、合规、治理和安全机制；正因为这些基础设施尚未完成，他预计 agent 的采用规模仍有 100 倍空间。[查看原帖](https://x.com/levie/status/2106583814709633413)

### 产品设计师 Ryo Lu

Ryo Lu 警告，AI 会让“向平均值收敛”的循环变得几乎没有摩擦：大家复制同样的语言、审美和功能，再用数据奖励这些相似选择，最后产品精致却可以互换。他主张把软件当成表达观点的媒介，AI 提升的是实现速度，但“什么值得存在、为什么必须是这个形状”仍需要创作者用自己的经历、判断和审美回答。[查看原帖](https://x.com/ryolu_/status/2106337039201505453)

### FPV Ventures 合伙人 Nikunj Kothari

Nikunj Kothari 认为，个人 agent 的到来会把平台的创新者困境推到台前：Amazon 需要保护广告现金牛和品牌，而 DoorDash 已开始通过 CLI 谨慎开放文本下单入口。[查看原帖](https://x.com/nikunj/status/2106488814940414455)

他也提醒开发者，不妨短期提高 token 用量来探索边界、寻找真正用途，但单纯为了消耗更多 token 而“tokenmaxxing”并没有价值。[查看原帖](https://x.com/nikunj/status/2106452873513201930)

### OpenClaw 与 OpenAI 的 Peter Steinberger

Peter Steinberger 披露，OpenClaw 的 Android 应用已经卡在 Google 审核流程超过一周。这是一个很具体的平台风险信号：即使 AI 产品迭代速度很快，移动应用分发仍可能被传统审核流程拖住。[查看原帖](https://x.com/steipete/status/2106446147791597774)

### SPC 合伙人 Aditya Agarwal

Aditya Agarwal 指出，财富并不能买到世界顶级医生、律师或创意专业人士的无限时间，一个顶级癌症医生仍可能只给病人 20 到 30 分钟。AI 的特殊之处在于，它同时降低专业能力的获取门槛，并把每个人可获得的服务时间扩展到近乎无限，这就是“智能便宜到无需计量”的实际含义。[查看原帖](https://x.com/adityaag/status/2106503075209044336)

### OpenAI CEO Sam Altman

Sam Altman 明确警惕把宗教力量投射给 AI 模型，或把人类判断交给模型。他认为，这种对 AI 的精神化和判断权让渡本身就是一个真实的安全问题。[查看原帖](https://x.com/sama/status/2106388373221118198)

## OFFICIAL BLOGS

### Claude Blog

#### Claude Cowork and chat are now one Claude

Claude 正把 Cowork 与聊天合并为同一个入口，用户不再需要先判断任务该放进普通对话、Cowork 还是 Design。核心变化是，长时间任务可以在关闭电脑后继续运行，而原有上下文、skills 和 connectors 会直接延续到任何对话里。官方对这次产品判断的概括很直接：“So we stopped making you choose.”

同时上线测试版的 Claude Docs、Claude Slides 和对话内 Claude Design，让文档、演示和视觉设计都能在同一会话里协作编辑、评论、分享，并导出为 PowerPoint 或 PDF。功能将在未来几周先覆盖 Pro 和 Max，Team 与 Free 随后跟进；Enterprise 是否启用由管理员决定，变更前至少提前 30 天通知。对团队最实际的影响是，一份报告和配套幻灯片可以共享同一上下文，还能设为每周自动执行。[阅读原文](https://claude.com/blog/cowork-is-now-claude)

## PODCASTS

### The MAD Podcast with Matt Turck：Who Feeds the GPUs? Inside AI's Hidden $30B Layer | Renen Hallak, VAST Data

**核心结论：AI 的下一轮竞争不只发生在模型和 GPU，而在连接二者的数据与软件基础设施层。**

VAST Data 创始人兼 CEO Renen Hallak 把这层称为 AI 时代的“操作系统”。VAST Data 估值约 300 亿美元，为 xAI 和多家 AI cloud 提供基础设施。Hallak 的核心判断是，传统数据中心的每一层都要重做：机架功率从约 10kW 走向 500kW，CPU、慢速网络和机械硬盘转向 GPU、高速网络与大容量 SSD，而图片、视频、音频和自然语言又让数据量急剧增加。

最有冲击力的需求信号来自客户预测：一家 AI cloud 原先预计三年需要 500PB，随后又追加 2EB。Hallak 认为真正的物理瓶颈已经变成土地、电力、芯片与建造周期，需求增长速度快于供给。企业最终也会需要自己的“AI factory”，未必自建机房，但要控制自己的数据、模型、权重和 agent，让组织经验通过 fine-tuning 与 reinforcement learning 沉淀为自己的 IP。

他的管理方法同样具体：“bad things should be stated loudly and often and good things once and softly.” 也就是坏消息要大声、反复地说，好消息说一次就够了。组织要尽量扁平，让一线人员直接暴露瓶颈，再持续消除限制因素。对创业者而言，短期最值得关注的价值区不是容易商品化的硬件，而是软件基础设施，以及少数能形成用户忠诚的应用层产品。[观看原视频](https://www.youtube.com/watch?v=awoR908Yu5Y)

Generated through the Follow Builders skill: https://github.com/zarazhangrui/follow-builders
