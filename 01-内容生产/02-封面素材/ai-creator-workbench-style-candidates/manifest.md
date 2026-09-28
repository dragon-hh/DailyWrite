# 超级 AI 工作台：封面风格候选

- 来源脚本：`01-内容生产/01-脚本创作中/8.16 可以一键监控全网博主的超级AI工作台.md`
- 封面标题：`全网博主监控` / `超级AI工作台`
- 视觉锚点：多平台博主内容汇入中央工作台、AI 热点结构化、任务分配给本地 Agent、知识库与发布数据沉淀。
- 生成方式：内置 `imagegen`；每种风格分别从零生成一张完整 3:4 候选，场景与标题一次性共同构图。
- 当前状态：`awaiting_style_selection`。选定风格后，再为该风格从零生成 4:3 横版。
- 本地后处理：仅等比缩放到 1080×1440，未重排或重绘标题。

## 候选

- `light-editorial-3d`：`ai-creator-workbench-light-editorial-3x4-candidate.png`，1080×1440，验收通过。
- `neon-tech-3d`：`ai-creator-workbench-neon-tech-3x4-candidate.png`，1080×1440，验收通过。

## 生成记录

- `light-editorial-3d`：首轮通过。
- `neon-tech-3d`：首轮因内容卡和数据模块出现细小伪 UI 文字/刻度而拒绝；在向用户说明后重新完整生成，第二轮通过。拒绝稿未归档为候选。

## `light-editorial-3d` 最终提示词

```text
Use case: ads-marketing
Asset type: complete 3:4 vertical short-video cover candidate, exact final canvas target 1080x1440, with integrated Chinese typography
Style ID: light-editorial-3d
Primary request: Create a brand-new premium editorial cover for a video introducing a personal AI creator workbench. It monitors followed creators and AI-industry news across multiple platforms, turns the information into structured daily insights, routes tasks to local AI agents, and preserves published-video analytics and a growing content knowledge base. Visualize one coherent personal command center rather than a generic computer desk.
Scene/backdrop: bright warm ivory studio backdrop with subtle plaster and fine paper texture, spacious, low saturation
Subject: one elegant modular AI workbench in the middle-lower area. At its center is a refined vertical control console with a transparent intake funnel. Around the intake are multiple blank creator-content cards from different directions, each using only an abstract profile silhouette, play triangle, or image placeholder with no text or platform logo. The central console processes them into three clean physical modules: a daily-insight stack represented by layered report cards and a small trend curve; a task-routing rail that sends blank task tokens toward two restrained local-agent cubes; and a knowledge-and-performance archive represented by document drawers, a database stack, and an upward chart. The relationship should read instantly as gather -> structure -> dispatch -> accumulate.
Style/medium: premium editorial product still life, refined realistic 3D render, tactile matte ceramic, ivory paper, light wood, frosted acrylic, restrained champagne metal; inherit only the light editorial design language of the registered account reference, not its titles, brands, people, or exact objects
Composition/framing: portrait 3:4. Integrate the title as the central visual anchor at approximately 38% to 48% of image height. Keep the modular workbench and its three output modules across the lower half, with creator cards flowing in from the upper sides without crossing the title. Maintain at least 6% safe margin on every edge. Typography, objects, perspective, shadows, and negative space must feel designed together in one pass, not pasted afterward.
Lighting/mood: soft upper-left daylight, gentle realistic shadows, calm, capable, intelligent, premium
Color palette: warm ivory, beige, pale gray, deep charcoal details, one restrained champagne-gold accent
Text (verbatim with fixed line break): "全网博主监控\n超级AI工作台"
Typography: render exactly two centered lines. First line exactly "全网博主监控". Second line exactly "超级AI工作台". Modern simplified-Chinese sans-serif Bold or Black paired with compatible bold uppercase Latin letters; deep charcoal or near-black only; strong editorial hierarchy; extremely legible at thumbnail size.
Constraints: render the supplied title exactly once and exactly as written. The first line must contain exactly 全, 网, 博, 主, 监, 控. The second line must contain exactly 超, 级, uppercase A, uppercase I, 工, 作, 台. No misspelling, missing character, repeated character, garbled glyph, changed capitalization, or altered line break. No other text anywhere. No subtitle, English caption, platform name, numbers, labels, code, logo, signature, or watermark. Generate the full scene and typography together in one pass.
Avoid: dark background, neon glow, cyberpunk, blue-purple gradient, busy dashboard UI, photorealistic office people, clutter, glossy toy look, cheap advertising template, yellow headline, thick black outline, recognizable platform logos, unrelated props
```

## `neon-tech-3d` 最终提示词

```text
Use case: ads-marketing
Asset type: complete 3:4 vertical short-video cover candidate, exact final canvas target 1080x1440, with integrated Chinese typography
Style ID: neon-tech-3d
Primary request: Create a brand-new high-impact futuristic cover for a video introducing a personal AI creator workbench. It monitors followed creators and AI-industry news across multiple platforms, structures the information into daily insights, routes tasks to local AI agents, and preserves published-video analytics and a growing content knowledge base. Visualize one coherent monitoring-and-action system.
Scene/backdrop: deep black and midnight-blue futuristic control room with layered depth, subtle grid floor, dark server forms, luminous cyan circuitry, and a few restrained orange status lights. Do not place any interface screens, dashboards, code panels, text panels, labels, scales, axes, tick marks, or tiny horizontal strokes anywhere.
Subject: one central transparent monitoring-and-routing core. From the upper-left and upper-right, large physical creator tokens flow into the core through glowing cyan pipes. Each creator token is a simple luminous acrylic tile containing only one oversized solid circular head-and-shoulders pictogram or one oversized solid play triangle; no borders divided into UI sections, no lines, no micro-details. The core outputs into three purely physical modules: a daily-insight module made from a constellation of glowing nodes plus five rising solid bars and one large arrow, with no axes or labels; a task-dispatch rail sending blank solid task cubes toward two distinct crystalline local-agent cores; and a knowledge-and-performance vault made only from plain closed drawers, smooth database cylinders, and a large upward arrow. The relationship must instantly read as monitor -> digest -> dispatch -> accumulate.
Style/medium: polished cinematic 3D CGI tech illustration, glossy black glass, dark metal, luminous acrylic, crisp electric-blue rim lighting, premium Chinese short-video thumbnail; inherit only the dark neon data-system visual language of the registered reference, not its title, people, anime characters, robots, social cards, brands, or exact layout
Composition/framing: portrait 3:4. Place a large rounded black glass title panel across the center as the first visual focus, occupying about 28% of image height. Keep the monitoring core and incoming creator tokens above and behind the title. Arrange the three output modules below and around the title panel. Route all cyan cables around rather than across the letters. Maintain at least 6% safe margins and preserve strong thumbnail readability.
Lighting/mood: dark, technical, energetic, intelligent, high contrast; electric blue and cyan glow with tiny restrained orange accents
Color palette: black, midnight navy, electric blue, bright cyan, white, with very small orange status lights
Text (verbatim with fixed line break): "全网博主监控\n超级AI工作台"
Typography: render exactly two centered lines on the black panel. First line exactly "全网博主监控" in very large bold white modern simplified-Chinese sans-serif. Second line exactly "超级AI工作台" in very large bold bright electric-cyan modern simplified-Chinese sans-serif paired with compatible uppercase Latin letters. Strong square block typography, crisp, slightly dimensional, extremely legible at thumbnail size.
Constraints: render the supplied title exactly once and exactly as written. The first line must contain exactly 全, 网, 博, 主, 监, 控. The second line must contain exactly 超, 级, uppercase A, uppercase I, 工, 作, 台. No misspelling, missing character, repeated character, garbled glyph, changed capitalization, or altered line break. The supplied title is the only textual content permitted in the entire image. Outside the title panel there must be zero letters, zero numbers, zero punctuation, zero code, zero fake UI copy, zero tiny horizontal strokes arranged like writing, zero axes, zero tick marks, and zero labels. No subtitle, English caption, platform names, logo, signature, or watermark. Generate the complete scene and typography together in one pass.
Avoid: any interface screen or dashboard, any card with divided UI regions, any chart axis or scale, any monitor or panel with code-like marks, fake UI text, microcopy, labels, random glyphs, platform logos, recognizable social-media interfaces, warm ivory studio, beige editorial still life, daylight product photography, pasted-on typography, anime characters, humans, humanoid robots, social-media feeds copied from the reference, cheap gaming poster, purple-pink cyberpunk, unreadable dashboard clutter
```
