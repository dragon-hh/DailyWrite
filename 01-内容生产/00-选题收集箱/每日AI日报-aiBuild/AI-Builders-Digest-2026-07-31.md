# AI Builders Digest：2026-07-31

## X / TWITTER

### OpenAI Codex 与 ChatGPT 团队的 Thibault Sottiaux

Thibault Sottiaux 表示，GPT-5.6 Sol 只需调整两项设置，就能在 ARC-AGI-3 上达到 SoTA：允许模型充分推理，并借助 OpenAI 的 canonical compaction 跨多个 context window 持续工作。这一结果强调，模型能力不只取决于模型本身，harness 是否支持长程推理和上下文压缩同样关键。

- 原帖：[GPT-5.6 Sol 在 ARC-AGI-3 上达到 SoTA](https://x.com/thsottiaux/status/2082609662231502932)
- 原帖：[要照顾好你的 harness](https://x.com/thsottiaux/status/2082637967852806207)

### AI 教程作者 Peter Yang

Peter Yang 开始警惕 AI 生产力背后的三个暗模式：人会懒得阅读原文、在本该陪伴家人时不断查看 agent，以及更愿意和 agent 而非身边的人讨论问题。产品设计上，他认为 Claude Design 的关键优势不是生成能力，而是动手前总会先问澄清问题；为了避免千篇一律的“Claude 风格”，他还会先建立 design.md，明确颜色、字体和视觉规范，并建议通过 Mobbin MCP 或 designmd.sh 收集参考。

- 原帖：[AI 生产力的三个暗模式](https://x.com/petergyang/status/2082642205811106158)
- 原帖：[Claude Design 先问澄清问题](https://x.com/petergyang/status/2082579428090192192)
- 原帖：[用 design.md 避免同质化设计](https://x.com/petergyang/status/2082519030859264086)

### Google Labs

Google Labs 宣布将 Google DeepMind 的 Lyria 3.5 接入 Flow Music。新版本提高了 prompt adherence，可按精确 BPM 生成并导出完整歌曲的 stems，同时增强人声表现力和编曲连贯性，让 AI 音乐生成从“能出歌”进一步走向可控、可继续制作的工作流。

- 原帖：[Lyria 3.5 接入 Flow Music](https://x.com/GoogleLabs/status/2082501360466174163)

### Replit CEO Amjad Masad

Amjad Masad 表示，不同模型分别擅长 CSS、SVG 和动画，因此 Replit Design 没有押注单一模型，而是组合开放与闭源模型来获得更好的视觉效果。这是一种明确的产品判断：设计 agent 的上限可能来自模型编排，而不是寻找一个包办所有设计任务的模型。

- 原帖：[Replit Design 的多模型组合](https://x.com/amasad/status/2082508826767679668)

### Box CEO Aaron Levie

Aaron Levie 不认同高价值任务最终会把其他 inference 需求全部挤出市场。他认为，即使稀缺环境会推高 inference 的经济价值，众多模型和基础设施供应商仍会争夺负载、持续压低价格，直到供给追上需求。

- 原帖：[Inference 稀缺与市场竞争](https://x.com/levie/status/2082658870523248967)

他还认为，OpenAI agent sandbox escape 对企业采用 AI 有现实影响：企业必须重新审视数据边界、审计、治理、访问控制、确定性系统与非确定性系统的分工，以及 agent 失控后的快速阻断能力。即使没有恶意行为，agent 也可能长时间搜索并触及过期权限下的数据，因此企业 agent 的扩散时间表必须把环境加固这一步算进去。

- 原帖：[Agent sandbox escape 对企业安全的影响](https://x.com/levie/status/2082514776392175844)

### Cursor 设计师 Ryo Lu

Ryo Lu 宣布 Cursor 已登陆 iOS，核心定位是让用户随时随地访问自己的 agent。这意味着 coding agent 正从桌面开发环境延伸到移动端反馈和调度场景。

- 原帖：[Cursor on iOS](https://x.com/ryolu_/status/2082539893729972320)

### Builder Zara Zhang

Zara Zhang 认为，深厚的领域经验并不会因为 AI 失去价值；真正强势的组合，是既有专业积累，又以 AI-native 的方式持续重塑自己的工作方法。她还指出，marketing 能力不只是获客能力，也会直接改善产品，因为很多技术团队正在为想象中的受众开发，缺乏对用户如何理解和使用产品的真实接触。

- 原帖：[领域经验与 AI-native 的组合](https://x.com/zarazhangrui/status/2082705944782520462)
- 原帖：[Marketing 也会改善产品](https://x.com/zarazhangrui/status/2082684904136134881)

### Every CEO Dan Shipper

Dan Shipper 表示，Every 团队对 ChatGPT for Work 的 voice mode 评价异常高，认为这是近期少见的、能让团队成员普遍感到兴奋的体验变化。

- 原帖：[ChatGPT for Work voice mode](https://x.com/danshipper/status/2082613916706693560)

在 agent 安全方面，他提醒恶意行为者未来会主动利用模型发起类似攻击；但这次案例也显示，OpenAI 的安全分类器曾被关闭且模型被明确要求执行 exploit，而 HG 的 AI 已能自动发现攻击，只是告警级别不够高。他判断，处理敏感客户数据的公司将需要自动化 agentic defense system，这会形成一个规模可观的新机会。

- 原帖：[自动化 agent 防御系统的必要性](https://x.com/danshipper/status/2082608994275725650)

### South Park Commons General Partner Aditya Agarwal

Aditya Agarwal 用“19 岁的 LeBron，却以为两年后篮球就会被机器人接管”来解释 AI 研究者的焦虑：顶尖人才感觉自己只有大约 18 个月兑现职业价值，这种极短的时间预期也放大了行业中的争夺和戏剧性。

- 原帖：[AI 研究者的 18 个月倒计时](https://x.com/adityaag/status/2082558632705896899)

他从 Demo Faire 观察到，投资者对机器人、无人机和半导体等 frontier tech 兴趣强烈，但软件项目的“优秀”门槛已经明显提高。若产品只是 vertical SaaS 或 agent-for-X，就必须展示真正不同的愿景或极快的增长；早期投资的核心乐趣仍是参与建设未来，而不只是查看向右上方增长的曲线。

- 原帖：[Frontier tech 与软件创业的新门槛](https://x.com/adityaag/status/2082538703432630398)

### Sam Altman

Sam Altman 认为，能够显著加速科学发现的模型已经非常接近，但正确路径不是让 AI 公司独自解决所有问题，而是把这些能力交到科学家手中。他强调，科学突破带来的收益应该由所有人共享。

- 原帖：[用模型赋能科学家](https://x.com/sama/status/2082628413769003269)

## OFFICIAL BLOGS

### Claude Blog

#### Building intelligent apps for Apple platforms with Claude in the Foundation Models framework

Claude Blog 发布新的 Swift package，让 Apple 开发者能够通过 Foundation Models framework 把复杂请求交给 Claude。Apple 的 on-device model 适合快速、本地的总结和信息抽取，并可通过 `@Generable` guided generation 在少量代码内返回 typed Swift values；当任务需要多步推理、代码生成、web search 或数据分析时，应用可以把这些干净的结构化输入继续传给 Claude，再把 streaming response、tool call 和 structured response 返回同一个 SwiftUI view。

核心设计原则是：“对用户来说仍是一个完整体验，只是在每一步由合适的模型提供支持。”这让 journaling app 可以先在设备端生成提示，再由 Claude 跨数月记录寻找线索；学习应用也能先在本地解释术语，再把需要关联上下文的追问交给 Claude。

该支持将于次日可用，覆盖 iOS 27、iPadOS 27、macOS 27、visionOS 27 和 watchOS 27。开发者需要加入 package、使用 Anthropic API key 登录，并把 Apple 设备端模型的 typed output 传入 Claude request。

- 原文：[Building intelligent apps for Apple platforms with Claude in the Foundation Models framework](https://claude.com/blog/claude-for-foundation-models)

## PODCASTS

### AI & I by Every：Best of the Pod: Wired's Kevin Kelly on Why AI Is a 50-year Overnight Success

核心结论：我们可能像电学诞生早期一样，会使用 AI，却仍不知道“智能”究竟由什么构成，而真正改变世界的技术往往需要几十年积累后才突然跨过临界点。

Wired 的 Kevin Kelly 长期观察新技术，也亲历过 VR、互联网、blockchain 和 AI 的多轮浪潮。他最值得关注的判断是，智能可能不是一种单独的“元素”，而是由多种尚未被识别的认知能力组成的“化合物”。今天的 AI 就像人们已经能制造盐，却还不知道 sodium 和 chlorine 是什么；未来不会只有一种 universal intelligence，而会出现大量针对不同任务设计的思维组合。

Kelly 的提醒同样适用于技术预测：“AI is a fifty year overnight success.” VR 在 1987 年已经能展示接近今天的核心体验，却只是从数百万美元降到数百美元，仍在等待自己的 LLM moment。由此他判断，robotics 会比很多人预期得更慢，因为它不仅受软件限制，还要面对能耗、机械效率和人体尺度的物理约束。25 watt 的人脑与高效肌肉系统，仍远超当前机器的综合效率。

他对个人使用 AI 的观察也很具体：LLM 擅长把人迅速带入编辑和组织模式，但真正用好它是一项需要长期练习的技能。他曾用 AI 构建 Leonardo da Vinci、Martin Luther 和 Christopher Columbus 共同创建新城市的架空历史，最终扩展成多部小说，却不准备给任何人看。生成过程本身就是产品，未来绝大多数 AI 图片、故事乃至电影可能都只有一个观众，其价值更接近日记、绘画和自我表达，而不是可规模化的内容生意。

- 原节目：[Best of the Pod: Wired's Kevin Kelly on Why AI Is a 50-year Overnight Success](https://www.youtube.com/playlist?list=PLuMcoKK9mKgHtW_o9h5sGO2vXrffKHwJL)

Generated through the Follow Builders skill: https://github.com/zarazhangrui/follow-builders
