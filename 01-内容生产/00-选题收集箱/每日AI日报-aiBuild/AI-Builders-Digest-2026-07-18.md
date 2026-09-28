# AI Builders Digest — 2026-07-18

## X / TWITTER

### Google VP Josh Woodward

Josh Woodward 回顾了 NotebookLM 的起点：Steven Johnson 展示写书方法的一次演示，催生了团队内部一直简称为“Notebook”的小项目。如今它已有超过 3000 万用户和 60 万个组织使用，团队也正式对外采用 Notebook 这一名称。

来源：https://x.com/joshwoodward/status/2077811657385079045

### Anthropic Claude Code 团队的 Boris Cherny

Boris Cherny 认为，AI 编程真正的回报不是多写几行代码，而是让修复和维护在后台自动完成，使团队能投入过去根本无暇触及的工作。落地时应让 Claude 端到端验证自己的结果，启用权限 auto mode、自动代码与安全审查，并用 Agent view、`/loop`、`/batch`、动态工作流和 worktree 隔离来管理多个 agent。衡量回报也不能只看使用量，而应追问：这项工作原本是否值得工程师手工做，要花多少工程工时。

来源：

- https://x.com/bcherny/status/2077929390806073807
- https://x.com/bcherny/status/2077929397495959693
- https://x.com/bcherny/status/2077929404219474148

### OpenAI Codex 与 ChatGPT 团队的 Thibault Sottiaux

Thibault Sottiaux 公布了 ChatGPT 桌面端的调整：侧边栏现在展示对话历史和 Projects，Chat 与 Work 历史可在 Web、移动端和桌面端同步，但本地任务仍只保留在电脑上；用户也能在桌面端更方便地切换 Chat 与 Work 模式。Codex 模式保持不变，团队会继续修复细节问题并改善性能、可靠性和效率。

来源：https://x.com/thsottiaux/status/2077928427936710901

### AI 教程创作者 Peter Yang

Peter Yang 指出 Claude Code 当前除 Drive 外缺少其他 Google Workspace connector，而 ChatGPT 已覆盖更多连接能力；他同时对 Claude Code 的 browser use 体验表达不满。这两点都指向 agent 产品在外部工具集成和浏览器可靠性上的现实短板。

来源：

- https://x.com/petergyang/status/2077968093406707970
- https://x.com/petergyang/status/2077966904938127502

### Meta AI 高级总监 Madhu Guru

Madhu Guru 判断，Kimi、GLM 等 open-weight 模型将迫使企业重新设计 AI 技术栈，核心是保持模型可替换性。他建议建立贴近业务的回归 eval 与高难度“爬坡”eval，提高 eval 运行速度；基于质量、成本和延迟自行做 model routing；再用 model-agnostic harness 统一 prompt、上下文、工具定义和输出解析，避免业务系统感知底层具体模型。

来源：https://x.com/realmadhuguru/status/2077885624607228018

### Google Labs

Google Labs 回顾 Project Tailwind 从早期实验成长为 NotebookLM 的过程，并宣布该产品如今成为 Gemini Notebook。它体现了 Google 将 Labs 实验逐步产品化并纳入 Gemini 品牌体系的路径。

来源：https://x.com/GoogleLabs/status/2077832590132949268

### Replit CEO Amjad Masad

Amjad Masad 分享了一款仍在开发中的国际象棋引擎：先用 200 万个 Stockfish 标注局面进行 fine-tuning，再做一次较短的 GRPO 强化学习，当前表现似乎已超过 frontier model 的国际象棋能力，并附有实验、代码注释和教程。他还调侃蒸馏模型可能超过教师模型，呼应了 open model 性能快速提升的话题。

来源：

- https://x.com/amasad/status/2077908032944779732
- https://x.com/amasad/status/2077908318975332417

### Vercel CEO Guillermo Rauch

Guillermo Rauch 称 Kimi K3 在其引用的综合 Web 工程 benchmark 上超过 Fable，以更短时间达到相近成功率，这是 open model 首次领先所有 proprietary model；不过他也提醒 benchmark 不是全貌，目前最佳模型完成率最高为 92%，在获得帮助时为 96%。此外，Vercel 邀请 React 早期推动者 Pete Hunt 领导 Frameworks 与 Next.js，并让 GraphQL 共同发明者 Nick Schrock 负责 Agentic Developer Experience，目标是服务未来海量 agent 和 self-improving software。

来源：

- https://x.com/rauchg/status/2077900518404321759
- https://x.com/rauchg/status/2077870043833229692

### Box CEO Aaron Levie

Aaron Levie 认为，open model 将 frontier intelligence 的成本继续压低，会释放大量此前受 token 成本限制的企业工作流，也让 applied AI 层能按任务调优和路由不同模型。Box 与 Databricks 的集成则展示了具体方向：企业可从合同、财务文档、供应链资料等非结构化内容中提取结构化数据，在不搬移或重新处理原内容的情况下与 ERP、CRM、产品分析数据联合查询。

来源：

- https://x.com/levie/status/2077857617859535112
- https://x.com/levie/status/2077782120232350205

### FirstMark VC Matt Turck

Matt Turck 与 OpenAI 工业计算负责人 Sachin Katti 聚焦 AI 基础设施扩张：数据中心如何把电力转成 token、为何液冷和电网成为关键约束，以及 inference 可能开始主导算力需求。对谈还涉及 Stargate、OpenAI 自研 Jalapeño 芯片、tokens per watt、十万 GPU 的网络问题、数据中心融资，以及 OpenAI 为什么认为“建得不够快”比过度建设更危险。

来源：https://x.com/mattturck/status/2077791541167268243

### Builder Zara Zhang

Zara Zhang 分享了一款来自中国的硬件创意：把口罩同时做成麦克风，让用户在公共场所使用语音输入时不被旁人听见。这个设计试图直接解决 voice-first AI 在公共空间中的隐私和社交阻力。

来源：https://x.com/zarazhangrui/status/2077953473535176772

### Every CEO Dan Shipper

Dan Shipper 对“Kimi K3 已与 Fable 同级”的说法保持强烈怀疑，准备亲自进行实际体验验证。他同时复盘 OpenAI 的 agentic coding 转向：早期 GPT-5 更像 pair programmer，独立的 Codex 模型和产品线随后快速成熟，Codex Desktop 借助后来者优势形成更干净的体验，最终又成功并回 ChatGPT，成为一次少见的主产品自我颠覆。

来源：

- https://x.com/danshipper/status/2077839678636732809
- https://x.com/danshipper/status/2077825318992429286

### South Park Commons GP Aditya Agarwal

Aditya Agarwal 表示自己正在把系统从 Fable 切换到免费替代模型，因为当效果足够好时，继续支付高价缺乏理由。他进一步提出一个尖锐问题：如果别人一使用某项“高价值”能力就能复刻它，那么它原本的护城河可能并没有想象中深。

来源：

- https://x.com/adityaag/status/2077983435000324125
- https://x.com/adityaag/status/2077983583168278961

### Sam Altman

Sam Altman 表示，新 voice model 已跨过一个体验阈值，他现在与 ChatGPT 说话的频率已经超过打字。他也承认 OpenAI 过去 12 个月并非最佳状态，主要责任在自己，但预计接下来 12 个月会成为公司迄今最好的一年，并强调 AI 应让更多人获得自由、能动性和财富。

来源：

- https://x.com/sama/status/2077842579232895286
- https://x.com/sama/status/2077817060068057493

## OFFICIAL BLOGS

### Anthropic Engineering：How we contain Claude across products

Anthropic 的核心判断是：agent 越强、权限越大，理论爆炸半径就越大，因此安全工程不能只依赖模型“更听话”，还要在环境层给能力划硬边界。Claude.ai 使用短生命周期的 gVisor container；Claude Code 面向懂终端的开发者，以 human-in-the-loop 加 OS sandbox；Claude Cowork 面向非技术用户，用本地 VM、文件挂载模式和 egress control 限制可触达范围。

数据说明了为什么批准弹窗不够可靠：用户会同意约 93% 的权限请求；一次内部钓鱼测试中，恶意 prompt 在 25 次尝试里有 24 次成功诱导 Claude 外传凭证。模型层同样不是绝对防线，Claude Code auto mode 能拦截约 83% 的过度主动行为，但仍会漏掉一部分。文章最值得记住的一句是：“The deterministic boundary is what gets hit when everything probabilistic misses.”

实践启示包括：先解析 symlink 再校验路径；把 allowlist 当作能力授权，而不只是域名过滤；警惕持久记忆投毒、multi-agent 信任升级和远程 connector 的动态风险；优先使用经长期检验的 hypervisor、seccomp、gVisor 等基础组件，因为真正暴露问题的往往是团队自建代理和策略层。

来源：https://www.anthropic.com/engineering/how-we-contain-claude

## PODCASTS

### Unsupervised Learning：Ep 91: Top AI Analyst Unpacks Today&apos;s AI Hype Cycle

**核心结论：AI 很可能像互联网和移动端一样成为重大平台变迁，但真正值得研究的不是它到底“比工业革命大几倍”，而是价值会落在哪一层、哪些具体产品能形成高频需求。**

科技分析师 Benedict Evans 用历史平台周期拆解当前热潮。他提醒，foundation model 的竞争未必复制 Windows，因为 LLM 缺少相同的网络效应；更可能出现的局面是基础设施承担高投入和边际成本，而大量价值向应用层转移。当前软件开发已明确找到 product-market fit，但普通消费者多数仍只是偶尔使用 AI。真正的鸿沟不是模型 demo 是否惊艳，而是产品能否把能力变成每天都会用、能解决具体问题的体验。

Evans 对就业和 AGI 叙事保持克制。模型能力的物理上限确实未知，但企业采用还受流程拆解、组织优先级、合规和部署速度制约。正如云计算二十年后也只覆盖部分企业工作流，AI 不会因为实验室进展快就瞬间改造所有行业。他的建议很直接：“Meanwhile, let's build some stuff and work out what works.” 与其沉迷终极隐喻，不如先做产品、观察真实行为。

他还强调 AI 是 enabling technology，不只是生成文字和图片。未来许多价值会藏在欺诈检测、后台流程和用户看不见的系统改进里，就像互联网的关键不只是聊天室，而是网络本身。但也应默认今天的一批协议、产品和公司会失败，有些行业会被彻底重构，另一些行业可能变化有限。最终仍要回到商业基本面：技术再新，低毛利转售生意依然可能只是低毛利转售生意。

来源：https://www.youtube.com/watch?v=vDY_ocrkQ5w

Generated through the Follow Builders skill: https://github.com/zarazhangrui/follow-builders
