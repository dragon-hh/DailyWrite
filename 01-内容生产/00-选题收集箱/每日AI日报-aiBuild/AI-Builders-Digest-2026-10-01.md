# AI Builders Digest — 2026-10-01

## X / TWITTER

### Thibault Sottiaux，OpenAI Codex 与 ChatGPT 产品成员

Thibault Sottiaux 表示，未来几天内会有数百万个 Dots 上线，为大量不同用户持续处理各类任务。他的实际感受是，经过两三天使用、让 Dot 逐步了解个人偏好和关注事项后，体验会出现明显跃升，而且它能独立承担相当有野心的任务。OpenAI 目前正先观察用户如何使用主 Dot，再决定何时开放创建整支 Dot 团队的能力。

https://x.com/thsottiaux/status/2105105086506840421

### Thariq，Anthropic Claude Code 团队成员

Thariq 给出了一个很简单的 Claude 使用建议：明确告诉它“我们有能力做成任何事，请更勇敢一点”。这不只是 prompt 技巧，也是在提醒使用者，模型输出的上限有时取决于你是否给了它足够大胆的行动空间。

https://x.com/trq212/status/2105065127892734076

### Amjad Masad，Replit CEO

Amjad Masad 分享了一套 harness 设计思路，目标是用明显更低的成本逼近前沿性能。关键提示不是单纯追逐更强模型，而是通过执行框架与系统设计，把性能和成本一起纳入优化。

https://x.com/amasad/status/2104996638817386820

### Guillermo Rauch，Vercel CEO

Guillermo Rauch 宣布 AI SDK 的每周下载量达到 3000 万。他还用 fframes、Opus 和 GPU 渲染制作了一段增长里程碑视频，把 500 万、1000 万、2000 万和 3000 万下载量节点直接变成可视化内容，展示了 AI 编程与程序化视频生产的结合方式。

https://x.com/rauchg/status/2105043144975011982

### Aaron Levie，Box CEO

Aaron Levie 认为，在当前阶段，AI 行业仍有可能通过共享标准与共同实践处理安全和保障问题，同时不牺牲竞争。他也承认，随着能力继续提升，更严格的监督、测试、责任层和监管终将到来，但眼下行业自发协作仍是一条现实路径。

https://x.com/levie/status/2105111520913039530

### Garry Tan，Y Combinator 总裁兼 CEO

Garry Tan 把 OpenClaw 的 test-audit skill 合并进了 GStack，直接针对测试膨胀问题。他的判断是，测试数量变多并不自动等于质量更高，而如今可以借助 AI 审计测试资产，识别重复、低价值或失去作用的测试。

https://x.com/garrytan/status/2105049005147525231

### Zara Zhang，Builder

Zara Zhang 用 Opus 5.5 只经过 6 次 prompt，就为自己的水杯做出一整套营销网站。整个制作链同时调用 ElevenLabs 生成音乐、Meshy 生成 3D 资产、OpenAI API 生成图片，说明复杂的多媒体网站已经可以由一个模型串联多种生成工具完成。

https://x.com/zarazhangrui/status/2105096296831017078

### Nikunj Kothari，FPV Ventures 合伙人

Nikunj Kothari 观察到，当前市场越来越难找到长期投入的“传教士型”人才，许多人更愿意快速加入显而易见的赢家；对早期投资者来说，核心人物突然离开可能让原公司迅速变成空壳。他认为应用层的护城河已经不是单一壁垒，而是产品、技术和 GTM 中上千个细节的组合，最终仍会回到创始人的执行速度与适应能力。

https://x.com/nikunj/status/2105148927599423752

他还给 B2B 创始人提供了一个低成本获客思路：把 X 上正在升温的话题整理后发布到 LinkedIn，因为后者往往慢一到两周，可以借时间差获得注意力。

https://x.com/nikunj/status/2104949147812159672

### Sam Altman，OpenAI CEO

Sam Altman 宣布 Dots 上线，把它描述为一种全天候替用户工作的 AI 方式，目的是释放人的时间与注意力，让用户把精力放到更高层级的工作上。

https://x.com/sama/status/2104995014208258235

他同时强调 6.1 Sol 的成本优势：价格是 Astra 的五分之一，cache read 还提供 95% 折扣，并称其能力依然很强。

https://x.com/sama/status/2104994395980533804

## 官方博客

### Claude Blog：Claude in Chrome is generally available

Claude in Chrome 已向所有 Claude 付费套餐全面开放，并新增浏览器内自主执行能力，不再要求用户逐项批准每个操作。它可以利用现有登录状态读取页面、输入文字、点击链接、跨页面导航和填写表单，尤其适合没有 API 的内部仪表盘、旧系统和供应商门户。

安全机制是这次开放的重点。官方原文称：“Claude in Chrome 现已向所有 Claude 付费套餐全面开放。”与此同时，系统会在执行前用 probe 检查网页内容中的潜在 prompt injection，再由安全分类器核对即将执行的动作是否符合用户原始要求，不匹配的动作会被阻止。最新评测中，Claude Sonnet 5 和 Opus 5 在启用 probe 与自动审批安全分类器后没有攻击成功，Fable 5 的攻击成功率为 0.3%，且人工确认都属于低严重性场景。

实际影响是，浏览器 agent 可以覆盖更多无法直接接入的工作系统，但 prompt injection 仍是持续变化的风险。Claude in Chrome 当前只支持 Chrome；本地文件或其他桌面应用仍需要 Claude desktop app，其他 Chromium 浏览器和移动端暂不支持。

https://claude.com/blog/claude-in-chrome-generally-available

Generated through the Follow Builders skill: https://github.com/zarazhangrui/follow-builders
