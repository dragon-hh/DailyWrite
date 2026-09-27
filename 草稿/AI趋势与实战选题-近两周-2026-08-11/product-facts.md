# 关键产品与技术事实核验

核验日期：2026-08-11。以下只核验报告最终会重点引用的产品能力；其他条目在 HTML 中以“日报称/Builders 观察”表述，不扩展成未经核验的产品承诺。

## 已由官方或官方仓库确认

1. **Codex Security CLI / TypeScript SDK**
   - OpenAI 官方仓库明确提供 `@openai/codex-security` CLI 与 TypeScript SDK，可做 repository/path/diff/working-tree 扫描，支持 `validate`、`patch`、`--fail-on-severity`、`--max-cost` 与 pre-commit hook。
   - https://github.com/openai/codex-security/blob/main/sdk/typescript/README.md
   - https://openai.com/index/codex-security-now-in-research-preview/

2. **Claude Code auto mode 与环境隔离原则**
   - Anthropic 官方工程文章说明用户批准约 93% 权限请求；auto mode 用模型分类器减少审批疲劳，但仍会漏过部分风险行为，因此只是 defense-in-depth 的一层，不能替代 sandbox、VM、文件边界与 egress control。
   - https://www.anthropic.com/engineering/how-we-contain-claude

3. **Claude Code cross-session messaging**
   - Claude Code 官方 changelog 存在跨 session `SendMessage` 的加固记录，确认该机制已经进入真实产品面；接收端不会继承被转发消息的用户权限。
   - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md

4. **Cloudflare Browser Run 与 agent 浏览器可观测性**
   - Cloudflare 官方说明 Browser Run 支持远程浏览器、CDP、Live View、session recording、human-in-the-loop 和并发运行；Dynamic Workers 用 V8 isolate 执行短生命周期动态代码，并强调还需额外防御层。
   - https://blog.cloudflare.com/browser-run-for-ai-agents/
   - https://blog.cloudflare.com/dynamic-workers/

5. **Managed Deep Agents**
   - LangChain 官方说明 Managed Deep Agents 提供持久化 threads、checkpointing、streaming、context 与 observability，定位是把开源 Deep Agents harness 放进托管运行时。
   - https://www.langchain.com/blog/introducing-managed-deep-agents

6. **LangSmith Align Evals 与 LLM Gateway**
   - Align Evals 用人类评分校准 LLM-as-a-judge；LLM Gateway 代理模型调用，执行 spend limit、PII/secret redaction，并把每次调用写入 LangSmith trace。
   - https://www.langchain.com/blog/introducing-align-evals
   - https://docs.langchain.com/langsmith/llm-gateway

7. **Replit Agent 4 的设计与并行工作方式**
   - Replit 官方说明 Agent 4 支持 infinite canvas、多 UI variants、设计与代码同环境以及并行 agents。
   - https://replit.com/blog/introducing-agent-4-built-for-creativity

8. **GitHub Copilot app 的 session 形态**
   - GitHub 官方说明 session 可从 issue、PR、prompt 或 previous session 启动，每个 session 拥有独立 branch、files、conversation 和 task state，并可通过 PR 验收。
   - https://github.blog/changelog/2026-05-14-github-copilot-app-is-now-available-in-technical-preview/

9. **OpenRouter 的强弱模型协作能力**
   - OpenRouter 官方公告页列出 `subagent`（把自包含任务委托给更便宜模型）与 `advisor`（便宜模型在必要时咨询更强模型），支持本报告提出的 supervisor/worker 路由模式。
   - https://openrouter.ai/blog/announcements/

## 仅按本地日报引用、未扩展验证的条目

- Kitesurf、Token Saver、Numbat、ori CLI、ForgeStencil、Swiftlet、Soup、SpecForge、Seedance 2.5 API、Lyria 3.5、FLUX 3 Video。
- HTML 中可作为“本地日报收录的观察对象”出现，但不会写成已亲测、已全面上线或已达到某个绝对效果。

