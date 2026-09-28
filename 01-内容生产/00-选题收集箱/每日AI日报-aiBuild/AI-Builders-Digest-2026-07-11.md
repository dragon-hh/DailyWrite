AI Builders Digest — 2026-07-11

## X / TWITTER

### Swyx，AI Engineer / Latent Space 相关 builder
Swyx 观察到一个很实用的 AEO 现象：多个 frontier model 在写邮件功能时，即使项目里已经有现成的 transactional email infra，也会主动倾向使用 Resend。这说明面向 AI agent 的“被模型优先选择”正在变成新的开发者获客入口。
https://x.com/swyx/status/2075376938676621752

他还把 OpenAI 的新动作和 Greptile 之前被调侃的方向联系起来，暗示代码 agent 领域正在从“被嘲笑的 demo”快速进入大厂重兵投入阶段。
https://x.com/swyx/status/2075336806661509513

### Josh Woodward，Google / Google Labs / Gemini App / Google AI Studio VP
Josh Woodward 汇总了 Gemini 用户 12 小时内 1400+ 条反馈，优先级非常产品化：Workspace 集成可靠性、tool calling、项目和文件夹组织、MCP 与 Custom Skills、Deep Research 导出到 NotebookLM、移除 Nano Banana 水印、编辑历史消息、语音输入、移动端滚动 bug。最值得注意的是，Google 已经把 MCP、custom skills 和 connected apps 放进 Gemini Spark 的早期支持里，但还在扩大发布范围。
https://x.com/joshwoodward/status/2075241749048401936

### Thibault Sottiaux，OpenAI Codex & ChatGPT
Thibault Sottiaux 宣布，为庆祝 GPT-5.6 Sol 发布，ChatGPT Work 和 Codex 的 rate limits 会在 24 小时内再重置两次，目的就是让用户可以真正尝试更有野心的任务。
https://x.com/thsottiaux/status/2075452680760443190

他还提到 ChatGPT Work 和 Codex 已经进行了一次完整 usage limits reset，并说 Rajan Agarwal 加入后会推动 model research 和 coding capabilities。信号很明确：OpenAI 正在把 Codex 放到新的 work product 核心位置上，并鼓励用户用更长、更复杂的任务压测。
https://x.com/thsottiaux/status/2075330198887940337

### Peter Yang，AI 教程与产品观察者
Peter Yang 对 OpenAI 新发布给出了一组很具体的产品反馈。他认为 OpenAI 最有机会把 agent 工作流推向主流，因为 ChatGPT 已经把图像、实时语音、browser/computer use 和插件整合得像“能学习、能执行白领工作的同事”。
https://x.com/petergyang/status/2075345016437039600

他的主要肯定是 GPT-5.6 Sol 在复杂任务上“很不容易放弃”，但主要担忧是产品命名和入口过于复杂：ChatGPT Work vs. Codex、Sol/Terra/Luna、effort 档位、tasks vs. chat 都会让普通用户迷路。他建议尽快统一到 ChatGPT、Codex 或 ChatGPT Codex，而不是继续用 tab 和 toggle 拆体验。
https://x.com/petergyang/status/2075345016437039600

### Nan Yu，Linear Head of Product
Nan Yu 对创业公司融资视频的“炫耀式发布”表达了产品人式怀疑：如果视频只是两个人对着屏幕聊一个很大的融资数字，它到底怎样帮助业务？这条不是模型发布消息，但对 builder 有用：叙事应该服务产品和分发，而不是只服务估值展示。
https://x.com/thenanyu/status/2075369080006087127
https://x.com/thenanyu/status/2075369895408095511

### Madhu Guru，Meta AI Senior Director
Madhu Guru 宣布加入 Meta 做 AI products。他的判断是，SWE agents 已经改变了软件工程，但大多数复杂系统里的 agent 还非常早期，普通用户还没有真正感受到 AI agents 的全部力量。他认为 Meta 有机会把这种能力带到更广的人群和场景里。
https://x.com/realmadhuguru/status/2075243087325217038

### Thariq，Anthropic Claude Code
Thariq 给 agentic coding 提了一个很短但关键的判断：核心能力之一是“减少未知数”。这和成熟工程实践很贴近，真正有效的 coding agent 不是盲目生成代码，而是不断缩小不确定性，确认边界，再行动。
https://x.com/trq212/status/2075283841758183674

他还转发了 Fable 相关更新，语气上是鼓励用户继续使用更多 Fable。
https://x.com/trq212/status/2075280416995705312

### Amjad Masad，Replit CEO
Amjad Masad 提出一个很好的工程悖论：AI 让 coding 变得更灵活，但 runtime 反而需要更刚性。他观察到 Replit 的 infra 团队开始写 formal specs，追求更 deterministic、更 resilient 的基础设施。结论很硬：“你越想跑得快，脚下的地面越要稳。”
https://x.com/amasad/status/2075423115052790054

他还认为 LLM 市场在短时间内变得非常动态。6 个月前很多 VC 还相信 Anthropic 可能形成垄断，但现在市场已经证明强模型会来自多个实验室和新进入者。
https://x.com/amasad/status/2075413916491075755

此外，他提醒用户可以在 Replit 尝试 Fable。
https://x.com/amasad/status/2075358353686208741

### Guillermo Rauch，Vercel CEO
Guillermo Rauch 认为这是 model release week，并预测 Meta Spark 1.1、Grok 4.5、GLM 5.2 可能显著改变 token 市场份额。他的判断点在于，大多数 agentic tasks 需要“足够高的智能 + 很快的速度”，所以模型路由和 AI Gateway 这类基础设施会变得更关键。
https://x.com/rauchg/status/2075294130327196152

他还补了一句：open models 很快会变得“极其快”，值得继续关注。
https://x.com/rauchg/status/2075294327354577256

### Aaron Levie，Box CEO
Aaron Levie 把 AI 时代的企业竞争优势问题讲得很清楚：如果每个行业最好的数据都会被 AI 学到，法律、金融、医疗、生命科学里的 intelligence 都变得更丰富，那么公司未来靠什么差异化？他的答案不是“模型本身”，而是模型智能、公司自有数据、工作流连接方式、员工使用系统创造价值之间的增强循环。
https://x.com/levie/status/2075416313481290077

他还分享了 Box AI Complex Work eval 中 GPT-5.6 Sol 相比 GPT-5.5 的表现：金融服务 76% vs 71%，医疗 58% vs 46%，公共部门 74% vs 63%，生命科学 60% vs 51%。他的核心判断是，Sol 在复杂、数据导向、需要深度推理和分析的企业任务上进步明显，尤其是在非结构化企业数据驱动的 agent 场景里。
https://x.com/levie/status/2075287443411222628

### Garry Tan，Y Combinator President & CEO
Garry Tan 表示 Meta Muse Spark 1.1 在他的 OpenClaw 上表现很好，并称赞 Alexandr Wang。这是一个短更新，但值得注意的是，builder 侧已经在真实工作流里测试新模型，而不是只看发布稿。
https://x.com/garrytan/status/2075445455438385255

### Nikunj Kothari，FPV Ventures Partner
Nikunj Kothari 用一条长段子总结了这一周模型发布的密度：GPT-5.6 分 Sol、Terra、Luna，Grok 4.5 抢在 GPT-5.6 前一天发布，Fable 5 回归，Sonnet 5 进入更便宜的默认层，Meituan 开源 1.6T 参数的 LongCat-2.0，ByteDance 推出 Seedream 5 Pro，OpenAI 发布 GPT-Live，Ollama 融资 6500 万美元。他的价值不在严肃分析，而是把“模型市场正在高速拥挤化”这件事压缩成了一张很有信息密度的快照。
https://x.com/nikunj/status/2075411514773967261

### Dan Shipper，Every CEO
Dan Shipper 抓住了 OpenAI 命名里的一个产品语义问题：如果叫 ChatGPT Work，那是不是暗示 developers 不做 work？这和 Peter Yang 的反馈一致，说明 Codex / Work / ChatGPT 的产品边界正在引发真实困惑。
https://x.com/danshipper/status/2075330044289802584

他还转发了“GPT-5.6 Sol 是 knowledge work gold standard”的观点，显示 Every 也在把 Sol 放进知识工作场景评价里。
https://x.com/danshipper/status/2075264022988116280

### Aditya Agarwal，South Park Commons General Partner / Bevel Health Co-founder
Aditya Agarwal 分享了与 Gagan Shux 的 SPC India 对谈，内容从申请 Indian Air Force、成为第二位进入太空的印度人，到 ISS 生活、微重力对身体和心理的影响、新太空经济、创业者机会以及 Moon/Mars 等未来探索方向。它不是直接 AI 内容，但对 builder 有启发：高压环境、长期训练和新产业窗口期如何塑造创业机会。
https://x.com/adityaag/status/2075414469497270557
https://x.com/adityaag/status/2075414473695703054

### Sam Altman，OpenAI
Sam Altman 表示 OpenAI 已听到企业对 AI 成本的担忧，GPT-5.6 Sol 以及 Terra、Luna 是改善 dollars-per-task 的重要一步。
https://x.com/sama/status/2075267201058426944

他还强调 Codex 是 OpenAI 新 work product 的核心，并明确说 Codex 不会消失。这和今天多位 builder 对 ChatGPT Work / Codex 命名和整合的讨论互相呼应。
https://x.com/sama/status/2075293792048136572

另外，他对 Fidji 离开或暂停相关消息表达了难过和感谢，并祝愿她早日恢复。
https://x.com/sama/status/2075354679031067058

## PODCASTS

### Unsupervised Learning — Ep 90: AI Pioneer Jürgen Schmidhuber on the State of AI Today
核心 takeaway：Jürgen Schmidhuber 认为真正的 AI 不只是屏幕里的 LLM，而是能在物理世界行动、通过自己的实验收集数据、形成世界模型的“人工科学家”。他对 AI 技术非常乐观，但对当下模型公司的商业护城河更悲观。

Schmidhuber 的几个观点很值得 builder 反复琢磨。第一，AGI 不能只停留在屏幕后面，robot hardware 和 physical AI 是真正缺口。他直说，目前真实世界硬件和人体相比还有很多限制，机器人要能操作现有机器，才可能进入自我复制、自我改进的更大循环。

第二，他把 recursive self-improvement 放回很长的历史里：从 1987 年的 meta evolution，到 1994 年的自指机器，再到 2003 年的 Gödel machine。今天常见的自我改进更像是这些思想的缩小版，主要依赖 neural network 权重更新和 gradient descent，所以有效，但还不是最一般的形式。

第三，他对当前 LLM 的批评是“人类偏置太强”。Web 数据只是人类觉得有趣的极小一部分，未来更关键的是 agent 像婴儿或科学家一样，通过自己的行动生成训练世界模型的数据，也就是 artificial curiosity。

第四，他不太相信 recursive self-improvement 会成为大公司的长期 moat。原因是很多关键 AI 算法来自小实验室和学术环境，开源和新研究者会持续扩散这些想法。他预期 AI 会越来越便宜，今天看起来惊人的能力，30 年后可能会像智能手机能力一样普通。

第五，他认为现在 AI 相关资本配置存在明显错配，可能出现 stock market 层面的重新定价，但这不是文明级 crash，而是市场学习和归一化。

最后，在 AI safety 上，他不接受单一 alignment 目标函数的朴素设定，因为人类目标本来就彼此冲突，真正聪明的系统也会不断提出新问题和新目标。他的更乐观判断是，人工科学家会对生命、文明和自身起源这些“有趣模式”保持强烈兴趣，因此更可能保护这些模式，而不是摧毁它们。

值得记住的一句话：智能的一个自然结果，是用越来越少的资源完成同样的事。

https://www.youtube.com/watch?v=RKjR8DQ40po

Generated through the Follow Builders skill: https://github.com/zarazhangrui/follow-builders
