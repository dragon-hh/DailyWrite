# AI Builders Digest · 2026-07-14

## X / TWITTER

### Swyx（dxtipshq / Cognition / Temporalio / AI Engineer / Latent Space 主理人）
Swyx 抛出一个 AI agent 设计的核心观点：很多 agent 框架缺乏"反思/反向传播"机制，只是在做无差别的多次 rollouts，本质上和"反复做同一件事期待不同结果"一样疯狂。他引用爱因斯坦那句关于疯狂的调侃，来说明 inference-time compute 必须真正带来边际优势才有意义。
原文：https://x.com/swyx/status/2076345087634620528

### OpenAI Codex & ChatGPT 负责人 Thibault Sottiaux
Thibault 在周末给 Codex / ChatGPT / Team / Edu 等付费用户发了一连串"没有 nerf、只有好事"的更新：GPT-5.6 Sol 已经落地推理优化，节省下来的成本全部让利给订阅，订阅可用额度大约多 10%；之前把上下文窗口从 272k 提到 372k 后导致扣费超额，已回滚到 272k，后续会重新推 372k；推理强度（juice value）的实验参数和 high/xhigh 推理下多 agent 略微超额的问题都已经回滚或修复；5 小时限额继续暂停。GPT-5.6 Sol 至少在 Go / Plus / Pro 订阅中保留，直到下一个更强的模型上线。
原文：
- https://x.com/thsottiaux/status/2076495156757577895
- https://x.com/thsottiaux/status/2076460408437887268
- https://x.com/thsottiaux/status/2076459871021736245

### 实用 AI 教程博主 Peter Yang
Peter 观察到目前 90% 以上的用户都在用 GPT-5.6 Sol，用 Terra 和 Luna 的人不到 10%。他建议当社区情绪转向时，团队应该反其道而行，用更人性、更透明的方式沟通，而不是更官腔。他还顺手点名 Anthropic，认为他们家模型虽然好，但社区沟通可以更直接。
原文：
- https://x.com/petergyang/status/2076519927843000448
- https://x.com/petergyang/status/2076512796481880270
- https://x.com/petergyang/status/2076510899490480228

### Replit CEO Amjad Masad
Amjad 用 Replit 的 computer use 模型跟自己新写的国际象棋引擎下棋，玩得很开心。更硬核的是他在 Replit 上"vibe research"：直接微调一个 Qwen-8B 来下棋，同时跑 3 个实验分支。他感慨现在的模型做 ML 已经变得相当靠谱，只要有好直觉引导，从未做过 ML 的人也能做有趣的 ML 工作。
原文：
- https://x.com/amasad/status/2076356893736673507
- https://x.com/amasad/status/2076227936202662357

### Vercel CEO Guillermo Rauch
Guillermo 抛出一个 AI 时代的架构忠告：让模型成为你机器里的一个齿轮，而不是反过来。AI SDK 走开放模型 API，AI Gateway 走开放的 Agent API + 零数据保留（ZDR）推理，创业公司和企业的数据、评测、模型选择、软件层都必须握在自己手里，不要把大脑外包出去。
原文：https://x.com/rauchg/status/2076364176252191222

### Box CEO Aaron Levie
Aaron 抛出一个 21 世纪企业的核心架构问题：随着 intelligence 被越来越密集地塞进 AI 模型，企业怎么把决策、洞察、工作流模式和最佳实践这些 IP 价值最大化？在他看来，即使基础模型变强，企业内部那一层"独有的 leverage"反而更重要：给业务流做 evals、按 tier 路由不同强度模型、把 trace 沉淀下来反哺自己的 workflow。applied AI 这一层帮企业解决这些问题的公司，会吃到下一波 enterprise workload 的红利。
原文：https://x.com/levie/status/2076338364635287637

### 独立 builder / follow-builders 作者 Zara Zhang
Zara 强推一个 Codex 用法：把会议 transcript 当 PRD。她和同事讨论一个功能的实现，把 transcript 直接丢给 Codex，它就按讨论把 prototype 搭出来，会议本身就是 prompt。另一条短推："Passion is the biggest moat"，热情才是最大的护城河。
原文：
- https://x.com/zarazhangrui/status/2076300222884626754
- https://x.com/zarazhangrui/status/2076284012339843546

### FPV Ventures 合伙人 Nikunj Kothari
Nikunj 吐槽了 SF 的"token maxxing"现象：很多人嘴上说在跑一堆 subagent，但被问"在为谁造什么"时几乎答不上来。他提醒大家：在让 token 飞起来之前，先停下来想想你正在做（谋生）的事到底重不重要，时间是这个世界上唯一要不回来的东西。
原文：https://x.com/nikunj/status/2076458876816540144

### OpenAI CEO Sam Altman
Sam 公开向社区征集：用 GPT-5.6 Sol 做过的最酷的东西是什么？他会从 OpenAI 档案库里挑一个人送一份特别的礼物。
原文：https://x.com/sama/status/2076398253332140410

### Anthropic 官方 Claude 账号
Anthropic 宣布延长 Claude Fable 5 在所有付费套餐中的访问权限，并把 Claude Code 的周限额继续提升 50%，一直到 7 月 19 日。同时再次明确：周额度的最多一半可以花在 Fable 5 上，超出部分可以用 usage credits，或者切换到其它模型继续工作。
原文：
- https://x.com/claudeai/status/2076351401006154204
- https://x.com/claudeai/status/2076351399999557669

## PODCASTS

### No Priors：Valar Atomics 创始人 Isaiah Taylor 谈核能如何打开能源丰裕
**核心一句话**：核能的成本曲线，决定了 AI 时代是否有能源可用。

Valar Atomics 创始人兼 CEO Isaiah Taylor 在 Utah 的 San Rafael 实验场里接受了 No Priors 的现场采访。他不是传统意义上的核工业人：曾祖父是曼哈顿计划的核物理学家，他自己从六岁起就想造"成千上万台机器"。他花了十年观察整个核工业，得出一个判断：核电行业过去几十年本质上是一家"建模与仿真公司"，并没有真正在迭代硬件。所以他创立 Valar，用 startup 思路从第一性原理重做核裂变。

他认为今天的核电行业被"老一代大型轻水反应堆 + NRC 商业路径"的范式锁死。过去十年绝大多数核能 startup 都试图走 NRC 的商业审批，但 NRC 的设计目的是"成熟系统的大规模商用部署"，对于"想把钢弯一弯、让原子裂变一下"的早期团队完全不友好。Valar 走的是另一条路：DOE 的 testing pathway，加上 EO 14301 这道行政命令要求"7 月 4 日前有三台先进反应堆在美国本土达到临界"，把"先有数据还是先过审批"这个死循环打破了。

他强调 Valar 是一家"硬件执行公司"，不是设计公司，"丰田凯美瑞问题"才是真正的核工业问题：把反应堆做得尽可能简单、便宜、安全，能造几万台，而不是去造一辆"兰博基尼"。他用 video game 里的"tick rate"来衡量公司节奏：从公司成立到第一次裂变原子用 2 年 4 个月，从 Project Nova 第一次裂变到 Ward 250 第二次用 7 个月，目标是把这个间隔压缩到几分钟。

他反复强调的一点是"consequence reduction 而非 odds reduction"。传统核电把几乎所有工程力量都花在"确保事故永远不会发生"上，但 odds 是随机的。Valar 的反应堆用 TRISO 燃料、石墨慢化、氦气冷却，配上"Modular Citadel"（带正弦曲线接缝、无钢筋、无螺栓、无灌浆、自堆叠的预制混凝土块，78 英寸厚），再加上 RCCS 被动冷却系统做"失电 + scram"测试：scram 之后立刻关掉所有电力、循环泵、RCCS 泵，只靠物理几何把余热在两天内带走，本质熔毁就不可能发生。他提到美国核电里那些报价 45 万美元一个的信号放大器盒、报价 500 万美元还要等两年半的反应堆保护系统（RPS），都被 Valar 自己 5 个工程师花 6 周、40 万美元自研替代了。

最后他说，能源是宇宙里唯一不可逆的稀缺资源，只要你能把能源做得更便宜，需求就会被你"诱发"出来。NVIDIA Blackwell 那块 AI 芯片已经由 Valar 的反应堆直接供电，nuclearwebsite.com 这个网站也是直接托管在反应堆上的。他给大型 compute 买家的判断是：别再用过去那批"建模仿真型"创业公司当参照系，exponentials 的速度是反直觉的。

视频链接：https://www.youtube.com/watch?v=5Xvbq_zvOQ4

---

Generated through the Follow Builders skill: https://github.com/zarazhangrui/follow-builders