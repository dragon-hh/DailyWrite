# AI Builders Digest：2026-09-13

## X / TWITTER

### OpenAI Codex 与 ChatGPT 团队 Thibault Sottiaux

Thibault Sottiaux 汇总了 Astra 本周密集上线的能力，包括 Images 2.5、GPT-Live-1、Agents API、Data Agent 和 ChatGPT for Financial Services，而且这还不是 DevDay。随后他说明团队已修复几类影响 Astra 质量的问题：旧模型 Skill 误触发或妨碍自检、一项可能导致提前停止或回复旧消息的上下文实验，以及配置不当、导致长尾流量质量下降的引擎；其中上下文实验估计影响了约 4,000 至 5,000 名用户，现已停用。他还宣布 Git AI 团队的 Aidan 与 Sasha 加入 OpenAI，Git AI 将继续保持开源，用于帮助企业理解 coding agent 对代码库的实际贡献。

https://x.com/thsottiaux/status/2098639827084480864

https://x.com/thsottiaux/status/2098612714704891959

https://x.com/thsottiaux/status/2098569976143806918

### AI 教程创作者 Peter Yang

Peter Yang 决定把所有本地定时任务放在 Codex，把云端任务迁到 Grok Bot，以本地和云端形成清晰分工。他同时对“软件工厂”叙事保持怀疑：当前 AI 更适合验证和测试，还不足以在没有人类定义需求、检查工作的情况下，端到端自我改进产品或构建新功能；夜间循环只要做错一个假设，就可能把后续 token 全部浪费掉。

https://x.com/petergyang/status/2098614492066435228

https://x.com/petergyang/status/2098565668241334366

### Meta AI 高级总监 Madhu Guru

Madhu Guru 认为，多数企业 AI 项目失败，不是因为缺少模型，而是沿用了旧的软件产品打法：由中央团队脱离一线工作流搭平台、低估 evals，并让缺少 AI 产品经验的人领导转型。她建议企业把 evals 作为一等公民，并把最强的 AI builder 嵌入财务、销售、客服等具体职能，与实际使用者共同重做流程。

https://x.com/realmadhuguru/status/2098448235048378456

### Anthropic Claude Code 团队 Thariq

Thariq 推出 plugin evals，帮助开发者判断自己的 Skill 在新模型发布后是否仍然有效，可在插件目录运行 `claude plugin eval init` 初始化。他也提醒，不要只看 pass/fail 分数解释 eval：不少失败来自过度严格的隐藏测试，有时模型答案本身甚至比预设结果更合理。

https://x.com/trq212/status/2098531560643539440

https://x.com/trq212/status/2098490139798655427

### Replit CEO Amjad Masad

Amjad Masad 宣布 Replit 收购了一家完全基于 Replit 构建的公司，并判断这会是未来多起同类收购中的第一起。这释放出一个值得关注的信号：AI 开发平台不只提供工具，也可能沿着平台内原生公司的成长路径向下游整合。

https://x.com/amasad/status/2098548464452055437

### Vercel CEO Guillermo Rauch

Guillermo Rauch 表示，Tailscale 的 model router 底层使用 Vercel AI Gateway。他把 AI Gateway 类比为新一代 CDN：直接连接模型源站会很脆弱，自建路由又昂贵且麻烦，因此统一网关正成为多模型基础设施中的标准层。

https://x.com/rauchg/status/2098531157230969062

### Box CEO Aaron Levie

Aaron Levie 介绍了把 Box 挂载到 agent sandbox 的新方式，让 agent 能更方便地读写其运行环境中的文件。他的判断是，当 AI agent 开始执行企业关键流程时，也需要获得人类员工长期拥有的基础能力，而受控的企业内容访问正是其中之一。

https://x.com/levie/status/2098478938003841123

### Cursor 设计师 Ryo Lu

Ryo Lu 宣布 Cursor 已加入面向大型创意项目的 long-lived agents。这个方向意味着 coding agent 不再只处理一次性短任务，而是开始承接需要持续上下文和更长执行周期的工作。

https://x.com/ryolu_/status/2098324260867772806

### Builder Zara Zhang

Zara Zhang 认为，“一人公司”被高估了。AI 的确让个人产能大幅提高，但从零构建新事物仍可能非常孤独；共同头脑风暴、一起承受挫折并庆祝进展的伙伴，往往是维持长期动力的关键，而不只是成本项。

https://x.com/zarazhangrui/status/2098483800456179923

### FPV Ventures 合伙人 Nikunj Kothari

Nikunj Kothari 指出，风险投资中的成功归因会在热门项目和大额退出出现后变得格外激烈，因为稀缺的退出与账面增值直接影响下一只基金的募资。新兴 GP 尤其容易被从成功叙事中抹去，因此真正可靠的长期信用并不来自机构改写的历史，而来自创始人的实际评价。

https://x.com/nikunj/status/2098550718923997430

### OpenClaw 与 OpenAI 团队 Peter Steinberger

Peter Steinberger 为 CUA 提交了一个 Linux 按键可靠性补丁，说明真实环境中的 computer use 仍需要扎实的底层输入修复。他还展示了 Astra 在 OpenClaw 云端会话里通过 CUA 玩 Doom 的实验，并幽默地评价它“还不算 AGI，但大概已经胜过苍蝇的大脑”，体现了通用模型、agent runtime 与电脑操作框架正在更紧密地组合。

https://x.com/steipete/status/2098527982709256637

https://x.com/steipete/status/2098527519213604889

### Every CEO Dan Shipper

Dan Shipper 认为，更高的公开 benchmark 分数并不能说明模型能否做好你的真实工作。Every 过去三年一直用实际任务做新模型的长篇 vibe check，现在又搭建了内部平台，让每个人都能基于日常工作创建个人 benchmark，把原本偏主观的体验判断逐步变成可量化、可重复的评估。

https://x.com/danshipper/status/2098481799047647715

## PODCASTS

### No Priors：Coinbase’s Everything Exchange: Agentic Finance, Stablecoins, and Tokenization with CEO Brian Armstrong

**核心结论：**当 AI agent 能自主购买数据、调用服务和执行交易时，金融账户与低成本支付能力会成为 agent 基础设施，而不是传统金融产品的附属功能。

Coinbase 联合创始人兼 CEO Brian Armstrong 描绘了三条正在汇合的路径。第一，股票、商品、crypto、衍生品和预测市场逐步上链，形成 Everything Exchange。第二，stablecoin 把全球转账压到一秒以内、成本低于 1 美分。第三，Agentic Finance 让人类获得 AI 财务顾问，也让 agent 拥有隔离资金账户或 self-custodial wallet，能够自行支付、交易和购买工具服务。

关键矛盾在微支付。传统银行卡通常有约 30 美分固定费用，而 Coinbase 观察到约 76% 的 agent 电商交易低于 30 美分，常见场景是搜索、金融数据或 agent 之间的专业工具调用。Armstrong 的说法很直接：“我们不想让 AI 没有银行账户。” Coinbase 孵化并交给 Linux Foundation 的 X402 协议，正试图让 Google、Cloudflare、AWS 等参与者共同建立这类支付轨道。

他也分享了 Coinbase 内部的 agent 实践：为团队和代码仓库维护一套“公司大脑”，把事故历史、财务控制、A/B 测试和 PR 经验放进可读取的 Markdown。人类审查发现遗漏时，不只修当前代码，还把新上下文写回这套大脑，让后续一次通过的 PR 比例持续上升。内部 harness Toshi 已能拆分复杂功能、并行调度多个 agent，并通过 X402 调用和支付外部服务。

这套思路延伸到 Brian 参与创办的 New Limit。团队用 AI 从巨大的转录因子组合中选择下一轮实验，已在动物模型中完成至少一种人类细胞类型的成功重编程，并计划明年启动首个一期临床试验。共同逻辑是：AI 的价值不只在生成答案，而在进入能支付、行动、接受反馈并持续改进的真实系统。

https://www.youtube.com/watch?v=uLDK4l_-gUE

Generated through the Follow Builders skill: https://github.com/zarazhangrui/follow-builders
