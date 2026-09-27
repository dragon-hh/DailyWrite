AI Builders Digest — 2026-06-23

X / TWITTER

Thibault Sottiaux，OpenAI Codex & ChatGPT 团队

Thibault Sottiaux 这次主要在向 Codex 用户要反馈：一是 Codex 现在可以累积 usage resets 后，用户到底会囤着不用，还是放心消耗；二是 Codex app 里哪些地方还“不够 delightful”。这不是产品发布，更像是一个很直接的产品信号：OpenAI 仍在把 Codex 当成高频开发工具来打磨，核心问题已经进入使用习惯、额度心理和体验细节这一层。

来源：
https://x.com/thsottiaux/status/2068792010715324444
https://x.com/thsottiaux/status/2068736857312198928
https://x.com/thsottiaux/status/2068792061265121316

Peter Yang，Practical AI 教程与访谈作者

Peter Yang 转述了 liu8in 关于 agentic video 的一个很实用判断：HTML 之所以可能成为视频 agent 的基础，是因为“agents have no visual intelligence”，而 HTML/CSS/JavaScript 是 LLM 更天然的表达层。也就是说，与其让 agent 直接“看懂并制作视频”，不如先把视觉结构变成它擅长操作的代码，再叠加 footage、image、asset、SVG 等素材。他还提到 ferrymanio 这类跨平台发布工具，以及自己对 unlimited token plans 的“tokenmaxxing”心理：额度越无限，越觉得不烧满是一种浪费。

来源：
https://x.com/petergyang/status/2068755908319236338
https://x.com/petergyang/status/2068854663534031124
https://x.com/petergyang/status/2068874249167884544

Nan Yu，Linear Head of Product

Linear 产品负责人 Nan Yu 赞同“Quality is irrational”这个说法：持续选择质量，需要一种近乎非理性的投入，也需要相信端到端控制会比套用通用框架带来更好结果。这条和 Linear 一贯的产品气质一致：质量不是一个 ROI 表格里自然会赢的选项，而是团队主动选择的偏执。他还回应了 Outlook/Gmail 相关讨论，认为单靠某个补丁式方案无法显著解决问题，关键在默认行为。

来源：
https://x.com/thenanyu/status/2068778750800531640
https://x.com/thenanyu/status/2068668365623710018

Guillermo Rauch，Vercel CEO

Vercel CEO Guillermo Rauch 提到团队对 v0 性能做了全面优化，从 painting、layout、WebGPU shaders 到 blocking scripts，每一帧都被审视，并表示会把学到的经验更新到相关资料中。更有意思的是他那句短评：“Coding agents will squeeze every ounce of IKEA effect out of you, if you let them.” 这句话点到了 AI coding 的一个真实副作用：agent 越能帮你搭东西，人越容易对“自己参与搭出来的东西”产生过度依恋。

来源：
https://x.com/rauchg/status/2068838709517336756
https://x.com/rauchg/status/2068778558672273422

Aaron Levie，Box CEO

Box CEO Aaron Levie 连发两条关于 agent 架构和企业软件未来的判断。第一条是关于 Sakana 的 Fugu：它把任务自动分配给最适合的模型，并负责选择、委派、验证和综合，让开发者面对的是单一 API，而不是复杂的 multi-agent 系统。Levie 认为这和很多 applied AI 产品正在构建 agent harness 的方式一致，未来随着闭源前沿模型和开源模型继续分化，能做“最佳模型路由”的层会非常有价值。

他的第二个判断更偏企业软件：agents 使用软件的频率可能会是人的 100 倍，因此权限、数据泄漏防护、权威数据源、日志审计、人机协作都会变成核心基础设施。一个简单 agentic task 可能调取的数据，比一个用户一个月接触的数据还多。那些能支撑 headless interactions、并且商业模式和技术策略都跟得上的平台，会在下一阶段占更好位置。

来源：
https://x.com/levie/status/2068917230570795178
https://x.com/levie/status/2068851573175021864

Ryo Lu，Cursor 设计师，早期 Notion 和 Stripe 成员

Ryo Lu 展示了自己在 ryOS 里做的 Books：因为想念木质书架，他从 Cursor mobile 开始搭建，然后手工调动画和材质，直到感觉对了。它支持任意 epub，并能和 ryOS account 同步阅读进度。这条信息的重点不是“又一个阅读器”，而是一个设计师型 builder 的工作流：先用移动端 coding agent 起步，再用人工 taste 打磨交互质感。

来源：
https://x.com/ryolu_/status/2068923971136098633
https://x.com/ryolu_/status/2068924375341179347

Garry Tan，Y Combinator President & CEO，GStack / GBrain creator

Garry Tan 强调，在 2026 年这个 usable AGI 刚起步的阶段，被低估的是“个人大脑”和“公司大脑”的价值。AGI 给你 intelligence，但真正解锁效果仍然需要你收集并整理自己的 personal context。他也说这正是他做 GBrain 并开源它的原因。这个判断和当前 agent 产品的一个共同瓶颈吻合：模型能力越来越强，但没有上下文，就没有可靠的个性化执行。

来源：
https://x.com/garrytan/status/2068701356358308112
https://x.com/garrytan/status/2068701357696323769

Zara Zhang，Builder

Zara Zhang 给了一个判断 AI slop 的简单规则：你的输入，也就是 context，是否比输出更长？她的经验是，要让 AI 产出高质量写作或设计，输入通常需要是输出的 3 到 5 倍。如果输入远短于输出，结果很可能就是 slop。她还特别澄清，她说的是 context，不是 prompt。这是一个很值得记住的区分：prompt 是指令，context 是真实材料和约束。

来源：
https://x.com/zarazhangrui/status/2068923768500793603
https://x.com/zarazhangrui/status/2068964055235321954

Nikunj Kothari，FPV Ventures Partner

Nikunj Kothari 分享了一个投资人每周都会遇到的 workflow：在 X 上看到有趣项目，试用、fork、冒出想法，然后点进 founder 主页准备私信，同时祈祷自己之前没有漏回过对方的 DM。他说自己会尽量回复所有 DM，但还是会漏。这不是 AI 技术观点，但对 builder 生态有用：X 仍然是项目发现、试用和投资人触达的重要链路，只是信息流和私信管理已经成了瓶颈。

来源：
https://x.com/nikunj/status/2068714024934740476

Peter Steinberger，OpenClaw + OpenAI

Peter Steinberger 提到 OpenClaw 的讨论：热度回落之后，团队提高了质量、扩展了团队，并创建了非营利组织；他认为这是 OpenClaw 目前最强的一周。他还表示自己曾经怀疑 multi-model routing，而最新讨论让他觉得这个怀疑可能是对的。放在今天其他 builder 的讨论里看，这正好形成一个张力：一边是 Aaron Levie 看好模型路由层，一边是 Peter 对 multi-model routing 保持怀疑，说明这个方向还远没有形成共识。

来源：
https://x.com/steipete/status/2068961217524490739
https://x.com/steipete/status/2068960117253632160
https://x.com/steipete/status/2068965200343224367

PODCASTS

Training Data: Google DeepMind's Logan Kilpatrick: Why the Model Eats the Harness

The Takeaway：Logan Kilpatrick 的核心判断是，AI 产品的竞争重点正在从“模型本身”扩展到模型周围的 agent harness，但这个 harness 也会不断被模型吞掉，新的 alpha 会继续上移。

Logan Kilpatrick 负责 Google AI Studio 和 Gemini API，他把 Google 当前的 agentic 战略描述成第二条“贯穿线”：过去 Gemini 模型本身把 Google 的许多产品串起来，现在 Antigravity 这样的 agent harness 正在成为新的基础层。它不只是 IDE，还包括 web 上的 agent-first experience、CLI、SDK，以及可通过 Gemini API 使用的 managed agent。更关键的是，同一套 harness 也在驱动 Search、Gemini app、Cloud、AI Studio 等产品里的 agent 能力。

他对“agentic AI 是否会吞掉现有产品使用时长”的回答很 Google：目标不是最大化 eyeballs，而是最大化用户 outcome。他认为 Search 在 AI 时代反而变成正和，用户和 agent 都在搜索更多。Google 产品的 agentic 程度目前大多还在 crawl 阶段，因为 13 个十亿级用户产品需要谨慎推进；更靠近 walk 的是 Gemini app 和 Antigravity 这类前沿体验。

关于 coding agents，他承认外部开发者对 Gemini coding 的采用感知不如 Claude 和 Codex 强，但认为 Google 已经通过 Windsurf 团队和 Antigravity 建起内部反馈飞轮。他特别强调，“如果没有一个真正承载长程开发任务的产品，很难做出很好的 coding model”。Google 内部 10 万级工程师的 dogfooding、AB test 和 live experiments，是他们认为可以转化为优势的地方。

最值得记的一段是他对“model eats the harness”的解释：两年前，model 基本就是一组 weights，输入 token，输出 token；现在大家仍叫它 Gemini、GPT、Claude，但它已经变成围绕 weights 的一整套系统，包括 tool calling、hosted tools、search、code execution、container、agent harness 等。scaffolding 往往领先模型几步，然后逐渐被上游吸收进模型系统。他预计今天很多人认为 harness 是 alpha，但 12 个月后，这种形态的 harness 可能已经不再是核心差异点。

在 world models 和 generative media 上，他把 Omni 视为“world understanding playing out”的例子：它不是把人替换成 AI avatar，而是保留人的话语、声音、形象，只改变布景、桌子等非人格化元素。他喜欢这种方向，因为“personhood is there. It's just different and amplified.” AI Studio 的 Android vibe coding 也给了一个硬数字：他说过去一周 AI Studio 里已经构建了约 350,000 个 Android apps，其中很多可能原本根本不会被人做出来。

播客来源：
https://www.youtube.com/watch?v=cMAs8z2dehs

Generated through the Follow Builders skill: https://github.com/zarazhangrui/follow-builders
