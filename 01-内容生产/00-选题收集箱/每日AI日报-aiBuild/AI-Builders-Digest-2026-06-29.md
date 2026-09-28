AI Builders Digest — 2026-06-29

X / TWITTER

Swyx（AI Engineer / Latent Space 等）提醒，开放模型做 eval 时不应只按 token 数比较推理预算，也可以按热门推理服务商上的「美元推理成本」来衡量 thinking level。核心点是：开放模型在每美元 token 里程上可能明显优于闭源 API，所以成本口径会改变模型发布方讲故事的方式。
来源：https://x.com/swyx/status/2070949306060931312

OpenAI Codex & ChatGPT 的 Thibault Sottiaux 总结了 Codex 最近的一批产品改进：超长线程处理更顺，悬浮导航栏可以预览并跳转回合，设置搜索覆盖更多控件，缩放不再让 tooltip、dialog、menu 等错位，复制到 Slack 能保留 Markdown，大段粘贴也不会卡死 UI。他还提到一个偏轻松但很有产品味的新增项：专门的 Pets panel。
来源：https://x.com/thsottiaux/status/2071071289247244481

Peter Yang 分享了一个很实用的个人 AI 工作流：每周六让 Hermes 自动发健康检查邮件，从 Withings 智能秤、Fitbit、Google Health，以及自己 vibe coded 的 MCP server 和移动健身 app 里拉数据，汇总目标进展、关键 takeaways 和统计。他另一个判断也值得记：问题处理没有绝对等级，如果火已经烧了几天，越早拉人一起解决，往往比独自等到“高级别方案”更好。
来源：https://x.com/petergyang/status/2070906940352520477
来源：https://x.com/petergyang/status/2071058953115767275

Linear 产品负责人 Nan Yu 对“解决问题能力等级”框架泼了一点冷水：如果你遇到的问题里 90% 都不值得解决，那么 level 1 和 level 6 在 90% 的情况下其实差不多。这句话背后的产品判断是，识别什么不值得做，本身就是能力的一部分。
来源：https://x.com/thenanyu/status/2070821322901397645

Vercel CEO Guillermo Rauch 关注 AI 安全能力的攻防两用性。他认为 Mythos / Sol 一类网络安全能力既能用于防御，也可能成为进攻能力；如果对手拿到等价能力，而美国企业还不知道自己的潜在漏洞，会形成严重风险。他建议企业用 deepsec 或类似 harness 配合 frontier models 提前做安全检查。
来源：https://x.com/rauchg/status/2071047674187714830

Box CEO Aaron Levie 认为，AI token 成本优化真正的关键不是抽象技巧，而是深刻理解底层工作流。企业想要用更少的钱买到更多 intelligence，需要一个介于具体业务和底层模型之间的应用层：懂 workflow、context、business process，能做 eval、领域优化、UX 调整和落地支持。他把这视为当前 applied AI 公司的核心 playbook。
来源：https://x.com/levie/status/2070937863806751154

FirstMark VC / MAD Podcast 主持人 Matt Turck 用一段“智能眼镜历史”吐槽了行业循环：从 Google Glass、Microsoft HoloLens、Meta Ray-Ban、Apple Vision Pro 到 Snap，硅谷一直在换包装说服用户“这次真的想要”。有用的提醒是：AI 眼镜要赢，不能只靠技术叙事，必须证明普通用户真的愿意戴、愿意用。
来源：https://x.com/mattturck/status/2070972014945243622

Builder Zara Zhang 分享了一个很强的非传统开发者信号：她说自己不是工程师，去年还几乎不会用 GitHub，现在 GitHub 已经有 10k followers，项目都来自“用技术连接真实用户问题、解决自己的痛点、再把产品故事讲出来”。这是一种 AI 时代很典型的 builder 路径：不会手写代码，也能把产品做出来并获得分发。
来源：https://x.com/zarazhangrui/status/2070982013822333007
来源：https://x.com/zarazhangrui/status/2071116793234813272

Peter Steinberger（OpenClaw + OpenAI）转述了一句很适合 AI 产品分发和访问控制的话：“History teaches us that access blockage rarely stops determined users.” 他当天也提到自己在大屏显示器上折腾 BetterDisplay 的体验，最后还是回到 2x XDR，算是一个硬件生产力选择的小注脚。
来源：https://x.com/steipete/status/2071063588329193551
来源：https://x.com/steipete/status/2071034256051097799

OFFICIAL BLOGS

Claude Blog：Claude Code now supports artifacts

Claude Code 开始支持 artifacts：它可以把一次 coding session 中的调查、重构、分析和进度，转成实时可分享的可视化页面，例如 PR walkthrough、系统解释器、dashboard、release checklist、incident timeline 等。关键不只是“生成页面”，而是页面基于当前 session 的完整上下文，包括代码库、connectors 和对话本身；更新后同一个链接会原地刷新，并保留版本历史。默认权限是作者私有，可分享给团队或组织，且不能公开发布。实际含义很明确：agent 工作不再只是聊天记录或终端输出，而可以变成团队能共同查看、复用、审阅的工作界面。
来源：https://claude.com/blog/artifacts-in-claude-code

PODCASTS

Training Data：Memory and Continual Learning: Engram's Dan Biderman and Jessy Lin

核心 takeaway：Engram 的判断是，下一代有用的 AI memory 不能只靠把内容塞进 context window 或外部数据库，很多“该内化的东西”需要进入模型权重，变成模型的直觉。

Dan Biderman 和 Jessy Lin 是 Ngram / Engram 的联合创始人，方向是 memory 和 continual learning。他们认为当前模型真正的瓶颈不一定是原始智力，而是理解新的、持续变化的上下文：公司怎么工作、团队优先级是什么、某类任务在这个组织里怎么做。RAG、工具和 context engineering 仍然重要，但如果模型每次都要重新读同一批文件、写超长 system prompt、靠搜索才知道该问谁，推理成本和质量都会受限。Jessy 提到，在某些场景下，把常用组织知识和工作模式训练进模型，可能让 token 消耗下降两个数量级。

他们最有意思的区分是：什么应该 externalize，什么应该 internalize。酒店房间号可能写下来就好，但长期使用的密码、团队协作习惯、谁负责什么、哪些研究方向有关联，这些更像应该被模型“记住”的东西。Dan 的一句话很概括：“In the same way you ask an employee, they don't type into the search box, What was I working on yesterday? They just know.” 这也是他们想象的未来：每个团队、每个人都有不同于 frontier model 的专属模型，随着时间真的变得更懂你、更懂你的组织。
来源：https://www.youtube.com/watch?v=aiR7F4jqjXY

Generated through the Follow Builders skill: https://github.com/zarazhangrui/follow-builders
