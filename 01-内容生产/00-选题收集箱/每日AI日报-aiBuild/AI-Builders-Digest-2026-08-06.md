# AI Builders Digest · 2026-08-06

## X / TWITTER

### Swyx

Swyx 认为，ontology 和知识图谱现在重新升温，不是因为概念突然变新，而是因为“足够好”的智能已经便宜到近乎可以忽略成本。过去知识图谱最难、最贵的智能处理环节正在商品化，于是数据结构、上下文组织和知识连接这些互补能力反而更值钱。

- [原帖](https://x.com/swyx/status/2084832553895444570)

### Google VP Josh Woodward

Josh Woodward 介绍了 Notebook 的产品取舍：不堆叠模式切换，而是把不同能力收进一个统一的 prompt bar，让用户直接表达目标。该功能已向 Ultra 和 Pro 用户开放，之后会逐步覆盖所有用户。

- [原帖](https://x.com/joshwoodward/status/2084746170576892342)

### AI 教程创作者 Peter Yang

Peter Yang 提出一种更现实的 vibe coding 商业路径：SaaS 未必需要自己赚大钱，也可以成为高客单价服务的自助获客漏斗，不过这会重新落回“用时间换钱”的咨询模式。他还把复杂浏览器自动化视为自己一半的 Codex 使用场景，并关注更便宜、用量更宽松的 GPT 5.6 Luna High 能否承担这类任务；与此同时，他直言现在从 X 分成赚钱甚至可能比做 micro SaaS 更容易。

- [SaaS 作为服务漏斗](https://x.com/petergyang/status/2084855632029774167)
- [复杂浏览器自动化需求](https://x.com/petergyang/status/2084849701351035182)
- [X 分成与 micro SaaS](https://x.com/petergyang/status/2084846191456751725)

### Meta AI 高级总监 Madhu Guru

Madhu Guru 给创业团队的顺序是：先用最强 frontier model 做原型，不计成本与延迟，把用户体验和真实需求验证出来；再集中优化 prompt、model routing、harness、small model 和 fine-tuning。等 6 到 8 周后 open-weight model 追上来，再迁移生产负载；他认为很多团队的问题不是不会优化，而是长期停留在昂贵的验证阶段。

- [先验证、后降本的 playbook](https://x.com/realmadhuguru/status/2084809416105472070)
- [验证模型与生产模型不是一回事](https://x.com/realmadhuguru/status/2084667443046502631)

### Vercel CEO Guillermo Rauch

Guillermo Rauch 用 FactoryAI 的案例说明 Vercel 的后端能力：其 API 服务运行在 Fluid compute 上，每月处理数十亿次请求。他还称，在 AI SDK 中增加一行代码，就能为 DeepSeek v4 Flash 的 AI Gateway token 节省 90% 以上。

- [FactoryAI 的 Fluid compute 案例](https://x.com/rauchg/status/2084804138169446449)
- [AI SDK 的 token 节省](https://x.com/rauchg/status/2084779435866398801)

### Box CEO Aaron Levie

Aaron Levie 观察到，企业采用 AI 的路径远比早期 cloud 多样：coding agent、员工生产力 agent、模型选择、数据访问身份和安全边界都没有统一答案。有的企业标准化到 ChatGPT 或 Claude，有的允许多模型并存，还有的自建 orchestration layer；这种早期异质性意味着市场格局还会变化很多年，现在断言最终赢家大概率都太早。

- [原帖](https://x.com/levie/status/2084828773808239080)

### FirstMark VC Matt Turck

Matt Turck 借 Airtable 的退出讨论点出 SaaS 创业者的真实心理：旁观者嫌成交价低，许多创始人却会把“至少成功退出”视为求之不得的结果。它提醒人们，舆论中的估值期待与经营者真正面对的退出概率并不是一回事。

- [原帖](https://x.com/mattturck/status/2084759190195536202)

### Builder Zara Zhang

Zara Zhang 认为，新技术扩散首先是社会和情绪过程，而不是效率计算：人们看到相似的人因采用技术而变得更成功，或感到周围人都已采用，才会行动。因此，AI 推广不该只说“效率提升 10 倍”，更有效的方法是展示可代入的同类榜样；企业做 AI 培训也可以先把 agent 拉进团队群，让员工直接看它工作。她还把高效会议重新定义为现场工作会：人或实时旁听的 agent 当场完成行动项，让“说”和“做”之间的间隔归零。

- [技术扩散是社会过程](https://x.com/zarazhangrui/status/2084828855404294266)
- [让团队看着 agent 工作](https://x.com/zarazhangrui/status/2084635984164237792)
- [会议中直接完成行动项](https://x.com/zarazhangrui/status/2084601752817729811)

### Every CEO Dan Shipper

Dan Shipper 判断，当前因 AI 引发的“能动性断裂”最终会愈合：当 AI 再次变成看不见的基础设施，人们关注的仍会是人类完成了什么。届时使用 AI 会成为默认条件，而不是需要特别标注的英雄叙事。

- [原帖](https://x.com/danshipper/status/2084634391079469390)

### SPC General Partner Aditya Agarwal

Aditya Agarwal 介绍了 Rivo 的“自动驾驶金融”：agent 连接现有支票账户，学习现金流，把闲置资金转入 Treasury-backed yield，并在账单到期前调回；真正困难的是不对称成本下的预测，早一天损失少量收益，晚一天却可能导致账单跳票和信任崩塌。他同时强调，大规模部署 AI 不该接受黑盒，理解 LLM 内部发生了什么是可靠落地的关键一步。

- [Rivo 的自动驾驶金融](https://x.com/adityaag/status/2084691244496625793)
- [AI 规模化与可理解性](https://x.com/adityaag/status/2084676740924764625)

### Sam Altman

Sam Altman 选择做一个努力行动的乐观主义者，而不是不断论证事情为什么不会成功的悲观主义者。尝试更难、失败也更可能，但如果没人愿意承担这种失败风险，社会就不会前进。

- [原帖](https://x.com/sama/status/2084663673570971990)

## PODCASTS

### Training Data：Chai Discovery's Bitter Lesson: Drug Design Is Another Scaling Problem

**核心结论：药物设计正在变成另一个 scaling problem，真正的突破来自更简单、可扩展的模型，加上能持续验证的实验闭环。**

Chai Discovery 联合创始人 Josh 和 Matt 想把“药物发现”改造成“药物设计”：研究者先描述目标分子的理想属性，模型生成候选，再用实验室做客观验证。关键进展不是少做实验，而是提高每轮实验的 ROI，把从想法到可测试假设的周期从九个月压到九周乃至九天。

他们最反直觉的选择是拒绝为每个新靶点不断增加专用模块。Chai 早期模型有约 23 个子模块，复杂度让迭代和 scaling law 都难以判断，于是团队回到 bitter lesson：扩大 data、model 和 compute，同时保持架构简单、评估严格。正如 Matt 所说：“一旦抓住真正重要的东西，整个研究过程和识别 scaling 方向都会简单得多。”

结果已经跨过实用门槛：传统 antibody design 的 binding 成功率约为 0.1%，Chai2 达到约 15%，意味着测试 1,000 个分子时，不再只得到 1 个命中，而可能得到约 150 个，从而有空间继续筛选可制造性等药物属性。Chai 选择向 Eli Lilly、Novartis、Argenx、Pfizer 等药企提供基础设施，而不是自己押注少数药物管线，因为广泛合作迫使模型在更多目标上真正泛化，也让收入继续投入下一代模型和数据飞轮。

- [观看本期节目](https://www.youtube.com/watch?v=wv53mDmY-k0)

Generated through the Follow Builders skill: https://github.com/zarazhangrui/follow-builders
