AI Builders Digest — 2026-06-19

## X / TWITTER

### Thibault Sottiaux，OpenAI Codex & ChatGPT
Thibault Sottiaux 给 Codex 用户抛了两个很实用的信号：一是 Codex App、CLI 和 SDK 不只绑定 OpenAI 模型，也可以配合开源模型使用；二是一次“double reset”福利，既给用户完整重置，也额外放入 reset bank 供之后使用。对 builder 来说，重点不是福利本身，而是 Codex 正在往更开放、更可插拔的开发工具方向走。

来源：
https://x.com/thsottiaux/status/2067181377028538431
https://x.com/thsottiaux/status/2067399435009622521

### Aaron Levie，Box CEO
Aaron Levie 继续强调 Applied AI 不是“LLM 上面薄薄一层 UI”。他认为企业里的 agentic workflow 真正难在工作流、上下文、模型路由、FDE 式落地、change management、domain-specific GTM 这些细节。模型能力当然会继续提高，但企业今天就要改变，所以能把 intelligence 接到真实业务流程里的公司，会逐步形成 moat。

来源：
https://x.com/levie/status/2067455756795039957

### Guillermo Rauch，Vercel CEO
Guillermo Rauch 把 React / Next.js 的类比带到了 agent 应用上：模型竞争越激烈，AI SDK 越重要，因为世界需要一个“如何构建和部署 agents”的实际方案。他还提到，在 Vercel 的 Next.js evals 里，一个开源模型 GLM 5.2 超过了 Opus 4.8，进一步说明应用层需要能适配快速变化的模型格局。

来源：
https://x.com/rauchg/status/2067242482190979186

### Garry Tan，Y Combinator President & CEO
Garry Tan 用一个粗略测算表达了 frontier AI coding 工具停用带来的生产力损失：如果 500 万开发者中有 17.8% 的工作被路由到 Fable，且 Fable 平均提升 15% 生产力，那么禁用可能造成约每小时 1200 万美元的吞吐损失。他还强调 AI 正在让技术创始人获得商业思考、商业创始人获得技术思考，结果可能是更多“真的能运转”的创业公司。

来源：
https://x.com/garrytan/status/2067366749411176831
https://x.com/garrytan/status/2067308407603048774
https://x.com/garrytan/status/2067260431597723825

### Zara Zhang，Builder
Zara Zhang 的两条提醒都很像“vibe coding 时代的产品常识”：不要在形成自己 taste 和 voice 之前就依赖 AI 写作，否则 AI 产出低质量内容时你甚至识别不出来；个人 app 也是一样，做出来只要一天，但验证自己会不会真的用，至少要一周。很多产品不是技术没跑通，而是默认用户会每天记得打开、按步骤操作，但真实的人懒、会忘、会中断，产品要为这种人设计。

来源：
https://x.com/zarazhangrui/status/2067423674689638652
https://x.com/zarazhangrui/status/2067313780724551853

### Claude，Anthropic Claude 官方账号
Claude 宣布 Claude Design 进入 beta，面向所有付费计划，并同时支持 web 和 desktop。更值得注意的是 Claude Design 与 Claude Code 的双向协作：可以把设计交给 Claude Code 构建，也可以从 Claude Code 终端同步设计项目；同时支持导出 PDF / PowerPoint，并提供更稳定的编辑器、布局控制、拖拽、resize 和对齐能力。

来源：
https://x.com/claudeai/status/2067325894268428560
https://x.com/claudeai/status/2067325893001826552
https://x.com/claudeai/status/2067325891781226581

### Amjad Masad，Replit CEO
Amjad Masad 转发并概括了一个很清楚的工作流方向：“Design with Claude, Ship with Replit”。这说明 Replit 正在把自己放在 AI 设计工具之后的构建与发布层，把 Claude Design / Claude Code 这类上游创作工具和实际部署体验接起来。

来源：
https://x.com/amasad/status/2067363904183783833
https://x.com/amasad/status/2067363597110391230
https://x.com/amasad/status/2067386053980266542

### Nan Yu，Linear Head of Product
Nan Yu 提醒大家，“taste”不只是审美品味，就像“design”不只是视觉设计。很多关于 taste 的讨论之所以互相错位，是因为有人在讲产品判断、系统取舍和质量标准，另一些人以为只是在讲外观。

来源：
https://x.com/thenanyu/status/2067327619897446721
https://x.com/thenanyu/status/2067327901666521478

### Nikunj Kothari，FPV Ventures Partner
Nikunj Kothari 连续谈到 tranched rounds 的问题：他反对分批融资结构的核心理由，是它会伤害下一位加入公司的员工，因为 409A 估值可能被抬高，而员工期权却要承受一个 lead preferred investor 并未真正支付的高估值。他还给了一个识别方法：如果一家公司以公开估值融资 xxM 美元、稀释低于 10%，很可能就是 tranched round。

来源：
https://x.com/nikunj/status/2067399657639285150
https://x.com/nikunj/status/2067397092981772501
https://x.com/nikunj/status/2067378464773292066

### Dan Shipper，Every CEO
Dan Shipper 提到 Every 会不定期投资他们看好的 AI founder，并点名支持 Tacit 的使命和方法。他还把自己 2023 年写的 Against Explanations 重新拉回上下文，认为 AI 可能加速科学进展，并对“这么快看到这么多进展”感到兴奋。

来源：
https://x.com/danshipper/status/2067386342661624055
https://x.com/danshipper/status/2067386395283345808
https://x.com/danshipper/status/2067293009964630081

### Sam Altman，OpenAI CEO
Sam Altman 公开表达了对 Noam 的长期期待，说 Noam 是他从 OpenAI 一开始就最想合作的人之一，“only took 10 years”，并认为这次等待会值得。另一条则延续玩笑口吻，把 Noam 们在 AI 上的成功归因于“divine benevolence”。

来源：
https://x.com/sama/status/2067427421083652131
https://x.com/sama/status/2067427678529974740

### Aditya Agarwal，South Park Commons General Partner / Bevel Health Co-Founder
Aditya Agarwal 提到 SPC members 探索的问题，能指示 frontier 下一步会走向哪里，并邀请读者通读这些问题、申请 SPC。这里的有效信号是：SPC 继续把“高质量问题列表”当成早期 builder 和未来方向的过滤器。

来源：
https://x.com/adityaag/status/2067306242825949398
https://x.com/adityaag/status/2067306244390428893
https://x.com/adityaag/status/2067306245942317426

### Josh Woodward，Google / Google Labs / Gemini App / Google AI Studio VP
Josh Woodward 强调 Google Labs 的一个核心价值是 co-create，并用 Voltage team 的案例作为例子。信息不长，但方向很明确：Google Labs 在对外表达上继续把“和用户共创”放在产品实验文化的中心。

来源：
https://x.com/joshwoodward/status/2067337173699850487

### Swyx，AI Engineer / Latent Space / Cognition 等相关 builder
Swyx 今天的有效信号比较偏活动现场和资源分享：他提到用 Polymarket prediction markets 来估算 7 月 1 日 AI Engineer World Cup suite 成为 Team USA game 的隐含价值，也分享了一篇 paper 链接。内容本身不够完整展开，但能看出他持续把 AI builder 社群、事件运营和 prediction markets 结合起来。

来源：
https://x.com/swyx/status/2067511309609115657
https://x.com/swyx/status/2067495676972540343
https://x.com/swyx/status/2067512137405350067

## PODCASTS

### AI & I by Every: GitHub’s COO Explains Why AI Hasn’t Replaced Developers
The Takeaway：AI coding agents 没有替代开发者，反而正在把 GitHub 变成一个“人 + 多个 agents”协作的基础设施层。

GitHub COO Kyle Daigle 的核心判断很具体：GitHub 以前服务的是开发者，但现在越来越多 legal、finance 和其他知识工作者也在用 GitHub Copilot app 做小工具和内部资产。GitHub 看到的不是“代码垃圾”简单增加，而是 agent 生成的 PR、commit 和协作流量指数级增长：采访开头提到每月有 1700 万个 agent PR；Kyle 还说，如果今年线性增长，GitHub 可能会从去年全年 10 亿 commits 走向 140 亿 commits 的轨道。

对 maintainer 来说，问题不只是更多 PR，而是如何控制入口、信任和 review 成本。Kyle 的解法是给社区“building blocks”，比如 agentic code review、agentic merge、让 maintainer 决定接受谁、如何证明贡献有意义，而不是由 GitHub 先规定一个统一标准。他很清楚地说，GitHub 的原则是 “we’re not building for the buyers, we’re building for the developers”。

商业模式上，他没有给出确定答案，但承认当 agents 不睡觉、可以并行跑 150 个任务时，传统 freemium / rate limit 结构会遇到压力。GitHub 想保留开发者的核心体验，同时让重度 agent 使用在规模化场景里可持续。更大的战略信号是 developer choice：GitHub 会继续自研，也会和 Anthropic、OpenAI、Google 以及其他 coding agent / model 合作，因为开发者最终会自己选择。

来源：
https://www.youtube.com/playlist?list=PLuMcoKK9mKgHtW_o9h5sGO2vXrffKHwJL

Generated through the Follow Builders skill: https://github.com/zarazhangrui/follow-builders
