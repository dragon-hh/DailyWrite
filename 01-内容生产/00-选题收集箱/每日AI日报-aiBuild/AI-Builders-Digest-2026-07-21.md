AI Builders Digest ｜ 2026-07-21

# X / TWITTER

## Thibault Sottiaux（Codex & ChatGPT 团队，OpenAI）
Thibault 在收用户关于 ChatGPT Work 的故事，受之前 DM 启发，这次专门征集"ChatGPT 给生活带来过深度正面影响"的真实案例，希望听到具体的人和事。
https://x.com/thsottiaux/status/2079058139207573541

## Cat Wu（Claude Code + Cowork，Anthropic）
Cat 分享了她用 Claude Cowork 管理一周日历的 prompt 范式：硬约束 <20 小时会议、合并冲突项、按历史偏好推断自己会拒绝的会议类型、晚宴不计入上限，并且让模型把判断沉淀成可复用的 skill，每次改动前先问她。本质上是把 LLM 当成一个会学习的执行助手，而不是一次性的工具调用。
https://x.com/_catwu/status/2079011428380602526

## Thariq（Claude Code，Anthropic）
Thariq 提醒用户遇到 bug 后重启 Claude Code，修复正在持续推送中。另一条预告他正在写一篇长文，系统复盘他们做 Claude Code skills 与 system prompt 的经验，以及如何把同一套方法迁移到你自己的项目里。
https://x.com/trq212/status/2079103743535280508
https://x.com/trq212/status/2078901672441790818

## Amjad Masad（CEO，Replit）
Amjad 给出一个关于"消费级订阅天花板"的判断：普通消费者主要把钱花在食品、房租、娱乐、电话 / 宽带和购物上，软件通常由公司采购，所以除 Netflix、Spotify 之外，几乎找不到真正的大体量 C 端订阅业务。这条对正在做 to C AI 订阅产品的团队是个清醒剂。
https://x.com/amasad/status/2079086360703680583

## Guillermo Rauch（CEO，Vercel）
Rauch 提出一个反主流观点：网络安全才是衡量超智能的最佳基准之一，比"一键复刻某个 XYZ 克隆版"的 demo 含金量高得多。真正考验模型的是"发现、打补丁、逆向、利用"这一整套链路，需要跨语言、跨运行时的推理能力，含大量 corner case reasoning，人类工程师里也只有极少数擅长。他特意提到 Kimi K3 在这类任务上的表现，认为这是开源模型走向强推理的好兆头。
https://x.com/rauchg/status/2078912929714356698

## Aaron Levie（CEO，Box）
三条值得展开的判断：

1. 开源权重模型比想象中更强，AI 监管的算式必须随之调整。如果 gatekeep 前沿模型能力、禁止开源，即便美国能禁，其他生态也不会禁，等于把工具送给对手，反而让本国企业在能力上掉队。

2. AI 成本下降不会让总支出下降，反而推高需求。token 更便宜之后，你能负担得起把它用在更广的任务上：写更多代码、审查更多 bug、在原本处理不动的大数据集上跑 agent。这也是 AI 开源商业模式能跑通的根本原因，没有人在本地跑模型，所有人都在算力上花钱，对算力供应商是大时代。

3. AI 落地的真正瓶颈是现实反馈速度。编程之所以最先被大规模采纳，是因为一个人可以在闭环内写、测、跑，端到端交付价值，不需要外部世界配合。生命科学要做几年临床、销售要来回谈判、合同要对方点头，这些都是现实反馈的天然延迟。所以"模型输出"本身远远不够，你需要的 applied AI 是把智能嵌入到行业工作流里，并设计系统去处理真实的反馈回路。这是应用层 AI 真正的机会所在。
https://x.com/levie/status/2078992778449850769
https://x.com/levie/status/2078968158006939716
https://x.com/levie/status/2078864191683969212

## Garry Tan（President & CEO，Y Combinator）
Garry 力推 Markdown 作为智能栈剧烈变动时代的"长青"数据格式：人类可读、跨工具可解析、能存活千年。同时打出一个新概念 GSkills，把 skills 当成可复用、可堆叠的 AI 能力单元，顺着他一直在做的 GStack / GBrain 体系延伸。
https://x.com/garrytan/status/2078803803659452624
https://x.com/garrytan/status/2078803084785111120

## Zara Zhang（独立 Builder）
两条观点合起来读很有意思：
- "代码现在可以是一次性的"：AI 让为某个特定问题临时写一段代码再扔掉成为常态，比如为了微调设计感的临时 playground、为理解一段代码逻辑的 HTML 页面、看完即弃的 dashboard。开发者应该接受这种"用过即弃"的心智。
- 给刚开始做内容的人一条务实建议：被朋友 / 同事反复问过的 top 3 问题，就是你最该拍的内容。说过的次数 ≥ 3 次，就值得拍成视频或写成帖子，动机之一就是为了让自己不在真实生活里再说第 N 遍。
https://x.com/zarazhangrui/status/2078835308905578660
https://x.com/zarazhangrui/status/2078830510177128481

## Dan Shipper（CEO，Every）
Dan 透露一个内部里程碑：AI 终于"过线"了，过去一周 Every 内部约 70% 的 copy edits 可以由模型自动完成，这是他多年来第一次达到这个比例。他认为这意味着写作型工作流正在发生质变，AI 不再只是 draft helper，而是可以直接接手大部分的 edit 工作。
https://x.com/danshipper/status/2078920115140358585

# PODCASTS

## "Stripe's AI Chief: How AI Agents Will Buy, Sell, and Pay"｜ The MAD Podcast with Matt Turck

嘉宾 Emily Glanz（Stripe 数据与 AI 负责人）与 Matt Turck 重谈 agentic commerce，回顾了过去一年从"假设"走向"基础设施可用"的关键变化。几个最值得记住的判断：

**一、agentic commerce 是一整个光谱，不只是"全自动"。** 最左端是机器支付协议（MPP）下的 agent 完全自主发现服务、下单、付款，没有任何人类在环；最右端是人在 AI 搜索界面里被推荐一双跑鞋然后点 buy button。Stripe 的 Agentic Commerce Suite 在两端都提供服务，关键是中间这一整条光谱都需要同样的基础设施：商家要暴露 catalog / inventory / 价格，消费者要授权 agent 代付，agent 要安全执行交易。

**二、Agentic Commerce Protocol（ACP）是新的"MCP for commerce"。** 由 Stripe 与 OpenAI 去年秋天联合发布，核心两件事：（1）商家一次接入，向所有支持 ACP 的 agent 暴露商品和库存，避免每个 agent 都要单独注册；（2）Shared Payment Token，把消费者的支付凭证抽象为带额度、币种、有效期、商户范围限制的 token，agent 永远拿不到原始卡号。Best Buy、Coach、URBN、Kate Spade、Quince、Fanatics、JD Sports 已接入品牌侧；Wix、Shopify、BigCommerce、CommerceTools 接入平台侧；Gemini、Microsoft、OpenAI 接入 agent 侧；Meta 则把"广告本身变成 agentic buying"作为一个有意思的延伸。

**三、自主级别分层，类似自动驾驶的 L1–L5。** 消费者一侧目前大多停留在 L2：你让 AI 帮你选一双鞋、点 buy button，但最终拍板还是你。真正的 L3（"我有 500 美元预算帮孩子搞定返校用品，你自己看着办"）还要时间。

**四、Link Wallet for agents 取代一次性虚拟卡。** 最早 Stripe 在 Perplexity Shopping 上跑通的是一次性虚拟卡方案，安全性好但灵活性差。新的 Link Wallet 基于 Shared Payment Token，可以设预算、按商户类别 / 国家 / 单笔限额管控、可随时撤回授权，也支持稳定币等不同底层凭证。Emily 强调，即便如此，今天消费者仍然会要求"每笔都过我"，这种控制感本身是信任建立过程的一部分，跟早年人们不敢在网上输信用卡是一个道理。

**五、"Token theft"是 AI 时代最被低估的话题。** 不偷钱也不偷卡，直接偷 token：拿到免费积分、倒卖、用别人的模型包成新产品。Stripe 数据披露，超过 1/6 的 AI 公司新注册账号属于多账号滥用（multi-account abuse），自由试用滥用过去六个月翻了一倍多，还有一类是月底产生大额 usage-based 账单然后直接走人的"吃霸王餐"。和 SaaS 不同，token 是有真实边际成本的，所以这类欺诈对 AI 公司是"成则废"的级别。

**六、"Vibe coding 已解决，Vibe deployment 是新的长杆。"** Emily 抛出的一个数据点：Stripe 文档的 agent 流量过去一年涨了 10 倍，现在约占所有文档流量的 40%；Stripe CLI 的资源请求中，约 70% 来自 agent。这意味着"写代码"已经不是瓶颈，瓶颈变成把应用真正部署上线、串好数据库、auth、hosting、email、监控、密钥等一整套服务——每一家当初都是给人类做 onboarding wizard，现在需要给 agent 提供同样的能力。Stripe 推出的 Stripe Projects 就是为此设计的编排层，已接入 Vercel、Supabase、Cloudflare、Twilio、Clerk 等十几家。

**七、AI 公司的计费正在从订阅走向混合 / 实时计量。** SaaS 边际成本接近零，订阅是天然货币化方式；AI 不行，每条 prompt 都有真实成本，必须按 usage 计量。Stripe 看到绝大多数规模化 AI 公司都已经从纯订阅过渡到"订阅 + 用量"混合模型（Lovable、ElevenLabs 都是这条路）。当消费方变成 agent、消耗速率变成机器级时，连"月底结算"都不够用，需要的是实时计量 + 实时结算，Stripe × Metronome × Tempo 的组合正是为此而生；同时也催生出新的财务岗位："能写代码的会计"，负责在海量微交易里既关账，也识别异常、欺诈、产品破损。

**八、agent-to-agent 交易今天还基本不存在，但方向明确。** Emily 用 Ronald Coase 的视角看：如果未来买卖双方都是 agent，市场摩擦被压到极低、撮合效率空前、合同 / 集成 / 履约都被自动化，理论上能显著提升经济增长。但 today 还几乎没有真正的 agent-to-agent 真实交易，"先做好一侧，再加上另一侧，最后两边都到位"。她对宏观经济最大的乐观不只来自消费效率提升，而是 AI 正在让个人创业者（nonemployer firm / solopreneur）真的能"从想法到上线、从上线到运营"，vibe coding 解决造物，vibe deployment + 垂类 agent 解决运营，整体拉动 business dynamism。

**九、安全层面：agentic commerce 长期可能比"人手刷卡"更安全。** token 不经过不可信服务、每笔都被 Radar 实时打分、商家保留 merchant of record 身份、不存在"人在陌生网站手输卡号"的环节。短期收益主要是便利，长期收益才是安全。

资源链接：
https://www.youtube.com/@DataDrivenNYC/videos

---

Generated through the Follow Builders skill: https://github.com/zarazhangrui/follow-builders
