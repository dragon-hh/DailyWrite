# AI Builders Digest | 2026-08-28

## X / TWITTER

### Anthropic Claude Code 团队 Thariq

Thariq 观察到多家客户正在遭遇欺诈请求。他认为这类攻击不仅伤害受害者，也会压缩服务商向正常用户开放使用额度的空间，因此认可 Stripe 在风控侧的投入。

https://x.com/trq212/status/2092729394565657010

他还介绍了 Claude 新增的 SendFeedback 工具。用户不必再手动进入 `/feedback` 撰写报告，只要让 Claude 起草反馈并确认发送，就能更低摩擦地把真实问题交给产品团队。

https://x.com/trq212/status/2092696449616376140

### Vercel CEO Guillermo Rauch

Guillermo Rauch 分享了面向 agent 的全球计算能力：支持多区域和故障转移，默认可运行最多 10,000 个并发 sandbox，并以每分钟 5,000 个 vCPU 的速度扩容，后续还会增加区域。重点不是单台机器更强，而是 agent 可以随时调用分布式算力。

https://x.com/rauchg/status/2092735785460277627

Vercel 也在推出安全仪表盘和 `vercel security check` CLI。这个 CLI 可以让 agent 在 human-in-the-loop 模式下改进安全状态，也能放进 cron 定期运行，把安全检查变成可自动化、可持续的流程。

https://x.com/rauchg/status/2092621371914482026

### Box CEO Aaron Levie

Aaron Levie 认为，企业落地 AI 的核心瓶颈不是再找一个更强模型，而是让 agent 安全地获得正确上下文。Box 当季营收为 3.211 亿美元，同比增长 9%，按固定汇率增长 11%，创 14 个季度以来最高增速，并把全年营收目标提高到 12.90 亿美元；他将增长动力指向企业对 AI 和非结构化内容管理的需求。

他的关键判断是，合同、研究资料、财务文件、营销资产和产品路线图等非结构化内容，才构成企业知识的大头。企业需要的是能够随时更换模型或 agent 的应用层平台，同时具备权限护栏、完整审计日志和实时安全告警，避免外部 agent 越权访问内部数据。

https://x.com/levie/status/2092702955292230100

### FirstMark VC Matt Turck

Matt Turck 把 NVIDIA 与 Hugging Face 的结合视为一次多方共赢：NVIDIA 进一步站到开源 AI 的中心，Hugging Face 获得更合适的长期归宿，开源生态本身也会受益。这是他的判断，而不是对开源商业模式已自动解决的保证。

https://x.com/mattturck/status/2092808287280329097

他同时提出几条值得继续观察的 AI 产业判断：NVIDIA 可能已经像一家顶级风险投资机构，应用公司正在比模型实验室更快地变成实验室，而 AI 泡沫的真正风险可能来自投资期限与技术兑现周期不匹配。他也提醒自己不能继续低估中国市场和团队。

https://x.com/mattturck/status/2092688916969095587

### Builder Zara Zhang

Zara Zhang 对大公司的 PR 职能提出了一个尖锐判断：本应增强品牌的团队，常常因为阻止真实、有个性的营销表达，反而成为品牌建设的障碍。问题不只是审批慢，而是组织为了规避风险，把最能建立信任的声音一起过滤掉了。

https://x.com/zarazhangrui/status/2092774923320369394

她还指出，人们对 AI 写作存在明显双重标准，自己使用时觉得合理，看到别人使用时却认为不正当。这说明争议往往不只围绕工具本身，也围绕作者身份、透明度和谁有资格借助工具提高效率。

https://x.com/zarazhangrui/status/2092773720112988366

### Every CEO Dan Shipper

Dan Shipper 宣布 Codex 原生应用已经出现，把 Codex 从单纯的开发辅助能力继续推向可以直接承载工作流的应用形态。

https://x.com/danshipper/status/2092686463859126492

他把当下称为「博学者和哲学家的黄金时代」，因为跨学科理解与持续追问正在重新变得稀缺且有价值。在他看来，这也是对知识焦虑的一种解药。

https://x.com/danshipper/status/2092636264902148262

### SPC General Partner Aditya Agarwal

Aditya Agarwal 判断，AI 前沿竞争将越来越由 post-training 决定。他介绍的 DeepCogito 是一家专注 post-training 的研究实验室，刚宣布完成 4,300 万美元 A 轮融资，研究重点是大规模强化学习与递归自我改进。

DeepCogito 的核心方法是 iterated distillation and amplification，也就是 IDA，并已在 3B 到 600B 以上参数规模的模型上公开验证。这里真正值得关注的是，模型能力竞争正从预训练规模扩展到如何让模型在训练后持续变强。

https://x.com/adityaag/status/2092679288869019700

### Anthropic 的 Claude

Claude 在 Cowork 中加入了内置浏览器。任务涉及网站时，浏览器会在侧边栏打开，Claude 可以导航页面、填写表单并完成工作，而用户无需离开当前环境。

https://x.com/claudeai/status/2092755571455758427

这个浏览器内置于桌面应用，与用户自己的浏览器和登录状态隔离，不需要安装扩展，并将在一周内向所有付费计划推出。

https://x.com/claudeai/status/2092755573183828193

如果用户更愿意在已经登录的个人浏览器里工作，Claude in Chrome 也已面向所有付费计划正式开放；现有用户仍会默认使用这一方式。

https://x.com/claudeai/status/2092755574563741871

## 官方博客

### Claude Blog

#### Claude in Chrome is generally available

Claude in Chrome 现已向所有 Claude 付费计划正式开放，并能在浏览器中自主执行部分操作，不再要求用户逐步批准。它可以利用用户现有登录状态读取页面、输入文字、点击链接、跳转和填写表单，尤其适合没有 connector 的内部仪表盘、旧系统和供应商门户。

这次全面开放的重点是 prompt injection 防护。网页、邮件或表单里可能藏有恶意指令，诱导 agent 偏离用户目标。Claude 会先用 probe 扫描工具返回的网页内容，再由安全分类器核对即将执行的动作是否符合原始请求。文章给出的强攻击评测中，Opus 4.5 在额外防护前的攻击成功率为 17.6%，Opus 5 为 3.8%；加入 probe 与自动批准安全分类器后，Sonnet 5 和 Opus 5 没有攻击成功，Fable 5 的成功率为 0.3%，且人工确认均为低严重度场景。

文章强调：「Prompt injection 仍是一个不断变化的目标。」这意味着 0% 的阶段性评测结果不能被理解为风险永久消失。Enterprise 管理员可以限制允许访问的域名；涉及本机文件或其他桌面应用时，仍需使用 Claude 桌面应用。目前 Claude in Chrome 不支持其他 Chromium 浏览器和移动端。

https://claude.com/blog/claude-in-chrome-generally-available

### Claude Blog

#### Claude gets its own browser in Cowork

Claude Cowork 在桌面应用中获得独立内置浏览器。网站任务出现时，它会在侧边栏自动打开，Claude 可以浏览、读取、点击和输入，适合填写表单、从仪表盘提取数据或处理没有 connector 的门户。它不需要扩展，也不会默认共享用户个人浏览器里的标签页、书签和密码。

内置浏览器与 Claude in Chrome 分工明确。前者适合把完整网页任务交给 Claude，让用户继续处理其他工作；后者适合直接操作用户已经打开并登录的页面。用户可以逐站点导入登录状态，但银行、邮箱和 SSO 站点默认不会迁移，除非用户主动选择。文章用一句话概括这种边界：「它是 Claude 的浏览器，不是你的浏览器。」

该功能本周向 Pro、Max 和 Team 计划的 macOS、Windows、Linux 桌面应用推出，Enterprise 管理员已经可以开启。它沿用 Claude in Chrome 的 prompt injection 防护，但官方明确提醒这些措施只能降低风险，无法彻底消除风险，因此建议先在可信网站使用。

https://claude.com/blog/cowork-built-in-browser

Generated through the Follow Builders skill: https://github.com/zarazhangrui/follow-builders
