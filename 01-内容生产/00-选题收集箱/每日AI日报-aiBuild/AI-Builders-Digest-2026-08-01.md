# AI Builders Digest：2026-08-01

## X / TWITTER

### Swyx（smol.ai、Cognition、AI Engineer、Latent Space）

Swyx 提出一个很值得注意的类比：既然模型可以被蒸馏，agent harness 也可以被蒸馏。这意味着团队未来优化的对象可能不只是模型能力，还包括工具调用、上下文组织和任务执行方式组成的整套运行结构。

- 原文：https://x.com/swyx/status/2083073422410821846

他还指出，高质量预训练数据会迫使顶级实验室自建全网抓取与索引系统，最终形成一个低频更新的私有 Google。这套基础设施不仅服务预训练，也会反过来支持 agent 的推理与检索，并成为不愿对外共享的竞争壁垒。

- 原文：https://x.com/swyx/status/2083016652032188669

与其让大量公司重复抓取网页、制造 bot 流量，他半开玩笑地建议把更多资金交给 Wayback Machine。背后的严肃问题是，AI 行业正在为同一份公共网络数据反复建设昂贵基础设施。

- 原文：https://x.com/swyx/status/2083064467383013569

### Google VP Josh Woodward

Josh Woodward 推荐了 Gemini Mac app 的一条低摩擦输入路径：按住 Fn 直接说话，整理后的文本会写入当前光标位置，不需要再编辑或复制粘贴。真正的产品价值不在语音转文字本身，而在于把 AI 润色嵌进用户已经在使用的输入界面。

- 原文：https://x.com/joshwoodward/status/2082926031543967896

### OpenAI Codex 与 ChatGPT 团队的 Thibault Sottiaux

Thibault Sottiaux 认为，真正更强的模型未必先以发布会形式出现，迹象可能是负载持续上升时可靠性反而提高、效率突然跃升、响应更快，以及系统出现重置。这个判断把观察重点从模型名称转向了运行层面的异常改善。

- 原文：https://x.com/thsottiaux/status/2083053369351090254

### Replit CEO Amjad Masad

Amjad Masad 认为，近期所谓“AI 逃出沙箱”的事件，很多首先是沙箱设计犯了基础错误，而不是 AI 突然变得不可控。Replit 从 2016 年起就在高强度攻击环境中运行沙箱，他给出的核心建议是：默认 zero-day 一定存在，并在 zero-trust 框架下建立多层防护。

- 原文：https://x.com/amasad/status/2083034412598579403

### Vercel CEO Guillermo Rauch

Guillermo Rauch 表示，Vercel 把许多应用从 CLI 到线上 URL 的端到端部署时间最多缩短了约 7 秒。更重要的是，这套基础设施可以通过 CLI、MCP 和 API 接入，让开发者在上面构建能够自主生成并部署软件的 agent 或软件工厂。

- 原文：https://x.com/rauchg/status/2082876367629381719

他同时确认，Grok Build 生成的应用由 Vercel 的托管与 CDN 基础设施承载。用户只需 prompt 后点击 Publish，就能把游戏、网站、内部工具或个人软件发布给从 1 人到大规模用户使用。

- 原文：https://x.com/rauchg/status/2082841035093467229

### Box CEO Aaron Levie

Aaron Levie 认为，agent 安全事件的关键结论不是“AI 很可怕”，而是企业环境中的配置和权限必须真正加固。只要工具、任务和算力足够，agent 会持续寻找完成目标的路径，因此任何看似封闭、实际存在缺口的系统都会变成风险入口。

- 原文：https://x.com/levie/status/2082997703458570412

他还指出，衡量 AI 成本时应该按任务能力归一化。前沿模型会因为能处理更高级的任务而显得昂贵，但效率提升和竞争随后会压低同类任务成本，这个循环将反复发生，并推动 AI 扩散到更多使用场景。

- 原文：https://x.com/levie/status/2082911418349920617

### FirstMark VC、MAD Podcast 主持人 Matt Turck

Matt Turck 把 Samsara 称为“很少有人谈论的最大 physical AI 部署”：系统每天覆盖美国 99% 的道路，积累 25 万亿个数据点，并把 agent 带入真实世界的车辆、安全和现场运营。这个案例提醒我们，physical AI 的规模可能早已存在，只是它不像聊天产品那样直接出现在大众视野里。

- 原文：https://x.com/mattturck/status/2082907699646173484

### Builder Zara Zhang

Zara Zhang 给管理者的 AI 培训建议不是先讲理论，而是举办一次“安装派对”：所有人带上电脑，当场装好 agent，并立刻完成一个有意义的任务。她的判断很直接，安装和设置占了采用门槛的 80%，一旦工具真的落到每个人机器上，团队会自然开始互相学习。

- 原文：https://x.com/zarazhangrui/status/2083084770763002350

### OpenClaw 与 OpenAI Builder Peter Steinberger

Peter Steinberger 批评 GCC 直接拒绝基于 LLM 的代码，认为这类政策不仅粗暴，而且难以证明一段代码究竟是否由 LLM 生成。争议的核心不是工具偏好，而是组织是否能提出一套可执行、可验证的代码质量与来源规则。

- 原文：https://x.com/steipete/status/2083019629379612728

### SPC General Partner、Bevel Health 联合创始人 Aditya Agarwal

Aditya Agarwal 介绍了风险预测工具 Preseen：产品已进行数周 private beta，一些量化基金和对冲基金正用它提前识别可能造成重大损失的风险。它把 forecasting 从观点输出推进到实际风控流程，目标不是预测一切，而是在高杠杆环境中减少被单一事件击穿的概率。

- 原文：https://x.com/adityaag/status/2083039973666644039

### Sam Altman

Sam Altman 表示，OpenAI 希望在每个层级都提供更好的价格与智能权衡。本次价格调整中，GPT-5.6 Luna 输入价格下降 80%，降至每百万 token 0.20 美元，输出为 1.20 美元；GPT-5.6 Terra 降价 20%，输入与输出分别为 2 美元和 12 美元；GPT-5.6 Sol 的 API 新增 Fast mode，以 2 倍价格换取最高 2.5 倍速度，同时保持相同智能水平。

- 原文：https://x.com/sama/status/2082880884525482061
- 价格详情：https://x.com/sama/status/2082880720989532597

## PODCASTS

### The MAD Podcast with Matt Turck：《The Biggest AI Deployment Nobody Talks About | Samsara CEO Sanjit Biswas》

**核心结论：physical AI 最大的机会，不是先用机器人替代所有人，而是先把尚未数字化的现实运营变成可感知、可推理、可执行的系统。**

Samsara 联合创始人兼 CEO Sanjit Biswas 此前在 MIT 读博期间共同创办 Meraki，如今带领 Samsara 服务运输、建筑、能源、公用事业和供应链等 physical operations。公司年经常性收入已超过 20 亿美元，保持盈利并以约 30% 增长；系统每年处理约 25 万亿个 GPS、视频和第三方数据点，覆盖数百万辆车与一线工作人员，并估算上一年帮助避免约 38 万起道路事故。

他的反常识判断是，现实世界不是软件 AI 的简单延伸。互联网已经积累了可直接训练模型的海量 bits，而工地、道路和电网没有现成的 token；硬件必须承受恶劣环境、不稳定网络和现场安装，错误还可能直接伤害人。Biswas 的概括是：“我们看到，风险本身就是机会，而不是挑战。”因此，可靠的 physical AI 必须把 GPS、摄像头、资产追踪器和外部数据融合起来，先给出判断，再在有护栏的流程中执行动作。

Samsara 的落地路径也很务实：从低风险、可验证的任务开始，例如保修审核、司机路线规划、疲劳和危险驾驶提醒，再逐步迈向全天候 AI ride-along。摄像头并不只用于监督，它更常见的价值是为司机免责、还原事故，并通过透明的数据规则换取一线人员信任。Home Depot 使用相关系统后，汽车索赔减少约 65%。

未来五到十年，Biswas 预计 physical operations 会形成混合队伍：机器人负责平整道路、仓储搬运等重复劳动，人类处理现场连续出现的例外与判断；自动驾驶在区域化 robotaxi 中扩散更快，在设备高度定制、长尾复杂的商用车辆领域可能需要十到二十年。真正紧迫的推动力来自基础设施：一家大型能源企业预计未来五年交付的电力将达到过去 125 年累计能力的三倍，其中 90% 新需求与数据中心有关。

- 原视频：https://www.youtube.com/watch?v=3FHsGiONOGw

Generated through the Follow Builders skill: https://github.com/zarazhangrui/follow-builders
