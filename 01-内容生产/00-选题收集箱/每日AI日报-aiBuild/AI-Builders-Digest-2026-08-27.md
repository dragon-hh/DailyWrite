# AI Builders Digest — 2026-08-27

## X / TWITTER

### Swyx

AI 工程师与社区建设者 Swyx 提醒，现阶段不要启用 Codex 的「locked use」能力。他本周两次因此被完全锁在 macOS 钥匙串之外，并指出相关能力依赖尚不稳定的 Mac 特性，Apple 开发者论坛也已将其列为已知问题；在云端能力尚未补齐之前，这项本地功能应谨慎避开。

https://x.com/swyx/status/2092492963435946494

### OpenAI Codex 与 ChatGPT 团队的 Thibault Sottiaux

Thibault Sottiaux 介绍了一款面向团队和小型公司的新方案，使用方式类似 Pro 100 美元套餐，但加入了安全工作区、SAML、SSO、MFA、集中计费、使用分析和支出控制。它覆盖 ChatGPT、ChatGPT Work 与 Codex 全部功能，并可连接 Google Workspace、Slack、GitHub、Microsoft 365 等服务，同时取消 5 小时限制。

https://x.com/thsottiaux/status/2092345330272780499

### AI 实用教程作者 Peter Yang

Peter Yang 开源了 `/fuck-cancer` AI skill，帮助癌症患者与照护者把分散的医生、文件和保险信息整理成一份持续更新的行动简报。简报只保留三项下一步行动，并明确区分已确认事实与未知事项、解释医学术语、记录照护决策；需要研究时，它会调用 National Cancer Institute 与 ClinicalTrials.gov API 等可信来源，也可保存为本地 Markdown 或同步到家庭共享的 Google Doc。

https://x.com/petergyang/status/2092249012913258946

他随后展示了该 skill 生成和维护的简报实例，强调用一份 single source of truth 集中患者信息、后续行动、已知事实、术语解释与更新日志。

https://x.com/petergyang/status/2092311110871617915

### Meta AI 高级总监 Madhu Guru

Madhu Guru 认为，很多 eval 失败，不是指标设计得不够精细，而是团队把 eval 当成静态产物，用户的使用方式却已经从短文档摘要升级到多文档综合、持续监控与主动 agent。她建议围绕对话轮数、文档规模、工具使用、自主程度和用户旅程建立 eval 路线图，从生产 traces 发现行为变化，并提前为下一阶段的 P0 用例补齐评测。

https://x.com/realmadhuguru/status/2092426017118028266

她还汇总了完整的九篇 eval 系列，覆盖失败模式分类、分层评测、平均值陷阱、hill climbing、区分能力与路线图等主题，适合作为系统化搭建 eval 的索引。

https://x.com/realmadhuguru/status/2092461206783373758

### Google Labs

Google Labs 推出实验性产品 Play with Putty，这是一款支持多人实时协作的 vibe coding 工具，可共同构建工具和网站。当前仅面向美国 18 岁以上用户开放候补名单，产品重点是把个人式的 AI 编程变成多人同步创作。

https://x.com/GoogleLabs/status/2092293667688173593

### Vercel CEO Guillermo Rauch

Guillermo Rauch 发布 Run SDK，用轻量级 QuickJS 安全上下文执行 agent 动态生成的代码。它瞄准不需要完整 sandbox 的场景，以更快、更低成本的方式提供受控代码执行，安装入口为 `npm i run`。

https://x.com/rauchg/status/2092382653161107534

他同时宣布 Vercel Connect 正式 GA，并把「安全连接服务与数据」称为构建 agent 最难的问题。开发者可以用命令创建例如 Notion 连接，再获得一个能代表已认证用户查询数据的 MCP client。

https://x.com/rauchg/status/2092352411839193234

### Box CEO Aaron Levie

Aaron Levie 判断，企业 AI 的主要机会不在继续堆叠原始模型能力，而在填平模型与真实工作流之间的巨大落差。真正有价值的 applied AI 公司，需要同时处理业务上下文、变革管理、多模型路由、垂直系统连接、agent 工作流 UX 与行业 eval，把 token 转化为可验证的业务结果；目前正是建立这些垂直领域头部公司的窗口期。

https://x.com/levie/status/2092466424694649066

### SPC 普通合伙人 Aditya Agarwal

Aditya Agarwal 认为，大众反感数据中心扩张并不意外，因为当前 AI 的直接收益主要流向知识工作者和高收入群体。真正改变公众态度的节点，可能是 AI 开始治愈普遍影响普通人的疾病；同时，AI 行业长期强调恐惧、却没有描绘可信的积极未来，也加深了这种距离感。

https://x.com/adityaag/status/2092290497826173186

### Anthropic 的 Claude

Claude 现在把 Chat 与 Claude Cowork 的记忆统一起来，Cowork 接手任务时，可以直接继承聊天中已经形成的项目背景、协作偏好与客户信息。记忆会随着对话自动更新，也可以通过明确说「remember this」来保存指定内容。

https://x.com/claudeai/status/2092299704864284888

https://x.com/claudeai/status/2092299707653439497

所有记忆都会以主题列表呈现在 Settings 中，用户可以逐项查看、编辑或删除。健康与宗教信仰等敏感主题默认不会进入记忆，除非用户在设置中主动开启；Memory 已默认面向 Free、Pro 和 Max 套餐启用。

https://x.com/claudeai/status/2092299710002319742

Generated through the Follow Builders skill: https://github.com/zarazhangrui/follow-builders
