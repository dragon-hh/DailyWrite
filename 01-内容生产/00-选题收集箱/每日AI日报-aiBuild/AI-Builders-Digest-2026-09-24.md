# AI Builders Digest — 2026-09-24

## X / Twitter

### Boris Cherny，Claude Code 团队

Boris Cherny 用 Opus 5.5 和少量 prompt，通过 Lean 对 Claude Agent SDK 做形式化验证，最终形成 16 个 PR，修复了多类 bug 和竞态条件。他还会结合 Lean 与 TLA+ 检查数据流、并发和状态管理，认为这类方法能发现人类很可能漏掉的问题。

https://x.com/bcherny/status/2102543349102338309

在另一项实测中，Opus 5.5 与 Fable 5.1 都把 HAProxy 从 C 移植到 Rust，并通过几乎全部测试；Opus 5.5 用时 9.5 小时，对比 Fable 5.1 的 12 小时，成本还低 51%。

https://x.com/bcherny/status/2102439069053747549

### Thibault Sottiaux，OpenAI Codex 与 ChatGPT 团队

Thibault Sottiaux 宣布 GPT-6 Sol 和 Luna 上线，强调两款模型在整体能力、写作和实际使用质感上都有明显提升。OpenAI 同时永久下调 API 价格 50%，并为 Plus、Pro 和 Business 用户发放一次可储存的 usage reset，核心方向是让更强模型覆盖更多使用场景。

https://x.com/thsottiaux/status/2102463847714247142

### Cat Wu，Anthropic Claude Code 与 Cowork 团队

Cat Wu 表示，Claude Opus 5.5 已成为 Claude Code、Claude app 和 Cowork 在 Pro、Max、Team 套餐中的默认模型。默认 effort 设为 medium，在智能水平接近 Fable 5.1 的同时速度更快；相比 Opus 5，用户的 rate limit 可多支撑约 25% 的使用量。

https://x.com/_catwu/status/2102437713781944397

### Thariq，Anthropic Claude Code 团队

Thariq 的判断是，模型能力提升不该被用来向生产环境塞入十倍功能，而应该换成更多用户理解、实验、原型和学习，最后只发布真正有效的东西。他也提醒，做游戏时 3D 生成可以快速把想象变成画面，但第一优先级仍是设计一个让人满意的核心游戏循环。

https://x.com/trq212/status/2102548686303854790

https://x.com/trq212/status/2102549030303867257

他还提到，workflows 已成为自己使用 Claude 的重要方式，而接近 Fable 水平、但成本更适合流程化调用的模型，会让这类用法更可持续。

https://x.com/trq212/status/2102477527688388752

### Guillermo Rauch，Vercel CEO

Guillermo Rauch 认为，生成和部署成本下降后，软件将不再真正“死亡”：即使 Google Reader 这类产品消失，用户也可以生成一份属于自己的版本并永久保留。

https://x.com/rauchg/status/2102594015669756323

Vercel 的最新 Next.js eval 中，Opus 5.5、GPT-6 Sol 和 Fable 5.1 都达到 97%，Grok 4.7 为 94%，但 Grok 的成本便宜 2 到 7 倍。这个结果说明，顶级编码表现已经相当接近，成本差异开始成为模型选择的重要变量。

https://x.com/rauchg/status/2102519097770885231

他还认为，AI 让网页可以呈现更独特、更具想象力的形态，因此团队已经没有理由不继续推进设计边界。

https://x.com/rauchg/status/2102438365455167883

### Alex Albert，Anthropic Research

Alex Albert 用 Opus 5.5 在 Blender 中重建 1906 年旧金山地震前的 Market Street，展示了模型在 3D 建模与视觉上的进步。他的 prompt 要求先基于保险地图、历史影像、照片和地形资料建立带来源与置信度的数据文件，再用 Blender Python 编写可复用生成器，确保每栋建筑都能追溯到证据，而不是只追求一张看起来像的图。

https://x.com/alexalbert__/status/2102466523164274839

https://x.com/alexalbert__/status/2102466524934271381

### Aaron Levie，Box CEO

Aaron Levie 把本轮模型降价视为 agent 版的杰文斯悖论：单次任务成本越低，可部署 agent 的场景反而会快速增加，包括处理企业数据、扫描代码安全问题、分析日志和运行 agent swarm。Opus 5.5 降价与 GPT-6 Sol、Luna token 价格下降 50%，会直接推动 AI 在经济活动中的扩散。

https://x.com/levie/status/2102477253070430322

Box 的企业知识工作测试也给出了更具体的数据：Opus 5.5 相比 Opus 5 少用 63% token，输出冗长度下降 42%，速度提升 30%。在尽调、云成本分析、客户账户分析和临床诊断等任务中，它不仅更省 token，还能更准确地处理口径、隐含规则和统计检验。

https://x.com/levie/status/2102448415775051790

### Garry Tan，Y Combinator 总裁兼 CEO

Garry Tan 表示，Capy 能让他比单独使用 Codex 或 Claude Code 更快完成和提交 PR，说明编码 agent 的价值正在从单模型能力转向更完整的协作流程。

https://x.com/garrytan/status/2102544711647129902

他同时认为，应该让更多人真正学会 prompt 并充分使用 AI，把它变成推动个人目标的杠杆；能力普及之后，人们还需要主动寻找并解决更多自己和他人的真实问题。

https://x.com/garrytan/status/2102501556348440983

### Nikunj Kothari，FPV Ventures 合伙人

Nikunj Kothari 提醒，许多看似规模巨大的融资中可能混入大量 SPV 资金，再叠加分阶段估值与收入口径差异，新闻标题已经很难代表真实融资质量。他的结论很直接：不要只看 headline，真正能证明质量的数据往往并未公开。

https://x.com/nikunj/status/2102534909076349291

### Peter Steinberger，OpenClaw 与 OpenAI

Peter Steinberger 在升级 macOS 27 后遇到 ChatGPT 偶发崩溃，最终由 Astra 定位到 libuv 中一个存在约 14 年的 bug。这个案例说明，前沿模型在真实软件维护中的价值，不只是生成新代码，也包括穿透复杂依赖链寻找长期潜伏的根因。

https://x.com/steipete/status/2102501642176528743

### Aditya Agarwal，South Park Commons 普通合伙人

Aditya Agarwal 认为，当下关于 AI safety 的讨论之外，自动驾驶早已面对更具物理后果的安全问题。Waymo 为了让重达两吨、时速约 30 英里的机器人进入城市道路，建立了庞大的 eval 与测试基础设施；这种用系统化验证换取发布信心的方式，也值得其他 AI 产品借鉴。

https://x.com/adityaag/status/2102457464432284019

### Claude，Anthropic AI assistant

Claude Opus 5.5 上线后展示了两类更具象的创作应用：一类是由不同 seed 生成不同结果的算法绘图程序，另一类是把照片或文字描述转成可实际搭建模型和定制说明书的积木应用。这些例子把模型能力从聊天和编码延伸到了可交互、可制造的创作工具。

https://x.com/claudeai/status/2102471889092276516

https://x.com/claudeai/status/2102471885061812714

Generated through the Follow Builders skill: https://github.com/zarazhangrui/follow-builders
