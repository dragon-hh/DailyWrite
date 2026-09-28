# 让 AI 少返工的 4 个步骤：封面风格候选

- `content_id`：`DW-20260715-AI-DEV-SKILL-WORKFLOW-01`
- 来源脚本：`01-内容生产/01-脚本创作中/7.15 硅谷顶级工程师的最新AI开发工作流 -claude-v2.md`
- 封面标题：`让AI少返工` / `4个步骤`
- 视觉锚点：追问澄清、Spec 规范、可独立验证的 Tickets、Implement 与测试审查、Star 社会证明。
- 生成方式：内置 `imagegen`；每种风格分别从零生成一张完整 3:4 候选，场景与标题一次性共同构图。
- 用户选择：`neon-tech-3d`（选项 2）。
- 当前状态：`complete`。已确认 3:4 竖版，并从零单独生成 4:3 横版。
- 本地后处理：仅等比缩放到 1080×1440，未重排或重绘标题。

## 最终成品

- `ai-less-rework-4-steps-neon-tech-3x4.png`：1080×1440，抖音 / 小红书。
- `ai-less-rework-4-steps-neon-tech-4x3.png`：1440×1080，B 站等横版场景。

## 候选

- `light-editorial-3d`：`ai-less-rework-4-steps-light-editorial-3x4-candidate.png`，1080×1440，验收通过。
- `neon-tech-3d`：`ai-less-rework-4-steps-neon-tech-3x4-candidate.png`，1080×1440，验收通过。

## 生成记录

- `light-editorial-3d`：首轮通过。
- `neon-tech-3d`：首轮因实现模块出现细小伪代码文字而拒绝；在向用户说明后重新完整生成，第二轮通过。拒绝稿未归档为候选。
- `neon-tech-3d` 4:3：从零单独构图，首轮通过；未使用 3:4 裁切、扩图或编辑换字。

## `light-editorial-3d` 最终提示词

```text
Use case: ads-marketing
Asset type: complete 3:4 vertical short-video cover candidate, exact final canvas target 1080x1440, with integrated Chinese typography
Style ID: light-editorial-3d
Primary request: Create a brand-new premium editorial cover for a video explaining Matt Pocock's four-step engineering-grade AI development workflow. The benefit is reducing AI rework by clarifying requirements before coding. Encode the four source-backed stages into one coherent visual path: clarifying questions, an acceptance-ready specification, independently testable vertical-slice tickets, and implementation with tests/review. A restrained star trophy may suggest the project's 170,000 GitHub stars, but it must contain no text or numbers.
Scene/backdrop: bright warm ivory studio backdrop with subtle plaster and fine paper texture, spacious, low saturation
Subject: one elegant four-stage modular workflow machine in the middle-lower area. Stage one is a cluster of blank conversation cards and decision tokens; stage two is a clean specification document slab with abstract checklist marks but no readable text; stage three is a set of separate ticket blocks arranged as small complete vertical slices; stage four is a compact code-and-test workstation represented by a keyboard-like module, a checkmark light, and a small review lens. One small restrained AI engineer figure moves a module through the sequence. Add one champagne-metal star trophy as a popularity symbol.
Style/medium: premium editorial product still life, refined realistic 3D render, tactile matte ceramic, ivory paper, light wood, frosted acrylic, restrained champagne metal; inherit only the light editorial design language of the registered account reference, not its titles, brands, people, or exact objects
Composition/framing: portrait 3:4. Integrate the title as the central visual anchor at approximately 40% to 48% of image height. Keep the four-stage workflow in the lower half, with a subtle ascending sequence from left to right and small related pieces around the title without crossing it. Maintain at least 6% safe margin on every edge. Typography, objects, perspective, shadows, and negative space must feel designed together in one pass, not pasted afterward.
Lighting/mood: soft upper-left daylight, gentle realistic shadows, calm, intelligent, trustworthy
Color palette: warm ivory, beige, pale gray, deep charcoal details, one restrained champagne-gold accent
Text (verbatim with fixed line break): "让AI少返工\n4个步骤"
Typography: render exactly two centered lines. First line exactly the simplified Chinese and Latin text "让AI少返工". Second line exactly "4个步骤". Modern Chinese sans-serif Bold or Black paired with compatible bold Latin letters and digit; deep charcoal or near-black only; strong editorial hierarchy; extremely legible at thumbnail size.
Constraints: render the supplied title exactly once and exactly as written. The first line must contain exactly 让, uppercase A, uppercase I, 少, 返, 工. The second line must contain exactly digit 4, 个, 步, 骤. No misspelling, missing character, repeated character, garbled glyph, changed capitalization, or altered line break. No other text anywhere. No subtitle, English caption, numbers, labels, code, logo, signature, or watermark. Generate the full scene and typography together in one pass.
Avoid: dark background, neon glow, cyberpunk, blue-purple gradient, busy dashboard UI, photorealistic office people, clutter, glossy toy look, cheap advertising template, yellow headline, thick black outline, unrelated props
```

## `neon-tech-3d` 最终提示词

```text
Use case: ads-marketing
Asset type: complete 3:4 vertical short-video cover candidate, exact final canvas target 1080x1440, with integrated Chinese typography
Style ID: neon-tech-3d
Primary request: Create a brand-new high-impact futuristic cover for a video explaining Matt Pocock's four-step engineering-grade AI development workflow. The benefit is reducing AI rework by clarifying requirements before coding. Encode the four source-backed stages into one coherent neon data pipeline: clarifying questions, an acceptance-ready specification, independently testable vertical-slice tickets, and implementation with tests/review. A rising star milestone may suggest the project's 170,000 GitHub stars, but it must contain no text or numbers.
Scene/backdrop: deep black and midnight-blue futuristic development control room with layered depth, subtle grid floor, dark server forms in the distance, luminous cyan circuitry, a few restrained orange status lights. All background panels must be completely blank and contain no glyphs, lines resembling text, numbers, code, labels, or interface copy.
Subject: one central transparent workflow core connected by glowing cyan pipes to four large stage modules. The modules use only large universal pictograms and physical metaphors: a cluster of blank dialog-card shapes for questions; a blank specification slab with four oversized checkmark icons only; a grid of separate cube-like ticket blocks for vertical slices; and a pure hardware implementation-and-test module built from a luminous microchip, one oversized checkmark lamp, and a review magnifying lens. The implementation module must not include a laptop, monitor, terminal, code window, keyboard screen, or any small marks resembling text. Make the data visibly flow through the four stages. Add one compact rising-star graph made only from bars, a line, dots, and a star in the far background, with no labels or numbers.
Style/medium: polished cinematic 3D CGI tech illustration, glossy black glass, dark metal, luminous acrylic, crisp electric-blue rim lighting, premium Chinese short-video thumbnail; inherit only the dark neon data-system visual language of the registered reference, not its title, people, anime characters, robots, social cards, or exact layout
Composition/framing: portrait 3:4. Place a large rounded black glass title panel across the center as the first visual focus, occupying about 28% of image height. Keep the four-stage pipeline and transparent processing core behind, above, and below the title panel. Route all cyan cables around rather than across the lettering. Place two stage modules in the upper area and two in the lower area, with clear directional flow and at least 6% safe margins.
Lighting/mood: dark, technical, energetic, high contrast, intelligent; electric blue and cyan glow with tiny restrained orange accents
Color palette: black, midnight navy, electric blue, bright cyan, white, with very small orange status lights
Text (verbatim with fixed line break): "让AI少返工\n4个步骤"
Typography: render exactly two centered lines on the black panel. First line exactly "让AI少返工" in very large bold white modern sans-serif. Second line exactly "4个步骤" in very large bold bright electric-cyan modern Chinese sans-serif. Strong square block typography, crisp, slightly dimensional, extremely legible at thumbnail size.
Constraints: render the supplied title exactly once and exactly as written. The first line must contain exactly 让, uppercase A, uppercase I, 少, 返, 工. The second line must contain exactly digit 4, 个, 步, 骤. No misspelling, missing character, repeated character, garbled glyph, changed capitalization, or altered line break. The supplied title is the only textual content permitted in the entire image. Outside the title panel there must be zero letters, zero numbers, zero punctuation, zero code, zero fake UI copy, zero tiny horizontal strokes arranged like writing, and zero labels. No subtitle, English caption, logo, signature, or watermark. Generate the complete scene and typography together in one pass.
Avoid: any monitor or panel with code-like marks, fake UI text, microcopy, labels, random glyphs, warm ivory studio, beige editorial still life, daylight product photography, pasted-on typography, anime characters, humans, humanoid robots, social-media feeds, video cards, hearts, speech bubbles, cheap gaming poster, purple-pink cyberpunk, unreadable dashboard clutter
```

## `neon-tech-3d` 4:3 最终提示词

```text
Use case: ads-marketing
Asset type: final 4:3 horizontal short-video cover, exact canvas target 1440x1080, with integrated Chinese typography
Style ID: neon-tech-3d
Primary request: Create a brand-new horizontal companion cover for the selected neon-tech-3d series about Matt Pocock's four-step engineering-grade AI development workflow. The benefit is reducing AI rework by clarifying requirements before coding. Encode the four source-backed stages into one coherent neon data pipeline: clarifying questions, an acceptance-ready specification, independently testable vertical-slice tickets, and implementation with tests/review. Compose specifically for 4:3; do not crop, extend, edit, or recreate the vertical image pixel-for-pixel.
Series continuity: match the selected vertical cover's black and midnight-blue control room, electric-blue/cyan pipeline system, glossy black title panel, transparent processing core, large blank dialog cards, four-checkmark specification slab, ticket cubes, microchip, checkmark lamp, review magnifying lens, and rising star graph. Preserve the same visual metaphor and materials while creating a true horizontal composition.
Scene/backdrop: deep black and midnight-blue futuristic development control room with layered depth, subtle grid floor, dark server forms, luminous cyan circuitry, and a few restrained orange status lights. All background panels must be blank and contain no glyphs, lines resembling text, numbers, code, labels, or interface copy.
Subject: one transparent cyan workflow core on the right-middle, connected by glowing pipes to four large stage modules arranged as a clear left-to-right sequence across the lower third: blank dialog-card shapes, a blank slab with four oversized checkmark icons, a grid of separate cube-like ticket blocks, and a pure hardware implementation-and-test module built from a luminous microchip, one oversized checkmark lamp, and a review magnifying lens. The implementation module must not include a laptop, monitor, terminal, code window, keyboard screen, or any marks resembling text. Add one compact rising-star graph in the upper-right background using only bars, a line, dots, and a star, with no labels or numbers.
Style/medium: polished cinematic 3D CGI tech illustration, glossy black glass, dark metal, luminous acrylic, crisp electric-blue rim lighting, premium Chinese short-video thumbnail; inherit only the selected series' visual language, not any reference title, people, anime characters, robots, social cards, brands, or exact layout
Composition/framing: horizontal 4:3. Place a large wide rounded black glass title panel on the left half as the first visual focus. Position the transparent processing core to the right-middle. Run the four-stage workflow across the bottom and around the core with a clear directional flow. Route cyan cables around rather than across the title. Keep the rising star graph in the upper-right far background. Maintain at least 6% safe margins on every edge. The title and core must remain legible at thumbnail size.
Lighting/mood: dark, technical, energetic, high contrast, intelligent; electric blue and cyan glow with tiny restrained orange accents
Color palette: black, midnight navy, electric blue, bright cyan, white, with very small orange status lights
Text (verbatim with fixed line break): "让AI少返工\n4个步骤"
Typography: render exactly two centered lines on the black title panel. First line exactly "让AI少返工" in very large bold white modern sans-serif. Second line exactly "4个步骤" in very large bold bright electric-cyan modern Chinese sans-serif. Strong square block typography, crisp, slightly dimensional, extremely legible at thumbnail size.
Constraints: render the supplied title exactly once and exactly as written. The first line must contain exactly 让, uppercase A, uppercase I, 少, 返, 工. The second line must contain exactly digit 4, 个, 步, 骤. No misspelling, missing character, repeated character, garbled glyph, changed capitalization, or altered line break. The supplied title is the only textual content permitted in the entire image. Outside the title panel there must be zero letters, zero numbers, zero punctuation, zero code, zero fake UI copy, zero tiny horizontal strokes arranged like writing, and zero labels. No subtitle, English caption, logo, signature, or watermark. Generate the complete scene and typography together in one pass.
Avoid: portrait composition, cropping or extending the vertical cover, any monitor or panel with code-like marks, fake UI text, microcopy, labels, random glyphs, warm ivory studio, beige editorial still life, daylight product photography, pasted-on typography, anime characters, humans, humanoid robots, social-media feeds, video cards, hearts, speech bubbles, cheap gaming poster, purple-pink cyberpunk, unreadable dashboard clutter
```
