# AI Builders Digest — 2026-09-12

## X / TWITTER

### Google VP Josh Woodward

Josh Woodward 宣布 Gemini 已登陆 Windows，让桌面端用户可以直接使用 Gemini。这是一次明确的产品扩展，但原帖没有披露更多功能差异。

https://x.com/joshwoodward/status/2098131750660772342

### Anthropic Claude Code 团队 Boris Cherny

Boris Cherny 认为，AI 生成代码应该按用途分级：低风险、即将丢弃的原型可以被当作黑盒，但生产代码的质量标准应该比人写的代码更高。Anthropic 的做法包括大量 lint、测试、Claude 驱动的端到端测试、每日 fuzzing、自动代码与安全审查；开发者还应使用最新 frontier model、提高 reasoning effort，并通过 CLAUDE.md 和 skills 教会 Claude 理解代码库。

https://x.com/bcherny/status/2098217573276131577

他同时提醒，模型能力越强，双重用途风险越大：会写代码的模型也能攻击关键基础设施，会辅助生物研究的模型也可能被滥用于制造疫情。重点不是停止能力进步，而是让 safeguards、监控和社会讨论同步升级。

https://x.com/bcherny/status/2098281805770309686

### OpenAI Codex 与 ChatGPT 团队 Thibault Sottiaux

Thibault Sottiaux 宣布，一套可按需扩展 agent 的 API 已开放，底层接近 ChatGPT Work 使用的基础设施，开发者可在一分钟内开始构建。他还透露 OpenAI 内部用于制作 dashboard、理解业务的数据工作方式，并强调它已经成为团队不可或缺的工具。

https://x.com/thsottiaux/status/2098238138334548260

https://x.com/thsottiaux/status/2098165551554240764

由于系统容量压力，OpenAI 暂停接受新的 200 美元 Astra Pro 订阅，现有账户、其他套餐与 API 不受影响。这个动作说明高端 agent 产品的真实约束已不只是模型能力，也包括持续供给计算资源和保障现有用户体验。

https://x.com/thsottiaux/status/2098113585683808624

### AI 教程创作者 Peter Yang

Peter Yang 给出一个非常直接的实用判断：如果目标是把事情做完，他认为 Sol 优于 Astra。原帖没有展开基准或适用场景，因此这更像一线使用偏好，而不是完整评测结论。

https://x.com/petergyang/status/2098215935467544604

### Meta AI 高级总监 Madhu Guru

Madhu Guru 认为，agent eval 不能只看最终答案，还必须测量完成任务的每一步。两个 agent 即使都得到正确结果，能够准确找源、取对文档、用 4 次干净 tool call 完成任务的轨迹，也明显优于重复搜索、经历错误后用 17 次调用勉强到达终点的轨迹。

https://x.com/realmadhuguru/status/2098064969464217720

他的实践框架是：先定义完整 workflow，再拆出每一步任务，为各步骤设计独立或嵌入式 eval，并同时覆盖中位难度与困难任务。看评测时先研究过程，再看最终结果。

### Anthropic Claude Code 团队 Thariq

Thariq 分享了一个让 Claude 获得更多个人上下文的 prompt：让它用自由文本深入访谈，在适合多选时调用 AskUserQuestion，并把尚不了解但相关的人生信息保存到 memory。核心思路是把个性化从一次性提示词，变成结构化访谈后可持续复用的上下文资产。

https://x.com/trq212/status/2098157600361861579

### Google Labs

Google Labs 宣布 Dreambeans 已免费向美国 18 岁以上用户开放，覆盖 iOS 和 Android，无需订阅。用户还可以把 Gemini app 与 Dreambeans 连接起来，让它利用聊天中积累的细节与理解，生成更个性化的每日故事。

https://x.com/GoogleLabs/status/2098110018289803558

### Replit CEO Amjad Masad

Amjad Masad 区分了现实的 AI 风险与“全人类灭绝”叙事：他确实担忧网络安全等问题，但不认为 AI 导致 100% 人类死亡是一个接近现实的风险判断。这是一个明确的反共识立场，不过原帖没有进一步给出论证。

https://x.com/amasad/status/2098171265924116732

### Vercel CEO Guillermo Rauch

Guillermo Rauch 提出基础设施的新目标：让每个 agent 在每个区域都能拥有一台 computer。与此同时，Vercel 面对每天约 1,000 万次部署、累计 23.5 亿次部署的多租户规模，把全球 metadata store 的 p99 延迟改善了 91%，并同步加快 build 到 deploy 的链路。

https://x.com/rauchg/status/2098158541932794222

https://x.com/rauchg/status/2098091056302833837

他强调，底层系统需要在数百毫秒内完成全球同步，支持回滚、配置变更与路由更新；agentic deployment 的高速增长，正在把部署基础设施本身变成 AI 应用扩张的关键瓶颈。

https://x.com/rauchg/status/2098066258155708851

### Box CEO Aaron Levie

Aaron Levie 在与银行、媒体、保险、咨询等行业的数十位技术负责人交流后，总结出企业 agent 落地的七个现实主题：网络安全压力、多模型并存、agent 身份与权限、流程再造、架构快速换代、eval 尚不成熟，以及 legacy system 带来的数据碎片化。最关键的判断是，真正的 ROI 来自重写 workflow，让 agent 改变工作发生的方式，而不是把 agent 叠加到旧流程上。

https://x.com/levie/status/2098218284139311615

Box 也在加深与 OpenAI 的合作，让用户可以在 ChatGPT 中安全使用企业内容。Levie 把这理解为软件持续“无界面化”的一部分，未来 agent 会跨系统处理数据并执行 workflow。

https://x.com/levie/status/2098135659714085281

### FPV Ventures 合伙人 Nikunj Kothari

Nikunj Kothari 用三个数字概括当前早期风投市场的过热预期：创业者都想融 5,000 万美元 seed、都相信明年能做到 3,000 万美元 ARR，而热门的分批 seed 最终往往落在约 3 亿美元估值。这个观察揭示了融资规模、增长承诺与估值正在被同一套乐观预期同时推高。

https://x.com/nikunj/status/2098078391065018816

### OpenClaw 与 OpenAI 团队 Peter Steinberger

Peter Steinberger 认同一个适合 AI 编程时代的取舍：复制逻辑已经不再昂贵，但抽象仍然会制造理解和维护成本。当 agent 能快速生成重复实现时，过去为了减少代码量而提前抽象的收益可能下降，清晰的局部实现反而更有价值。

https://x.com/steipete/status/2098089196800098798

### SPC General Partner、Bevel Health 联合创始人 Aditya Agarwal

Aditya Agarwal 提出一个资源分配问题：如果一台机器唯一能做的事就是寻找重大疾病的治疗方法，人类愿意投入多少 GDP？他的答案是“非常高”，并认为我们已经进入必须认真面对这种选择的阶段。

https://x.com/adityaag/status/2098112281267843264

Generated through the Follow Builders skill: https://github.com/zarazhangrui/follow-builders
