AI Builders Digest — 2026-06-08

## 🎙️ 播客

### Unsupervised Learning: AI Research Legend's Honest Assessment of Where We Are

**核心观点：** Transformer 论文作者之一 Lukas Kaiser 认为，尽管当前 AI 取得了惊人进展，但 LLM 的泛化方式与人类存在本质差异——人类能从极少数据中提取深层概念，而模型需要海量数据才能"穷尽所有其他选项"后学到同样东西。这暗示着 Transformer 之后可能存在更优雅的架构。

**嘉宾背景：** Lukas Kaiser 是 Transformer 论文作者之一，曾在 Google 和 OpenAI 担任重要研究角色，现为独立研究者。

**关键洞察：**

- **关于泛化与推理：** Kaiser 承认 LLM 在推理加持下已能完成惊人任务（他每天花数小时与 Codex 讨论研究问题），但指出一个根本矛盾："人类能从极少数据中提取概念，而 LLM 需要先穷尽万亿 token 的所有表面模式，最后才学到真正概念。"他将此比喻为"美国人会在耗尽所有其他选项后才做正确的事"——LLM 也会学到概念，但效率极低。

- **关于 Transformer 的未来：** 他认为 Transformer 和推理能力都在持续进步，但"某种新架构的需求也在同步增强"。目前多个实验室正在探索 post-transformer 架构，已有有趣的小规模结果（如 TRM 和 HRM 模型在 Sudoku 等任务上表现优异），但尚未证明能在语言任务上 scale up。

- **关于 Agent 对研究的改变：** Kaiser 透露了一个量化数据——用 Codex 复现一篇旧论文，原本需要 3 周，现在只需 2 天，约 10 倍效率提升。更关键的是，这改变了研究节奏：可以并行启动多个项目，同时保持对"大画面"的掌控。他甚至认为这让自己的思维更敏锐，因为"你不需要记住每个类名，但必须清楚知道损失函数和 batch 在做什么"。

- **关于 Codex 的局限：** 他直言 Codex 接近"实习生"水平，但"你需要非常仔细地检查"——它可能自行添加一个你根本没要求的辅助损失函数，因为"这对它来说似乎合理"。他尝试过让 Codex 独立优化模型 overnight，但结果总是"一些非常微不足道的调整，不真正有趣或有用的"。

- **关于 RL 的泛化：** Kaiser 认为 RL 的泛化确实存在，但"以一种奇怪的外星人方式"——比如从数学到法律有迁移，但"即使从数学的一个子领域到另一个子领域，有时也不迁移"。他形容这是"锯齿状的泛化"：在某些方向很强，在看似接近的方向上突然失效。

- **关于硬件与研究的民主化：** 他提到一个惊人对比——当年研究 Transformer 时用的 GPU 只有 9 teraflops，而现在一张 RTX 5090（约 200 teraflops）相当于当时 5 台机器的算力。这意味着"一个大学生现在可以在几天内跑完相当于人类十年的学习量"——如果他有正确的算法的话。

- **关于开源 vs 闭源：** 他认为大模型确实更容易使用，但"小模型也在快速进步"。关键问题是：如果 post-transformer 架构出现，大实验室能否像当年押注 reasoning 一样果断转向？他担心公司变大后"更难下这种 wild bet"。

**最值得记住的一句话：**
"LLM 会学到概念，但总是在穷尽所有其他选项之后。你需要万亿 token，需要学完所有表面层面的东西，只有当那无法解释某事时，它才终于学到概念。这不是我们人类的学习方式。"

🔗 https://www.youtube.com/watch?v=N1geOimmdDo

---

Generated through the Follow Builders skill: https://github.com/zarazhangrui/follow-builders
