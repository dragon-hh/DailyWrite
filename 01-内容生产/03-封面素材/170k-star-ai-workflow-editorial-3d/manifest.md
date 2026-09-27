# 17万 Star 的 AI 开发流程封面

- 中文标题：17万Star的AI开发流程，小白也能抄
- 内容依据：`01-内容生产/01-脚本创作中/7.15 硅谷顶级工程师的最新AI开发工作流 -claude-v2-口播稿.md`
- 视觉锚点：25 个澄清问题、Spec 规范、Tickets 任务拆分、Implement 与测试验收、17 万 Star。
- 视觉隐喻：由提问卡片、规范文档、任务卡片和实现工作站组成的四段模块化流程，AI 工程师把模块依次推进，金色 Star 作为信任数字的视觉符号。
- 统一风格：暖白 3D 编辑场景、浅木与磨砂材质、柔和自然光；最终标题采用居中的现代黑体、深炭灰正文、低饱和香槟金重点词与轻柔投影。
- 生成方式：使用内置 imagegen 生成无文字的 3:4 底图，再使用本地确定性排版确保中文和数字准确。

## 成品

- `170k-star-ai-workflow-3x4.png`：1080×1440，抖音 / 小红书。
- `170k-star-ai-workflow-3x4-v2.png`：1080×1440，依据完整口播稿重做的中心粗体标题版。
- `170k-star-ai-workflow-3x4-v3.png`：1080×1440，取消娱乐化亮黄和粗黑描边后的编辑风格版，作为当前推荐成品。
- `170k-star-ai-workflow-3x4-v4-black-title.png`：1080×1440，全黑标题版；由画面中的金色 Star 独立承担重点色，作为当前推荐成品。
- `170k-star-ai-workflow-3x4-v5-imagegen-integrated.png`：1080×1440，Imagegen 一次生成场景与两行标题的完整封面，作为当前推荐成品。
- `ai-less-rework-4-steps-3x4-v6-imagegen-integrated.png`：1080×1440，改用收益导向标题“让AI少返工 / 4个步骤”的 Imagegen 一体化版本，作为当前推荐成品。
- `ai-less-rework-4-steps-3x4-v7-from-scratch.png`：1080×1440，不使用旧封面或无字底图作为编辑目标，Imagegen 从零一次生成标题与完整场景，作为当前推荐成品。
- `ai-less-rework-4-steps-4x3-v1-from-scratch.png`：1440×1080，Imagegen 针对 4:3 横版从零单独构图，作为配套横版成品。

## 底图

- `_bases/170k-star-ai-workflow-3x4-base.png`
- `_bases/170k-star-ai-workflow-3x4-base-v2.png`
- `_sources/170k-star-ai-workflow-imagegen-integrated-source.png`：Imagegen 一体化生成原图，仅做等比裁切/缩放后交付。
- `_sources/ai-less-rework-4-steps-imagegen-source.png`：收益导向标题版本的 Imagegen 一体化原图。
- `_sources/ai-less-rework-4-steps-from-scratch-source.png`：从零一次生成版本的原图。
- `_sources/ai-less-rework-4-steps-4x3-from-scratch-source.png`：4:3 从零一次生成版本的原图。

## V5 一体化标题

```text
17万Star
AI开发工作流
```

- 标题原则：最多两行，每行不超过 7 个汉字或等宽视觉字符。
- 生成方式：内置 Imagegen 在同一次生成中完成标题、场景、光影与空间关系；本地只裁切/缩放至 1080×1440，未叠加或修改文字。

## V2 最终提示词

```text
Use case: ads-marketing
Asset type: textless 3:4 vertical short-video cover base for Douyin and Xiaohongshu
Input image: established account style reference; inherit only its warm light editorial 3D language, tactile materials, soft product lighting, and restrained premium finish
Primary request: visualize an engineering-grade AI development workflow that first asks 25 clarifying questions, then turns them into a specification, splits it into executable tickets, and only then implements tested code; the GitHub project has 170K stars
Subject: one coherent four-stage modular workflow machine: question cards -> specification slab -> ticket cards -> code-and-test workstation, with a small AI engineer moving a module through the sequence and a champagne-gold star trophy as the popularity symbol
Composition: exact vertical 3:4; keep a completely clean central title band; place the workflow scene across the lower half and related symbols near the band edges
Style: sophisticated realistic 3D product still life, matte ceramic, ivory paper, light wood, frosted acrylic, restrained champagne metal
Constraints: no text, letters, numbers, logos, watermark, legible UI or unrelated props
Avoid: dark background, neon, cyberpunk, purple/blue gradients, busy dashboard UI, office people, glossy toy look, generic star-only concept
```
