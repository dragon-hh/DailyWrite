# AI Builders Digest：2026-09-14

## X / TWITTER

### AI 实用教程作者 Peter Yang

Peter Yang 对迟迟未至的 StarCraft 3 提出一个半认真、半挑衅的建议：与其等到 2030 年，不如让 AI 先承担一部分美术资产生产，再由人类监督质量。他的核心判断不是“让 AI 独立做游戏”，而是把生成能力放进人工把关的制作流程，用更短时间换取玩家愿意接受的高质量成品。

- https://x.com/petergyang/status/2098846399949627553
- https://x.com/petergyang/status/2098843136328171540

### Meta AI 高级总监 Madhu Guru

Madhu Guru 预测，未来 12 个月会有更多顶尖的前沿模型评测人才流向 METR 一类独立机构。驱动力包括资金增加、摆脱实验室股权带来的经济依赖，以及对 AI 生存风险的使命感。他同时强调，在解决 AI alignment 之前，人类必须先就机会、风险、二阶影响、衡量方法和跨国协调形成最低限度的共识，否则技术治理会先被彼此的不信任拖垮。

- https://x.com/realmadhuguru/status/2098859477219037691
- https://x.com/realmadhuguru/status/2098803717432860987

### Anthropic Claude Code 成员 Thariq

Thariq 认为，今天的 Claude Code 如果出现在 2018 年，会被当作 AGI；软件工程已经吸收了巨变，但系统和从业者都开始出现裂缝。即使他对灾难性结局的判断概率较低，也主张给行业留出时间加固系统，并让社会认真决定技术应如何部署。信心不能替代艰难的共同决策。

- https://x.com/trq212/status/2098860941391872132

### Replit CEO Amjad Masad

Amjad Masad 支持适度放慢前沿推进速度，用来加固现有系统。他给出的现实理由很具体：近期 agent 已经攻破了一些系统，而行业甚至还没有发现所有受影响的目标。安全窗口的价值，在于把未知暴露面真正查清楚。

- https://x.com/amasad/status/2098828265800835310

### Vercel CEO Guillermo Rauch

Guillermo Rauch 观察到，Vercel 团队在 Zig、Go、Rust 项目上的迭代速度已经能追平 TypeScript 和 Python。他由此提出一个鲜明判断：编程语言不再主要按人类书写便利性选择，agent 正成为“新的编译器”，把人的意图编译成高性能软件。

他还展示了不同模型、不同 reasoning effort 的 subagent 编排方式：规划模型与快速执行模型可以只靠 AGENTS.md 或提示词协作，不依赖复杂的服务端路由。与此同时，他承认 AI 安全与网络安全问题真实存在，但反对用可能让美国陷入官僚性停滞的治理方式处理竞争风险。

- https://x.com/rauchg/status/2098833404707922239
- https://x.com/rauchg/status/2098803573861621778
- https://x.com/rauchg/status/2098787667030712757

### Anthropic 研究人员 Alex Albert

Alex Albert 支持让独立评估人员以接近员工的权限常驻前沿 AI 实验室。他把这种安排类比为银行里的联邦检查员和核电站里的驻场监管员：在其他高风险行业并不罕见，因此可被视为一个务实的治理起点，而不是对科技公司的异常干预。

- https://x.com/alexalbert__/status/2098814342443761909

### Box CEO Aaron Levie

Aaron Levie 判断，随着模型能力提升，前沿 AI 行业不可避免会形成某种协同自律，真正困难的是各方能否就具体规则达成一致。任何“放慢”都依赖广泛的国际参与，但从博弈论看，各国往往要等风险变得更严重、更直观才愿意同步行动，因此接下来一段时间的治理过程大概率会非常混乱。

- https://x.com/levie/status/2098785357307539882

### Y Combinator 总裁兼 CEO Garry Tan

Garry Tan 用一句话概括传统企业软件在 agent 时代的处境：系统要么停留在 system of record，要么最终进化为某个垂直领域的专用 harness。价值正在从“保存业务事实”转向“围绕业务事实组织 agent 完成工作”。

- https://x.com/garrytan/status/2098666551629267324

### Sam Altman

Sam Altman 赞同放慢前沿能力推进节奏，并表示 OpenAI 近期一直在讨论这一问题。他明确支持让独立评估人员获得接近员工的访问权限，并称 OpenAI 也会采用同类安排，后续将公布更多信息。

- https://x.com/sama/status/2098811563415150910

## 官方博客

### Claude Blog：《Claude in Chrome is generally available》

Claude in Chrome 已面向所有 Claude 付费计划正式开放，并可在浏览器中自主执行点击、输入、跳转和表单填写，不再要求用户逐项批准。每次动作执行前，安全分类器都会核对它是否安全、是否符合用户原始请求；网页工具结果还会先经过探针扫描，以识别隐藏在页面、邮件或表单里的 prompt injection。

这次发布最值得注意的是量化结果。在更强的专业红队攻击评测中，不加额外防护时，攻击到达模型后对 Opus 4.5 和 Opus 5 的成功率分别为 17.6% 和 3.8%；加入探针与自动批准安全分类器后，Sonnet 5、Opus 5 和 Mythos 5 未出现成功攻击，Fable 5 为 0.3%，且成功案例均被人工确认属于低严重度场景。文中提醒：“Prompt injection 仍是一个不断移动的目标”（译）。这意味着正式开放不等于风险消失，而是把持续训练、扫描、动作校验和红队监测组合成了上线条件。

实际限制也很明确：它目前不支持其他 Chromium 浏览器或移动端；涉及本机文件及其他桌面应用时，仍需 Claude desktop app。

https://claude.com/blog/claude-in-chrome-generally-available

### Claude Blog：《Claude gets its own browser in Cowork》

Claude Cowork 在桌面端加入了内置浏览器。任务需要网页操作时，独立浏览器会在侧边栏打开，Claude 可以导航、读取、点击和输入；用户不必安装扩展，也不必把自己正在使用的浏览器会话交出去。它适合收集报表数据、下载供应商发票等可交付的网页任务，而 Claude in Chrome 更适合操作用户已经打开、已经登录的页面。

隐私边界是这项设计的核心。文中的说法很直接：“它是 Claude 的浏览器，不是你的。”（译）内置浏览器默认看不到用户的标签页、书签和密码；登录状态需按站点选择性导入，银行、邮箱和单点登录站点也不会自动包含。已有 Claude in Chrome 的用户仍以扩展为默认方式，其他用户则默认使用内置浏览器，并可在设置中切换。

该能力本周向 Pro、Max 和 Team 计划逐步开放，Enterprise 管理员现在即可启用。它沿用 Claude in Chrome 的 prompt injection 防护，但官方同时承认风险无法被彻底消除，建议先从可信网站开始使用。

https://claude.com/blog/cowork-built-in-browser

Generated through the Follow Builders skill: https://github.com/zarazhangrui/follow-builders
