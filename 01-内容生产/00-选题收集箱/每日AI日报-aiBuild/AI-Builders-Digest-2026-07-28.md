# AI Builders Digest — 2026-07-28

## X / TWITTER

### Thibault Sottiaux，OpenAI Codex 与 ChatGPT 团队

Thibault Sottiaux 认为，ChatGPT 真正的价值不是陪聊，而是替人完成现实中的琐碎工作：谈网络账单、清理订阅邮件、寻找购买或出行方案，都可以从手机上的一个 prompt 开始。他说自己每天至少用它处理 20 件事，仍会被结果惊到。

- 原文：https://x.com/thsottiaux/status/2081444811647963244

### Peter Yang，AI 教程与访谈创作者

Peter Yang 提醒，主流用户采用 AI 的关键阻力可能不是 token 不够，而是信任。对不沉浸在 AI 圈的人来说，更现实的问题是：是否愿意让 ChatGPT 接触 Gmail、Calendar、Google Workspace 或 Microsoft Office 等高度私密的数据。

- 原文：https://x.com/petergyang/status/2081555286817648738

### Madhu Guru，Meta AI 高级总监

Madhu Guru 把 AI 产品化分成两个阶段：第一阶段，有分发能力的公司先借助 AI 快速扩展到相邻问题，把过去需要大量定制软件的功能做出来，例如虚拟试衣；这些变化尚未在整个软件生态中充分显现。第二阶段才会出现更多全新功能和真正的产品创新，届时 AI 对软件形态的影响将无法忽视。

- 原文：https://x.com/realmadhuguru/status/2081437850466451736

### Amjad Masad，Replit CEO

Amjad Masad 转述了一位前 Anthropic 员工的观察：攻击者更偏爱使用由实验室大幅补贴的 AI 订阅服务，而不是开源模型来实施攻击。这个判断把 AI 安全讨论从“开放权重是否更危险”拉回到实际攻击成本与可获得性。

- 原文：https://x.com/amasad/status/2081576172656456076

### Guillermo Rauch，Vercel CEO

Guillermo Rauch 宣布 Vercel 联署支持 Open Weights and American AI Leadership 信函，认为开源代码、数据、协议和研究一直是技术进步的基础，开放权重是下一条合理前沿。

- 原文：https://x.com/rauchg/status/2081546513885622760

他还用 scriptc 把 Vercel CLI 的 TypeScript 编译为原生静态程序：二进制仅 1.28 MB，平均启动开销 1.5 ms，平均编译时间 2.94 秒，并继续使用多个 `node:` 标准模块。代码由 GLM 5.2 Fast 转译，产物不嵌入 V8 或 QuickJS。

- 原文：https://x.com/rauchg/status/2081517519303737559

### Aaron Levie，Box CEO

Aaron Levie 认为，模型变强并不会压缩应用层机会，反而会放大它。企业流程要真正被 AI 改造，还必须连接业务系统与正确数据，设计人类决策节点和 UX，建立持续改善数据与模型的反馈回路，并处理监管与合规；银行客户开户、法律合同审查和生命科学流程需要的实现完全不同。模型能力越强，可自动化的流程越有野心，对深入行业语境的 applied AI layer 需求也越大。

- 原文：https://x.com/levie/status/2081491621162668207

### Zara Zhang，Builder

Zara Zhang 认为，衡量 AI adoption 不该看消耗了多少 token，而应看从用户需求出现到功能真正上线用了多久。

- 原文：https://x.com/zarazhangrui/status/2081627581997269192

她还指出，通用聊天产品越通用，反而越难上手：用户面对空白输入框会僵住，因为他们确实不知道该问什么。这也解释了为什么市场上会出现如此多 AI 教程。

- 原文：https://x.com/zarazhangrui/status/2081627109299310684

### Nikunj Kothari，FPV Ventures 合伙人

Nikunj Kothari 给出一个简短但大胆的判断：“prompt 证明”很快会取代“工作量证明”。他的核心意思是，在 AI 协作环境里，能够展示如何提出问题、组织指令并得到结果，可能比展示亲手执行了多少步骤更重要。

- 原文：https://x.com/nikunj/status/2081383934928068619

### Sam Altman

Sam Altman 展示了 ChatGPT Work 的端到端执行能力：他只在手机上提出需求，系统便根据历史聊天为 9 人周末旅行筛选三个方案，制作供所有人协商活动和目的地的全栈网站，并计划在达成一致后完成预订，同时在 Gmail 中起草通知邮件。他的评价很直接：“它就这样完成了。”

- 原文：https://x.com/sama/status/2081396796174282900

## PODCASTS

### The MAD Podcast with Matt Turck：OpenAI’s Compute Chief: We Can’t Build Fast Enough | Sachin Katti

**核心结论：OpenAI 眼下最大的算力风险不是建设过度，而是物理世界的供给速度远远跟不上 AI 对算力的需求。**

OpenAI 工业算力负责人 Sachin Katti 曾任 Stanford 教授、连续创业者和 Intel CTO，如今负责从土地、电力、机房、芯片和融资，到上线运维、容量规划与内部算力分配的完整链条。他把 AI 数据中心描述为“把电子变成 token 的巨型工厂”：芯片、互连、电缆乃至变压器都产生大量热，因此液冷效率直接决定同样能耗下能产出多少 intelligence。

OpenAI 的判断是，需求仍远超供给，新增算力一上线就会被消耗；算力增长曾与收入增长同步，而 AI 开始参与 AI 研究后，能够并行运行的实验数量还会进一步爆炸。Katti 直言：“每当我们觉得算力已经够多、可以放慢时，结果总会让我们吃到负面惊喜：我们本不该放慢。”真正的瓶颈横跨整个供应链，包括许可、燃气轮机、变压器，以及电工和管道工等熟练工种。

这也解释了 OpenAI 为什么走向全栈。Stargate 是覆盖多种合作与自建方式的算力战略；Jalapeno 芯片则利用 OpenAI 已知未来模型负载的优势，与 Broadcom 在九个月内完成设计流片，核心指标是提高每瓦产生的 token 数。AI 已在辅助芯片设计，Katti 预计 AI 自己设计下一代训练与运行系统的递归世界并不遥远。与此同时，MRC 通过多路径传输，让十万 GPU 规模集群在链路故障时仍能继续训练；Guaranteed Capacity 则把“保证算力”转化为“保证 token”，使 intelligence 开始像企业必须提前锁定的关键供应品。

- 原视频：https://www.youtube.com/watch?v=wEZBlmvxx4o

Generated through the Follow Builders skill: https://github.com/zarazhangrui/follow-builders
