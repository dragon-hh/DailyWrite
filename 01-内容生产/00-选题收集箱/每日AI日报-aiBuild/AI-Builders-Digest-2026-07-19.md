# AI Builders Digest | 2026-07-19

## X / TWITTER

### AI builder Swyx

Swyx 认为，团队应该让 Codex、Claude、Gemini 或 Devin 每周自动研究如何改进 SEO 与 AEO，这仍是一块被明显低估的“免费 alpha”。他进一步提出，下一步值得研究的不只是一般化 AEO，而是不同模型是否会偏好由自己优化的内容，即所谓 on-policy AEO。

来源：
- https://x.com/swyx/status/2078244735794413786
- https://x.com/swyx/status/2078293998398263587

### OpenAI Codex 与 ChatGPT 产品成员 Thibault Sottiaux

Thibault Sottiaux 宣布重置所有付费用户的 Codex 与 ChatGPT Work 使用额度，并表示团队正以很快速度迭代基础设施，以应对持续加速的规模增长。他同时转发并认可了 GPT-5.6 Sol 的表现。

来源：
- https://x.com/thsottiaux/status/2078320950488297917
- https://x.com/thsottiaux/status/2078310751878647932

### AI 教程创作者 Peter Yang

Peter Yang 期待一种以语音为核心的 agent 工作方式：人可以在户外边走边像打电话一样分配任务，再通过语音接收状态更新，而不是整天盯着屏幕管理多个 agent。他认为这种交互能显著降低认知负担，并期待有实验室率先把它做成产品。

来源：https://x.com/petergyang/status/2078276992470794531

### Meta AI 高级总监 Madhu Guru

Madhu Guru 认为，企业难以从基础聊天机器人迈向真正可用的 AI 系统，核心瓶颈不是模型，而是 eval、harness 和人才。企业既要能用离线与在线 eval 明确定义用例、评估质量成本延迟曲线，也要建立独立于具体模型的路由、多 agent 编排、上下文、工具调用和记忆系统，其中最稀缺的是能在前沿把这一整套系统搭起来的人才。

他还指出，Kimi 等模型未必会直接伤害 Google，因为许多企业仍需要安全、数据驻留、合规和芯片保障，最终可能通过 Google Cloud 消费这些模型，价值只是从一个口袋流向另一个口袋。

来源：
- https://x.com/realmadhuguru/status/2078131628262752550
- https://x.com/realmadhuguru/status/2078210889778708744

### Anthropic Claude Code 成员 Thariq

Thariq 建议，在让 coding agent 消耗大量 token 之前，先制作 mockup、schema、数据模型或 proof of concept。早期原型能更快暴露方向错误，避免做到后面才发现自己根本不想要这个结果。

来源：https://x.com/trq212/status/2078189833445654714

### Vercel CEO Guillermo Rauch

Guillermo Rauch 宣布 Sandbox 下载流量免费，直接降低了构建和运行 agent 时的数据传输成本。他把这项变化概括为让开发者可以继续“ship more agents”。

来源：https://x.com/rauchg/status/2078305023784620342

### Box CEO Aaron Levie

Aaron Levie 的核心判断是，AI 越便宜，总需求越大，价值会同时流向客户与整个技术栈。更强的 frontier model 不一定因便宜模型普及而失去需求，因为复杂任务仍可能需要最强模型负责 orchestration，再把大批 token 工作分发给更便宜或更专用的模型。效率提升甚至会反过来增加 frontier model 的总支出，真正承压的更可能是利润率。

来源：https://x.com/levie/status/2078139206946459853

### Builder Zara Zhang

Zara Zhang 给 build in public 的建议是，不要把内容生产当成额外工作，而应展示产品内部本来就在发生的工作，例如短录屏、第一版实现，或某个用户行为如何改变了设计。真正有价值的是决策过程，而不是制作精良度。

她还观察到，商业会议从“录音令人不适”变成“默认全部记录”，而记录对象越来越不是人，而是后续处理信息的 agent，这说明技术正在直接改写组织文化。

来源：
- https://x.com/zarazhangrui/status/2078086930756202924
- https://x.com/zarazhangrui/status/2078076500683997446

### OpenClaw 与 OpenAI 成员 Peter Steinberger

Peter Steinberger 展示了 Codex 在缺少理想 API 时如何用 browser 与 computer use 完成 GitHub PR 图片上传：打开 Chrome、进入 PR、点击评论，再操作 macOS 文件选择器。过程既强大又笨重，因此他把 Codex 放在 VM 中运行，避免 agent 抢占本机应用焦点。

他还因 CodexBar 图标定制问题让 Codex 直接构建了一个编辑器，体现了 agent 从“辅助写代码”走向“遇到摩擦就现场造工具”的用法。

来源：
- https://x.com/steipete/status/2078318731785359634
- https://x.com/steipete/status/2078264088644276598

### Anthropic 的 Claude

Claude 宣布，从 7 月 20 日开始，Claude Fable 5 将以 50% 的使用限额纳入所有 Max 与 Team Premium 套餐；Pro 与 Team Standard 用户仍可通过 usage credits 使用，并会获得一次性 100 美元额度。Anthropic 表示，Fable 的需求很难预测，因此此前采用分阶段开放，并将继续投入新增容量。

来源：
- https://x.com/claudeai/status/2078302415804379218
- https://x.com/claudeai/status/2078302417100394737

## 官方博客

### Anthropic Engineering

#### An update on recent Claude Code quality reports

Anthropic 确认，近期部分用户感受到的 Claude Code 质量下降来自三个产品层问题，而不是 API 或推理层退化。第一，3 月 4 日把默认 reasoning effort 从 high 降到 medium，以降低延迟，但牺牲了用户感知的智能水平，已于 4 月 7 日撤回。第二，清理闲置会话旧 thinking 的实现有 bug，导致后续每一轮都持续丢弃历史推理，让 Claude 显得健忘、重复并更快耗尽额度，已于 4 月 10 日修复。第三，一条限制工具调用间文本不超过 25 词、最终回答不超过 100 词的 system prompt，使 Opus 4.6 与 4.7 在某项评测中下降 3%，已于 4 月 20 日撤回。

文章明确写道：“We never intentionally degrade our models.” 后续措施包括扩大公开版本的内部使用、改进 Code Review、对每次 system prompt 变更运行更广泛的逐模型 eval，并为可能损害智能水平的改动增加 soak period 和渐进式发布。Claude Code v2.1.116 已包含全部修复，并为所有订阅用户重置使用额度。

来源：https://www.anthropic.com/engineering/april-23-postmortem

#### Scaling Managed Agents: Decoupling the brain from the hands

Anthropic 将 Managed Agents 设计成三个可独立替换和恢复的抽象：session 是只追加的事件日志，harness 负责调用 Claude 与路由工具，sandbox 负责执行代码和修改文件。关键变化是把“brain”与“hands”解耦：harness 不再住在 sandbox 容器里，而是把容器当成普通工具，通过 `execute(name, input) → string` 调用。容器或 harness 挂掉后都可重新初始化，session 日志则留在外部恢复任务。

这种结构也把凭证移出不可信代码运行环境，Git 凭证随资源配置，MCP OAuth token 放在外部 vault 并由代理注入，减少 prompt injection 直接窃取凭证的风险。文章强调：“The session is not Claude’s context window.” 完整上下文被持久保存为可查询事件流，压缩和裁剪只是 harness 的可变策略。实际效果是 p50 首 token 延迟下降约 60%，p95 下降超过 90%，同时支持多个 brain 动态连接多个 hand。

来源：https://www.anthropic.com/engineering/managed-agents

### Claude Blog

#### New in Claude Managed Agents: self-hosted sandboxes and MCP tunnels

Claude Managed Agents 新增 self-hosted sandbox 与 MCP tunnel。企业可让工具执行、敏感文件、代码包和服务留在自己的基础设施或 Cloudflare、Daytona、Modal、Vercel 等托管 sandbox 中，同时由 Anthropic 基础设施继续负责 agent loop、上下文管理与错误恢复。self-hosted sandbox 已进入 public beta。

MCP tunnel 让 Managed Agents 和 Messages API 通过企业内部署的轻量 gateway 连接私有 MCP server，无需开放入站防火墙规则或公共端点，连接由内向外建立并端到端加密，目前处于 research preview。直接价值是把内部数据库、私有 API、知识库和工单系统安全地变成 agent 工具，同时保留企业已有的网络策略、审计、运行时镜像和资源控制。

来源：https://claude.com/blog/claude-managed-agents-updates

## PODCASTS

### The MAD Podcast with Matt Turck

#### OpenAI’s Compute Chief: We Can’t Build Fast Enough | Sachin Katti

**核心结论：OpenAI 当前真正担心的不是算力过剩，而是物理世界无法足够快地建设算力。**

OpenAI industrial compute 负责人 Sachin Katti 曾任 Stanford 教授、连续创业者和 Intel CTO。他把现代 AI 数据中心描述为“把电子变成 token 的巨型工厂”：规模更像一台覆盖足球场的超级计算机，芯片、连接件、变压器和数据大厅都需要大规模液冷。OpenAI 不只是采购合作伙伴的计算资源，也在直接参与数据中心、电网发电、输电线路和变电站建设；当电网容量不足时，还会考虑以燃气轮机为主的 onsite generation，而核能被视为最密集、清洁且可扩展的长期选项。

Katti 认为，推理已经占据很大一部分甚至多数计算量，而且训练本身也越来越依赖推理，例如合成数据、post-training 与 test-time compute。OpenAI 的自研芯片 Jalapeno 追求的关键指标是每瓦产生更多 token，通过模型与硬件协同设计缓解电力约束。

最反直觉的判断是，AI 参与 AI 研究不会减少算力需求，反而会让可运行的实验数量爆炸。过去实验规模受限于人类研究员数量，未来 AI 研究 agent 会把瓶颈推向计算和供应链。他直言：“Demand far outstrips compute supply today.” 只要有新算力上线，OpenAI 就会立即消耗；真正的风险是工厂、供应链和电力系统建设速度跟不上需求。

来源：https://www.youtube.com/watch?v=wEZBlmvxx4o

Generated through the Follow Builders skill: https://github.com/zarazhangrui/follow-builders
