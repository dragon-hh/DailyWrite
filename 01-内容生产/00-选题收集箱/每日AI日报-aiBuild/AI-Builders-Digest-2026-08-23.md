# AI Builders Digest — 2026-08-23

## X / TWITTER

### Swyx，AI 工程与开发者社区 Builder

Swyx 认为，“Simulation 是新的 scaling law”不只是营销口号。随着模型开始自动化越来越多的 ML 研究和 AI 工程，真正难以跨越的障碍将是模拟人类及其反馈；他把 Simile 在 Fortune 100 企业中初步找到 PMF，视为这个方向已经开始落地的信号。

https://x.com/swyx/status/2090948945753076141

### OpenAI Codex 与 ChatGPT 团队 Thibault Sottiaux

Thibault Sottiaux 表示，部分 Codex 用户本周的 cache hit rate 低于此前稳定水平，而稳定命中缓存是控制用量消耗的重要因素，这可能解释了为什么一些用户的额度下降得更快。团队正在调查，并承诺次日更新；同时，ChatGPT Work 与 Codex 付费用户的 banked reset 已经上线。

https://x.com/thsottiaux/status/2091033630147854385

https://x.com/thsottiaux/status/2090964822422949999

### AI 教程作者 Peter Yang

Peter Yang 对 Instinct 的体验评价很鲜明：它连接 iMessages、Google Workspace 和 MCP 的 onboarding 很顺滑，也会主动建议可执行的任务，但单一对话线程限制了严肃工作的并行性，因此更适合处理零散杂务。他随后提出更关键的隐私问题，称 Instinct 在未经许可的情况下索引并保留邮件，且没有提供删除记录的方式；在问题解决前，他不会推荐该产品。

https://x.com/petergyang/status/2090814910720835633

https://x.com/petergyang/status/2090936583814025417

### Meta AI 高级总监 Madhu Guru

Madhu Guru 警告团队不要把复杂的 eval suite 压缩成单一分数，因为平均值会掩盖模型在关键场景中的退步。例如，摘要和基础问答提升，并不能抵消复杂金融分析从 70% 降到 63% 的风险。加权总分同样可能制造虚假的数学精确性；更可靠的做法是维护有优先级的 eval 清单，深入理解关键测试在哪里成功、在哪里失败，再判断新系统是否真的更适合用户。

https://x.com/realmadhuguru/status/2090930137885774324

### Anthropic Claude Code 团队 Thariq

Thariq 分享了 Anthropic 内部常用的 ELI5 skill：输入 `/eli5` 和需要解释的问题，它会用大图、少文字的 HTML artifact，把内容讲给完全没有背景知识的人。这个 skill 可用于理解模块、设计取舍或事故根因；目前可以通过 Claude plugin 社区 marketplace 安装，团队仍在考虑是否把它做成官方 plugin。

https://x.com/trq212/status/2090884854590382515

https://x.com/trq212/status/2090884855798407576

https://x.com/trq212/status/2090890394880155888

### Vercel CEO Guillermo Rauch

Guillermo Rauch 宣布一个 Vercel 相关工具现已支持 Grok 与 Codex 订阅，并可直接装进 sandbox 测试。他还分享了团队持续运行 `is-agentic` 评测直到达到 100/100 的过程：评测循环迫使他们补齐了不少产品缺口，重点不是追逐分数，而是确保评判标准本身足够严格，值得消耗用户的时间和 token。

https://x.com/rauchg/status/2090953806624489501

https://x.com/rauchg/status/2090858571613470919

### Box CEO Aaron Levie

Aaron Levie 判断，AI 模型正在同时变得更便宜、更通用、更快，并深入更多专业领域。下一阶段最大的机会不只是继续提升模型，而是让廉价智能扩散到整个经济体系；对 applied AI 创业公司而言，上游模型的激烈创新与竞争正在形成强劲顺风。

https://x.com/levie/status/2091038566260539574

### Builder Zara Zhang

Zara Zhang 把持续建设压缩成三条原则：每天出现、始终发布，并且不要害怕一遍遍重复自己的核心信息。对 builder 来说，稳定输出和重复传播不是缺乏新意，而是让产品与观点真正被市场看见的必要动作。

https://x.com/zarazhangrui/status/2090702627206214081

### FPV Ventures 合伙人 Nikunj Kothari

Nikunj Kothari 展示了一个贴近日常生活的 agent 自动化：他让 Claude Code 从学校餐食网站的网络请求中找到未鉴权 API，整理出正确的数据格式，再接入家里的 Hermes bot。现在 Home bot 每天早晨会自动播报孩子当天的早餐和午餐，帮助家人决定是否需要自带食物。

https://x.com/nikunj/status/2090884422178627624

### Anthropic Claude

Anthropic 推出了由 Mythos 5 驱动的 Claude Security 扫描能力：把它指向 GitHub repo 后，系统会跨文件追踪数据流、分析组件交互，并为每个漏洞返回 CWE 分类、置信度、严重性和修复建议。建议补丁可直接在网页版 Claude Code 中打开，用户无需直接访问 Mythos 5；扫描按现有套餐的标准 token 用量计费。Anthropic 还计划与合作伙伴把 Mythos 5 集成进安全产品，设立提供 3500 万美元 credits 的 Defender Advantage Fund，并继续扩大 Cyber Verification Program。

https://x.com/claudeai/status/2090852316328902930

https://x.com/claudeai/status/2090852318527033804

https://x.com/claudeai/status/2090852320128938319

Generated through the Follow Builders skill: https://github.com/zarazhangrui/follow-builders
