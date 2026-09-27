AI Builders Digest — 2026-06-07

## X / Twitter

**Swyx** (Latent Space, AI Engineer, DX Tips)
- 分享了一个更聪明的 AI 使用技巧：与其用 "plan mode"，不如把任务框成一个问题，让模型有机会反驳和评估想法质量，而不是盲目执行。他建议在 prompt 末尾加个问号，就能触发这种效果。
- 提到了 AI Engineer 在伦敦的 AGI pills 活动。

https://x.com/swyx/status/2063082950317486133

**Boris Cherny** (Anthropic, Claude Code)
- Claude Cowork 的使用限制翻倍了（5小时限制），鼓励用户趁这个月尝试处理那些一直拖着的大项目。
- Cowork 最适合处理聊天搞不定的工作：跨多个账号的研究、定期报告、整理收件箱和起草回复。

https://x.com/bcherny/status/2063028954546733462

**Thibault Sottiaux** (OpenAI, Codex & ChatGPT)
- "更好的记忆 = 更短的 prompt = 每个 token 更有价值" — 强调记忆系统对提升 AI 实用性的关键作用。
- Codex 的用户体验在持续改善，采用率也在上升。

https://x.com/thsottiaux/status/2062966625733861752

**Peter Yang** (Product at Roblox, AI 教程作者)
- 分享了一套构建自进化 AI skills 的完整方法：给上下文、写好触发描述、添加 evals（自动评估）、添加记忆系统、再建一个 skill 来优化其他 skills。
- 刚采访了 Mike Van Horn，一位没有 CS 学位却给 Python 和 Go 贡献代码的开发者，强调 Every 的 Compound Engineering 方法。

https://x.com/petergyang/status/2062899832965255443

**Madhu Guru** (前 Google Product Leader, Gemini/Veo)
- 企业 AI 团队最常见的错误：只为当前模型的能力和价格做设计。应该向前看 6 个月，模型会更聪明更便宜。围绕今天的模型弱点搭建脚手架，等下一代模型原生解决后，再推向下一个前沿。这种反复识别和填补模型空白的能力，本身就是一种护城河。

https://x.com/realmadhuguru/status/2063024953721827329

**Amjad Masad** (Replit CEO)
- Replit 和 Shopify 的合作官宣。
- 转发了一些关于 AI 时代工程师角色的讨论。

https://x.com/amasad/status/2063065480878063694

**Guillermo Rauch** (Vercel CEO)
- Vercel 推出了全新的虚拟存储基础设施：Agent 文件系统状态可以独立于 Sandbox 生命周期进行读写和挂载。这种存储可以解耦，但又能附加到 Builds、Functions、Sandboxes 等产品上。
- 推出了 Skills API，定位为 "agent 能力的 npm registry"，免费且开放。

https://x.com/rauchg/status/2063009510503932181
https://x.com/rauchg/status/2062951924677128455

**Aaron Levie** (Box CEO)
- 关于 AI 替代工程师的讨论：Coding 是 AI 自动化最理想的场景（可验证、上下文数字化、用户技术能力强），但即便如此，我们仍然需要人类工程师监督 agent。知识工作的大部分领域不具备这些优势，所以 AI 对工程师的冲击被高估了 — agent 让人做得更多，但人不会消失。

https://x.com/levie/status/2063055332545540096

**Ryo Lu** (Cursor 设计)
- 在 Cursor 里设计代码现在简单到：点击、聊天、按住 shift 多选。Composer 2.5 让设计流程更顺畅。

https://x.com/ryolu_/status/2063038983408615435

**Garry Tan** (Y Combinator CEO)
- GBrain 给 OpenClaw 和 Hermes Agent 增加了能力。
- 启动了一个新项目，目标是帮助开发者学习最佳实践，更快构建更好的软件。

https://x.com/garrytan/status/2063146456106795457

**Matt Turck** (FirstMark Capital VC)
- 调侃了当下 X 上关于 VC 的负面故事，反讽说创始人也有 horror stories：比如创始人拿了更高估值的 term sheet，尽管你明显能提供更多价值。

https://x.com/mattturck/status/2063035894790345200

## Podcasts

**AI & I by Every** — "The SaaS Apocalypse Is a Goldmine With Figma's Matt Colyer"

Figma 开发者产品总监 Matt Colyer 做客节目，核心观点：所谓的 "SaaS 末日" 其实是金矿。

他分享了一个关键洞察：全球开发者数量可能从现在的几千万增长到 10 亿。软件会爆炸式增长，这对 SaaS 公司是巨大机会，不是威胁。他用自己的亲身经历说明：两年前他写了个邮件 agent 来处理孩子学校的 PTO 邮件，但维护成本让他意识到 — 自己造软件很有趣，但运行软件很痛苦。他现在买的软件比以前还多。

关于 Figma 的 AI 策略，Colyer 强调了两点：1) 支持第三方 agent 通过 MCP 接入；2) 自己也在开发 agent。他们看到了两个方向：code to design（用 agent 把代码同步到 Figma 画布）和 design to code（把设计变成 PR）。他认为未来的设计 agent 应该能在画布上主动发散思维（生成多个方案），也能收敛思维（评估哪个最好），而不是局限在聊天框里。

最让他兴奋的是 "proactive agent" — 不是你去问工具，而是工具主动来找你。就像他的邮件 agent 每天定时发摘要，而不是等他打开邮箱。

https://www.youtube.com/watch?v=kYKebKB3-d0

---
Generated through the Follow Builders skill: https://github.com/zarazhangrui/follow-builders
