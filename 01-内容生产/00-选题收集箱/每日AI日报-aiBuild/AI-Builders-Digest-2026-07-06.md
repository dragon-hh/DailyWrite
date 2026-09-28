AI Builders Digest - 2026-07-06

## X / TWITTER

### OpenAI Codex & ChatGPT 的 Thibault Sottiaux

Thibault Sottiaux 今天最值得看的是一个很直接的产品反馈征集：他问大家，Codex 现在还有哪些「早该做好、但依然做不好」的事情。这个问题本身比普通发布更有信号，因为它暴露了团队正在主动找 Codex 的长期短板，而不是只展示 demo。另一个高互动帖子是他分享 Sol 的一次轻松对话，把 emoji 计数、乘法和「欠 332 个敬礼」玩成了一个小型模型行为样本。

来源：
https://x.com/thsottiaux/status/2073551549494596079
https://x.com/thsottiaux/status/2073554978053005607

### Linear 产品负责人 Nan Yu

Nan Yu 把代码审查和产品测试分得很清楚：找 bug 最好的方式不是坐在那里「死算」代码，而是真正使用产品、试着把它弄坏；代码审查更适合看 architecture 和 API design，用来控制 technical debt 的增长。她还用两个 AI 编码相关的玩笑补了一刀：如果模型把生产表全删了，到底是模型被开除还是你被开除？这背后其实是 agent 时代责任边界的问题。

来源：
https://x.com/thenanyu/status/2073410299680428445
https://x.com/thenanyu/status/2073410944969932877
https://x.com/thenanyu/status/2073412466436878666

### Anthropic Claude Code / Cowork 的 Cat Wu

Cat Wu 说 Claude Fable 5 在 retention analysis 里主动使用了 propensity score matching，也就是按用户活跃度做匹配，让比较对象更接近「同类对同类」。她把这个例子归因于 Fable 5 判断力的提升，并把范围扩展到 Cowork 里写邮件、写文档，以及 Claude Code 里调试复杂错误。重点不是模型会一个统计术语，而是它在没有被明确要求时，能主动选择更合适的分析方法。

来源：
https://x.com/_catwu/status/2073439890482794966

### Vercel CEO Guillermo Rauch

Guillermo Rauch 基于 Vercel AI Gateway 的 lifetime usage 做了一个 token spend race 动画。这个 Gateway 每月聚合来自数百万开发者的数万亿 token，因此它看到的不只是单一产品数据，而是开发者实际调用模型的横截面。他点出的趋势是：不同 lab 之间的使用量会波动，Anthropic 当前很强，同时 open weight AI 也在上升。

来源：
https://x.com/rauchg/status/2073563586270781674

### OpenClaw + OpenAI 的 Peter Steinberger

Peter Steinberger 预告 OpenClaw 下一版会显示 reset 到期时间，让用户更清楚什么时候恢复额度。这是很小但很实用的 power-user 功能：对重度使用 Codex/agent 工具的人来说，reset 透明度直接影响任务排程和 token 使用策略。

来源：
https://x.com/steipete/status/2073482942513565713

### Every CEO Dan Shipper

Dan Shipper 转发并调侃了「Codex in ChatGPT」相关内容，重点信号是 Codex 正在更明显地进入 ChatGPT 使用场景，而不是只作为独立开发工具存在。他另一个帖子只是从 3Blue1Brown 与 Dwarkesh 的内容里学到数学家名字的发音，轻量但不算产品信号。

来源：
https://x.com/danshipper/status/2073586548545638459
https://x.com/danshipper/status/2073422764275364153

## OFFICIAL BLOGS

### Claude Blog: Building intelligent apps for Apple platforms with Claude in the Foundation Models framework

Claude Blog 发布了面向 Apple 平台的 Foundation Models framework 支持：通过新的 Swift package，开发者可以在 Apple 的 Foundation Models framework 里调用 Claude，把本地模型适合的快速任务和 Claude 适合的复杂任务接起来。Apple 的框架可以用 Swift 原生方式返回 typed values，并通过 @Generable annotations 形成干净输入；Claude 则接手 multi-step reasoning、code generation、web search 和 code execution 等更重的工作。

实际意义很明确：一个 journaling app 可以先在设备端生成每日 prompt，再让 Claude 跨几个月日记找线索；study app 可以先本地解释术语，再把更深入的「为什么重要」交给 Claude。支持将面向 iOS 27、iPadOS 27、macOS 27、visionOS 27 和 watchOS 27，开发者用 Anthropic API key 接入，package 负责 streaming、tool calls 和 structured responses 回到 SwiftUI view。

来源：
https://claude.com/blog/claude-for-foundation-models

## PODCASTS

### The MAD Podcast with Matt Turck: Cloudflare CEO: The Internet's Business Model Is Dead

The Takeaway：Cloudflare CEO Matthew Prince 的核心判断是，AI bot 和 agent 已经把互联网从「人看网页、广告付费」推向一个新阶段，而旧商业模式撑不住机器流量的成本。

Matthew Prince 说，Cloudflare 看到 bot traffic 已经在 2026 年上半年超过 human traffic，而且几乎全部增长都由 AI 和 LLM 背后的系统推动。他给出的具体画面很直观：人类买相机可能访问 5 个网站，agent 可能访问 5,000 个网站；如果趋势延续，五年内互联网流量可能变成今天的 1,000 倍。最尖锐的一句话是：「bots don't click on ads」。这意味着服务器、网络、CPU、GPU、内存都要扩张，但广告这种靠人类点击和展示付费的模型无法自然覆盖这些成本。

这期的另一个有用视角是，agent 时代会改变 brand 的含义。品牌过去是给人类的快捷信号：看到 Walmart、Marriott、McDonald's，你大概知道体验是什么。但 bot 有近乎无限耐心去比较和发现，品牌不再只是人脑里的 shortcut。Prince 没有给出确定答案，但他的判断很清楚：未来五年，互联网的商业模式会剧烈变化，而 Cloudflare 这类站在大量流量前面的基础设施公司，会被迫参与定义新规则。

来源：
https://www.youtube.com/watch?v=UN47z_opfmo

Generated through the Follow Builders skill: https://github.com/zarazhangrui/follow-builders
