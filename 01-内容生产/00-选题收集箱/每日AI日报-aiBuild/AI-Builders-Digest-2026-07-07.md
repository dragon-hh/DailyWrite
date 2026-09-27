AI Builders Digest — 2026-07-07

## X / TWITTER

### Nan Yu，Linear 产品负责人

Nan Yu 对“同时开 10 个 Claude Code 标签页”的炫技不买账。他认为，把 agent 管理成“即时战略游戏”的模式已经走进死胡同，因为即使是按当下标准已经过时的 AI，也能在微操层面击败 99% 以上的人类玩家。真正的问题不是人类能不能多开几个窗口，而是交互和编排方式本身要升级。

来源：
https://x.com/thenanyu/status/2073920959011074292
https://x.com/thenanyu/status/2073920326304460847

### Amanda Askell，Anthropic AI 哲学家与伦理研究者

Amanda Askell 把“让医生给出概率”形容成生活里没必要存在的 boss battle。她指出，即使你明确要求一个区间式的主观概率，医生给出的本质也只是判断和直觉，但现实里这种信息又经常被法律风险、责任边界或沟通习惯卡住。

来源：
https://x.com/AmandaAskell/status/2073786264059625897

### Cat Wu，Anthropic Claude Code / Cowork

Cat Wu 分享了一个 Claude Code + workflows + artifacts 的招聘用例：先告诉 Claude Code 岗位和候选人画像，再让它启动动态 workflow 找 100 个候选人，补齐 LinkedIn、Twitter、博客、播客和一句话推荐理由，最后生成 artifact 并发邮件。她的重点不是“AI 帮我搜人”这么简单，而是把一整段候选人 sourcing 流程变成可离线运行、可移动端复查的 agent 工作流。

来源：
https://x.com/_catwu/status/2073806626965049686

### Garry Tan，Y Combinator CEO

Garry Tan 的核心判断很直接：人类财富的真正约束从来不是资源，而是“服务彼此的好点子”和执行杠杆；现在杠杆约束被大幅削弱，剩下的就是想法本身。他还用日本的例子说明，当增长天花板存在时，系统会转向“更好”的竞争：更好的铁路、服务和工艺。放到 AI builder 语境里，这像是在提醒创业者：AI 让“更多”和“更好”同时变得可追求，但稀缺项会回到创意和判断。

来源：
https://x.com/garrytan/status/2073881439700168925
https://x.com/garrytan/status/2073881438123110512

### Zara Zhang，Builder

Zara Zhang 重新提到自己之前做的一个 skill，并补了一句“现在理解代码又流行起来了”。可用信息不多，但它指向一个明显趋势：围绕代码理解、上下文提取和可复用 agent skill 的需求正在变热。

来源：
https://x.com/zarazhangrui/status/2073768913310200310

### Nikunj Kothari，FPV Ventures 合伙人

Nikunj Kothari 对传统 VC 沟通效率有点不耐烦：他还在等那种会先要求 VC 试玩产品、带着至少两条反馈再来聊天的 founder。他认为，比起反复 Zoom 讲同一套 deck，双方如果先把各自的“个人 prompt”交给 Claude 做数字化预处理，线下对话就能更多用于产品 brainstorm 或真正互相了解。

来源：
https://x.com/nikunj/status/2073903310982218088

### Peter Steinberger，OpenClaw + OpenAI

Peter Steinberger 推荐了一个资源，并强调“Can’t recommend enough”，同时给出了使用入口。JSON 里没有提供被引用内容的完整上下文，所以这里只保留这个明确的推荐信号和原始链接。

来源：
https://x.com/steipete/status/2074007001802367446

### Dan Shipper，Every CEO

Dan Shipper 连续调侃 Fable / ultracode 式的 agent 工作流：一句“make no mistakes”可以变成 agent 自我扩张的指令，“改个按钮颜色”也可能触发 100 个 agent 的舰队。笑点背后其实是同一个产品问题：agent 系统需要知道什么时候该重兵投入，什么时候只是一个小改动。

来源：
https://x.com/danshipper/status/2073894034225897602
https://x.com/danshipper/status/2073764166700048480

### Sam Altman

Sam Altman 把孩子第一次把两个词连在一起，和 GPT-5.6 发现新数学相提并论。它不是产品发布，但这个类比挺说明他关注的东西：语言组合、认知跃迁，以及人类和模型在“突然会了某件事”时带来的惊讶感。

来源：
https://x.com/sama/status/2073791666553844074

## OFFICIAL BLOGS

今天 JSON 中没有新的官方博客内容。

## PODCASTS

### No Priors：Really Big Test-Time Compute in AI Changes Benchmarks, Safety and Research with OpenAI Research Scientist Noam Brown

最重要的一句话：今天评估 AI 模型，不能只问“模型有多强”，还必须问“你给了它多少 test-time compute 预算”。

OpenAI 研究科学家 Noam Brown 讨论了大规模 test-time compute 如何改变 benchmark、安全评估和研究节奏。他的核心观点是，过去 GPT-3 时代模型即使拿到更大推理预算，也很难显著扩展能力；但现在模型能力会随着 token、时间、成本和 scaffolding 预算增长而持续提升。因此，一个 benchmark 上的单一分数越来越容易误导人，应该改成在固定预算下比较，或者画出性能随 test-time compute 增长的曲线。

最尖锐的部分在安全评估。Noam Brown 说，现有 responsible scaling policies 和 preparedness frameworks 多数诞生于 test-time compute 不重要的时期，因此没有充分回答一个问题：如果一个模型在 10 美元预算下看起来安全，在 10,000 美元甚至 10,000,000 美元预算下是否仍然安全？他在开头直接说：“The policies that exist today don't really address that question.”

他还给了一个具体的研究方向：能否只用 10、100 或 1,000 美元级别的推理实验，预测模型在 10,000 美元预算下的表现？这会成为长期 agent 时代的重要评估问题，因为某些任务上模型可以被 scaffold 成运行数周、数月，甚至理论上运行一年。Noam Brown 用 poker solver 做自己的私有 eval：早期模型几乎做不了，5.2 已经能在他引导下做 reverse solver 并加速代码，5.5 则接近零样本完成大部分 solver 工作。他的判断是，六个月到一年后，模型可能一次性完成接近他博士论文级别的 poker solver。

来源：
https://www.youtube.com/watch?v=AZrU6y3pUcU

Generated through the Follow Builders skill: https://github.com/zarazhangrui/follow-builders
