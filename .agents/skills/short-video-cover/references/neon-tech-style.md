# 深色霓虹科技 3D 封面风格

`style_id`: `neon-tech-3d`

## 风格基准

参考图：`../assets/neon-tech-reference.png`。

只继承参考图的视觉语言：深黑科技空间、蓝青霓虹边缘、发光数据管线、立体模块、中央黑色标题牌和高对比大字。不要复制参考图中的标题、动漫人物、机器人、社交卡片、品牌或具体布局。

## 视觉系统

- 背景：黑色、午夜蓝或深蓝黑控制室，允许服务器、网格地面、远景数据面板和少量橙色状态灯。
- 标题牌：中央或中央偏左的大型黑色玻璃/金属面板，圆角、蓝色发光边框，与场景透视和管线自然融合。
- 标题：默认两行。第一行白色，第二行电光青色；使用现代中文黑体 Bold/Black 和兼容的粗窄体英文，无粗重描边。
- 主体：一个清晰的科技系统隐喻，例如核心舱、数据管线、芯片、模块阵列或调度台。
- 材质：黑色玻璃、深色金属、透明发光亚克力、蓝青能量管线。
- 光线：高对比蓝青边缘光、体积光和克制的橙色状态点；标题必须始终保持最高可读性。
- 密度：允许比浅色编辑风更丰富，但必须有明确层级，不能退化成杂乱仪表盘。

## 内容取材与转译

从原文选择 3 至 4 个锚点，组织成一个系统关系：

- Agent / Harness：中央核心舱、插件端口、循环节点。
- 工作流 / 自动化：输入卡片、发光管线、处理核心、输出模块。
- 数据增长：上升曲线、柱状图、里程碑星标；没有来源的数据不得写成数字。
- 工具 / 权限 / 记忆 / 沙箱：扳手、盾牌、数据库、立方体等无文字图标模块。
- 多模型或多角色：使用抽象芯片或模块，不默认复制参考图中的人物或机器人。

## 3:4 构图

- 成品尺寸 1080×1440。
- 标题牌位于画面中央区域，占画面高度约 24% 至 34%。
- 主核心位于标题牌后方、上方或下方，管线绕过标题，不能穿过字面。
- 相关模块分布在画面上部和下部，四周保留至少 6% 安全边距。

## 4:3 构图

- 成品尺寸 1440×1080，必须从零单独构图。
- 标题牌优先放在左侧或中央偏左，主核心放在右侧，形成清晰的横向数据流。
- 增长图、输出模块或辅助节点放在远景或下半部，不与标题争夺视觉中心。
- 四周保留至少 6% 安全边距。

## Imagegen 提示词骨架

```text
Use case: ads-marketing
Asset type: final <3:4 vertical | 4:3 horizontal> short-video cover with integrated typography
Primary request: visualize <topic> as one coherent futuristic data system; encode the source's 3 to 4 strongest anchors without copying the style reference's people, title, cards, brands, or exact layout
Scene/backdrop: deep black and midnight-blue futuristic control space with layered depth, subtle grid floor, cyan circuitry, and restrained orange status lights
Subject: <one central core or processing system> connected to <3 to 4 relevant modules> by luminous cyan pipelines
Style/medium: polished cinematic 3D CGI tech illustration, glossy black glass, dark metal, luminous acrylic, crisp neon rim lighting, premium Chinese short-video thumbnail
Composition/framing: integrate a large black title panel into the 3D scene; keep the title unobstructed; route cables around rather than across the letters; preserve 6% safe margins
Lighting/mood: dark, technical, high-energy, high contrast, electric blue and cyan glow
Color palette: black, midnight navy, electric blue, bright cyan, white, tiny restrained orange accents
Text (verbatim with fixed line break): "<第一行>\n<第二行>"
Typography: exact simplified Chinese and Latin text; first line white, second line electric cyan; modern sans-serif Bold/Black; extremely legible at thumbnail size
Constraints: render the title exactly once and exactly as supplied; no misspelling, missing character, repeated character, garbled glyph, extra caption, fake UI text, logo, signature, or watermark
Avoid: warm ivory studio, beige editorial still life, daylight product photography, anime characters, humanoid robots unless required by the topic, social-media feeds, purple-pink cyberpunk, unreadable dashboard clutter
```

## 验收

- 标题逐字准确，只出现一次；第一行白色、第二行青色，缩略图尺寸仍可读。
- 主核心、数据管线和模块关系一眼可辨，标题是第一视觉焦点。
- 没有复制参考图中的人物、旧标题、社交卡片或具体 UI。
- 没有无来源数字、无关小字、Logo、签名或水印。
- 3:4 与 4:3 像同一系列，但构图必须分别成立。
