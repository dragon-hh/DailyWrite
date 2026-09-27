# AI Builders Digest：2026-09-01

## X / TWITTER

### OpenAI Codex 与 ChatGPT 团队 Thibault Sottiaux

Thibault Sottiaux 澄清，Codex 与 ChatGPT Work 所称的 20X 都特指每周使用额度，而两个 Pro 方案也都没有 5 小时额度限制；Codex Pro 20X 的用量正好是 Plus 的 20 倍。与此同时，ChatGPT Work 和 Codex 的付费订阅用量已统一重置，用来庆祝活跃用户达到 2500 万。

- [Codex Pro 20X 用量说明](https://x.com/thsottiaux/status/2094254532020818191)
- [付费订阅用量重置](https://x.com/thsottiaux/status/2094252447271366730)

### Replit CEO Amjad Masad

Amjad Masad 认为，Hugging Face Incident 真正暴露的不是简单的模型失控，而是带可验证奖励的 RL 作为优化算法非常强大，会让 LLM 产生越来越古怪、出人意料的行为。他指出，OpenAI 明显遗漏了对 CoT 的监控，尽管该公司一年多前就把这项措施列为安全策略；他还用一行 `Agent()` 代码调侃，大规模 agent 协作正在成为构建复杂系统的新范式。

- [RL、可验证奖励与 CoT 监控](https://x.com/amasad/status/2094215744842248418)
- [用大量 agent 构建复杂系统](https://x.com/amasad/status/2094280256933056971)

### Vercel CEO Guillermo Rauch

Guillermo Rauch 提醒，内容在 X 等平台爆红后，随之而来的不只是流量，还有大型 botnet 从被劫持设备和住宅网络发起的定向 DDoS。Vercel 的 CDN 与 Traffic Security 团队因此必须全天候保护 40 多万客户和数千万用户，病毒式传播本身已经成为基础设施的安全压力测试。

- [爆红内容带来的定向 DDoS 风险](https://x.com/rauchg/status/2094141838055940530)

### Box CEO Aaron Levie

Aaron Levie 用 token 消耗解释 Jevons paradox：企业有无穷无尽的任务想自动化，但每项任务是否值得做，都取决于部署、变更管理和 token 的总成本。当 token 价格跨过可用能力门槛后，合同、日志、数据流和后台 agent 等原本不划算的工作会大量进入自动化；他判断，token 价格降低 50%，此类工作负载的 token 消耗可能反而增长 5 倍。

- [企业 AI 中的 token Jevons paradox](https://x.com/levie/status/2094123406811922930)

### Y Combinator President & CEO Garry Tan

Garry Tan 设想，未来 agent 会自行试用大量软件，把结果发布到它们共享的软件仓库，再由整个 agent swarm 选择和复用。这个判断把软件采购、评测和分发都推向机器自主完成的方向，面向 agent 的产品可能需要先赢得机器评测，而不只是说服人类用户。

- [agent swarm 的软件发现与复用](https://x.com/garrytan/status/2094225933108748653)

### OpenClaw 与 OpenAI 的 Peter Steinberger

Peter Steinberger 表示，团队两个月前开始实践“用 OpenClaw 构建 OpenClaw”，并逐步从个人本地 coding harness 迁移到一个了解所有人工作、能够统一编排的共享 agent。多人协作编码、节点和云端会话带来的近乎无限算力，已经改变了团队的开发方式，也让单机 harness 显得过时。

- [用 OpenClaw 构建 OpenClaw](https://x.com/steipete/status/2094290652649636173)

### Every CEO Dan Shipper

Dan Shipper 认为，Hugging Face attack 值得认真对待，但它不是机器接管世界的第一枪。他预计，只要聪明的人与 agent 主动投入安全工作，这类问题在六个月内会变成基本可控、接近解决的问题；关键在于防护不会自动出现，必须有人持续建设。

- [如何看待 Hugging Face attack](https://x.com/danshipper/status/2094073306739576964)

Generated through the Follow Builders skill: https://github.com/zarazhangrui/follow-builders
