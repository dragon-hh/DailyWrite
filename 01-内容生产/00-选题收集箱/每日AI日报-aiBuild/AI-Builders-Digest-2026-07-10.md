AI Builders Digest — 2026-07-10

## X / TWITTER

### Swyx
Swyx 今天的重点是“人味”和“模型生产化”。他赞赏 Theo 的 keynote 没有走那种 AI 生成感很重的“专业幻灯片”路线，而是用 Excalidraw / tldraw 式手绘风格传递人的思考和简洁表达。更实质的一条是他指出，很多 agent labs 对使用中国模型很谨慎，因为要卖给政府/国防客户；他认为 Cognition 团队真正难的部分在于做了多语言宣传与审查 eval、在 post-training 中校正，并把服务做到便宜且 1000 tok/s。
来源：
https://x.com/swyx/status/2074953099748450346
https://x.com/swyx/status/2074919183947808881

### Josh Woodward，Google / Google Labs / GeminiApp VP
Josh Woodward 直接向用户征集 GeminiApp 的短板：哪些能力现在还做不好，而且本该早就修好。这不是产品发布，但很像一个明确的产品反馈入口，说明 GeminiApp 团队正在主动找长期体验债。
来源：
https://x.com/joshwoodward/status/2074847444823674883

### Boris Cherny，Anthropic Claude Code
Boris Cherny 发布了 Claude Code 的新命令 `/checkup`。它会帮助清理未使用的 skills、MCP 和 plugins，去重本地与仓库里的 CLAUDE.md，把根 CLAUDE.md 拆成嵌套 CLAUDE.md 与 skills，关闭慢 hooks，更新 Claude Code，默认开启 auto mode，并预批准常被拒绝的只读命令。关键点是 `/checkup` 在改动前会先确认，定位很清楚：减少上下文浪费和本地配置熵。
来源：
https://x.com/bcherny/status/2074997570317779038
https://x.com/bcherny/status/2074997571563479143
https://x.com/bcherny/status/2074997911348244930

### Thibault Sottiaux，OpenAI Codex & ChatGPT
Thibault Sottiaux 的信号很简单：OpenAI 本周在 shipping。他提到 10am 的 livestream，并用深夜办公室堆满寿司和 tacos 的场景暗示团队处在发布冲刺中。
来源：
https://x.com/thsottiaux/status/2074885402918601082
https://x.com/thsottiaux/status/2075103845114663325

### Nan Yu，Linear 产品负责人
Nan Yu 给了一个很实用的 Product Marketing 判断：PMM 写的不是一段只给当前受众看的故事，而是一段会被受众继续转述给下一层受众的故事。她列出的传播链包括 PMM 到销售再到客户、PMM 到客户再到同行、PMM 到用户再到买家、PMM 到 champion 再到组织。另一条则借《Glengarry Glen Ross》里的奖励结构讲 power law：第一名拿车，第二名拿牛排刀，第三名出局。
来源：
https://x.com/thenanyu/status/2074907752829223043
https://x.com/thenanyu/status/2074901281466896694

### Cat Wu，Anthropic Claude Code + Cowork
Cat Wu 预告了一场 Claude Tag walkthrough：从单人 Claude Code 走到多人 Claude Tag，再深入 Claude Tag 的工作方式。她给出的产品演进线很清楚：AI 从“补完句子”，到“写完整功能”，再到 Claude Tag 能监控 channel、主动做事、让整个团队一起 steer，并记住上周告诉它的内容。
来源：
https://x.com/_catwu/status/2074925531519468012

### Thariq，Anthropic Claude Code
Thariq 认为大家应该更新对软件工程的模型：rewrite 可以是好、便宜、快的。他承认大多数 app 不像 Bun 那样容易测试和验证，但判断是模型会继续补上这些缺口。核心信号是 AI coding 让“重写”从高风险大工程，逐步变成可评估、可验证的常规选项。
来源：
https://x.com/trq212/status/2074993112217461020

### Amjad Masad，Replit CEO
Amjad Masad 反问：什么时候停止拿 autonomous agents 和手写代码比较？他类比说，我们不会看到 compiler 和工程师手写 assembly 比较。这是在推动一个评价框架转变：agent 应该作为更高层抽象被评估，而不是永远拿最低层实现方式做基线。他还询问 Replit 是否应该加入 CAD 3D modeling，透露 Replit 对软件创作边界的兴趣可能不止传统 app/code。
来源：
https://x.com/amasad/status/2075080984211624154
https://x.com/amasad/status/2075003156745089264

### Guillermo Rauch，Vercel CEO
Guillermo Rauch 的判断是：AI 会让所有软件都变成 Native，强调 uncompromising performance 和平台亲和性。他还宣布 Grok 4.5 已面向所有 Vercel customers 可用，并提到 agent stack 的多个组件正在拼起来，可能会驱动他的个人 productivity agents。
来源：
https://x.com/rauchg/status/2075018147330232707
https://x.com/rauchg/status/2074920996201796067
https://x.com/rauchg/status/2074874713143460150

### Aaron Levie，Box CEO
Aaron Levie 认为最新 AI 模型在复杂知识工作任务上已经非常强，尤其是法律、专业服务、医疗等复杂领域。他把 Grok 4.5 也列为一个在成本与性能上值得注意的新 entry，并判断随着模型在 coding、math、reasoning 和关键垂直领域上继续提升，企业数据和文档上的应用会出现更多跃迁。
来源：
https://x.com/levie/status/2075073587015516228

### Ryo Lu，Cursor 设计
Ryo Lu 把 Grok 4.5 进入 Cursor 称为“新时代的开始”，邀请用户在 Cursor 里试用并反馈体感。这条本身信息不长，但和 Vercel、Box 等人的 Grok 4.5 讨论连在一起看，说明新模型正在快速进入 builder 工具链。
来源：
https://x.com/ryolu_/status/2074951992884244606

### Matt Turck，FirstMark Capital VC
Matt Turck 的一句话很像今天内容趋势的侧写：AI content 正从 slop 走向“wait, this kinda slaps”。也就是说，生成内容正在从明显粗糙、模板化，走向让人意外可看的阶段。
来源：
https://x.com/mattturck/status/2074908816274034896

### Zara Zhang，Builder
Zara Zhang 提了一个被很多团队低估的问题：当每个人都买了 Codex Max、每天主要通过和自己的 Codex 对话完成工作后，人和人之间的协作可能会下降。她观察到会议被取消、协作减少、团队文化变差，因此认为 enterprise AI 不能只停在 single-player 或 human-agent collaboration，下一步应该是 human-human-agent collaboration。她也指出 Codex 的 frontend design 能力是限制自己更高频使用它的单点瓶颈。
来源：
https://x.com/zarazhangrui/status/2075004775436005687
https://x.com/zarazhangrui/status/2075003007520096416
https://x.com/zarazhangrui/status/2074998060162375832

### Nikunj Kothari，FPV Ventures Partner
Nikunj Kothari 认为“polished”正在越来越快地和 slop 绑定，因此会出现一次向 raw and human 的回摆。他还观察到开发者在 Codex 和 Claude Code 模型之间的摇摆非常剧烈，几乎每周都在“完了”和“又回来了”之间切换。这说明 AI coding 市场竞争已经足够强，用户的工具偏好会被每次模型和产品更新迅速重置。
来源：
https://x.com/nikunj/status/2075033190708961675
https://x.com/nikunj/status/2074878958525657452

### Peter Steinberger，OpenClaw + OpenAI
Peter Steinberger 澄清：OpenAI 雇佣的是他本人，不是 OpenClaw；OpenClaw Foundation 是独立的，有 sponsors 而不是 owners，并且第一次有了全职团队来保持 OpenClaw 稳定。他还展示了 agents 使用 nameplate 在需要用户输入时提供额外上下文的例子。
来源：
https://x.com/steipete/status/2075046949896736835
https://x.com/steipete/status/2074969319042363808
https://x.com/steipete/status/2074923615817200085

### Dan Shipper，Every CEO
Dan Shipper 预告 Every 订阅用户周五会拿到一个 prompt 和开源 repo，并表示某个内容发布把 stakes 提高了。结合今天播客内容，他的重点仍是把 AI 使用方法产品化、模板化，让订阅用户能直接复用。
来源：
https://x.com/danshipper/status/2074882061869961585
https://x.com/danshipper/status/2074953690876612764
https://x.com/danshipper/status/2074967404212298072

### Aditya Agarwal，South Park Commons General Partner
Aditya Agarwal 给 founders 的提醒很直：不要浪费这个时刻，要最大化野心。他认为现在只做纯软件已经不一定能像五年前那样捕获价值，South Park Commons Founder Fellowship 想找的是 hardware tinkerers、mad scientists、biohackers、会亲手碰 atoms 的人。如果仍然只做软件，那至少要有一个会被朋友嘲笑的 thesis，因为“heresy is the price of ambition”。
来源：
https://x.com/adityaag/status/2074892507306238235
https://x.com/adityaag/status/2074892952233705956

## OFFICIAL BLOGS

### Anthropic Engineering：An update on recent Claude Code quality reports
Anthropic 解释了最近 Claude Code、Claude Agent SDK 和 Claude Cowork 质量下降报告的原因，并明确说 API 未受影响。问题来自三次独立变更：3 月 4 日把 Claude Code 默认 reasoning effort 从 high 改成 medium，后来发现这是错误权衡并在 4 月 7 日回滚；3 月 26 日为了降低恢复 idle session 的延迟而清理旧 thinking，但 bug 导致后续每轮都持续清理，让 Claude 显得健忘和重复，4 月 10 日修复；4 月 16 日加入减少 verbosity 的 system prompt，与其他 prompt 变化叠加后伤害 coding 质量，4 月 20 日回滚。Anthropic 表示截至 4 月 23 日会重置所有订阅用户 usage limits。实际启示是：agent 产品质量不只取决于模型，也强烈依赖 harness、prompt、上下文管理和默认推理预算。
来源：
https://www.anthropic.com/engineering/april-23-postmortem

### Anthropic Engineering：Scaling Managed Agents: Decoupling the brain from the hands
Anthropic 介绍 Managed Agents 的架构思想：把 agent 的 “brain” 和 “hands” 解耦。它把 agent 虚拟化成 session、harness、sandbox 三类接口：session 是 append-only 事件日志，harness 负责调用 Claude 和路由 tool calls，sandbox 是执行代码和编辑文件的环境。文章的核心观点是，harness 会编码对模型能力的假设，而这些假设会随着模型变强而过期，所以系统应该稳定在接口层，而不是绑定某个当下实现。安全上，关键是让 Claude 生成代码运行的 sandbox 永远拿不到 token；性能上，只有需要时才 provision container，让 time-to-first-token 明显下降，文中提到 p50 TTFT 下降约 60%，p95 下降超过 90%。
来源：
https://www.anthropic.com/engineering/managed-agents

### Claude Blog：New in Claude Managed Agents: self-hosted sandboxes and MCP tunnels
Claude Managed Agents 新增 self-hosted sandboxes 和 MCP tunnels。self-hosted sandboxes 让 agent 的 tool execution 运行在用户自己的基础设施或 Cloudflare、Daytona、Modal、Vercel 等 provider 上，而 orchestration、context management、error recovery 仍在 Anthropic 侧。MCP tunnels 则让 agents 能访问私有网络中的 MCP servers，不需要把内部数据库、私有 API、知识库或 ticketing systems 暴露到公网；部署的轻量 gateway 只发起 outbound connection。对企业用户来说，这两项能力的共同意义是：让 agent 进入真实内网工作流，同时把文件、repo、网络策略、审计日志和 secrets 留在企业边界内。
来源：
https://claude.com/blog/claude-managed-agents-updates

## PODCASTS

### AI & I by Every：How a Writer Uses AI Without Losing His Voice
核心 takeaway：最有意思的不是“写作者要不要用 AI”，而是一个写作者如何把 AI 放在工具层，同时保护自己最稀缺的深度注意力和个人声音。

这位受访写作者的态度很克制：他大量用 AI 做 coding、重构、内部工具和研究助手，但明确不让 AI 进入自己的写作声音。他早上不碰互联网，不看手机，甚至有一台只能写作、不能做“有趣事情”的 laptop，因为一旦碰手机就会感到化学层面的注意力切换。他对 AI 的判断也不浪漫：它能帮人做非常厉害的工作，但也像老虎机一样有 dopamine pull。

最 builder 的部分是他的 n-of-one software 实践。他用 AI 重建了 newsletter software，把原本一年约 67,000 美元的 Campaign Monitor 成本，降到 Amazon SES 等基础设施上可能一年约 150 美元；还为会员做了一个叫 The Good Place 的私密社交空间，帖子一周后消失、每天只能发两条、无算法、按时间倒序。他的判断是，AI coding 会带来一个工具建造的黄金时代：个人可以为自己的具体工作流造软件，市场上也会出现更多针对 incumbents 的轻量竞争。

但他对创作边界很硬：AI 可以做研究助手，比如找资料、整理链接、补 TK；真正写作时，他仍然要保留那个“会写奇怪书的人”的部分。最值得记住的一句是：“if you're not touching it, if you're not using it, if you're not building with it, you can't really comment on it.” 也就是说，批评或拥抱 AI 之前，先亲手用它做东西。
来源：
https://www.youtube.com/watch?v=7ND0lQmLJlA

Generated through the Follow Builders skill: https://github.com/zarazhangrui/follow-builders
