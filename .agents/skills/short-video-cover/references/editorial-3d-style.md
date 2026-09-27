# 浅色编辑 3D 封面风格

`style_id`: `light-editorial-3d`

## 风格基准

参考图：`../assets/editorial-3d-grid-reference.png`。

只继承参考图的浅色 3D 视觉语法：浅色背景、真实柔光、克制材质与编辑排版气质。不复制任何参考图中的标题、品牌、构图细节或具体物件。

## 视觉系统

- 背景：暖白、象牙白、浅米灰，允许轻微纸张、石膏或细砂纹理；整体明亮、低饱和。
- 标题：默认水平居中、位于画面中央区域，最多两行，每行不超过 7 个汉字或等宽视觉字符。使用现代中文黑体 Bold 或 Black 字重，全部使用深炭灰或近黑色，不通过文字颜色强调关键词。
- 标题字形：保持端正、紧凑和编辑感；允许轻微字重或字号对比，不使用夸张斜体、卡通膨胀字、亮黄色或粗黑描边。
- 副标题：默认不加英文副标题。只有用户明确要求或信息确有必要时，才添加一行很小的无衬线副标题。
- 主体：围绕主题建立一个主要 3D 场景；如果有原始文档，允许加入 3 至 4 个紧密相关的叙事物件，但必须共同解释同一流程。
- 材质：哑光塑料、陶瓷、纸张、浅木、磨砂金属、布面等真实可触摸材质。
- 光线：柔和的左上侧自然光或棚拍光，保留清晰但不过硬的投影，营造安静的高级产品摄影感。
- 配色：以暖白、浅灰、米色为底；画面物件每期最多加入一种主题点缀色。标题固定使用深炭灰或近黑色，必要时增加暖白细描边。

## 内容取材

- 有原始脚本、文章或项目文档时，必须先读全文，禁止只依据标题补画面。
- 优先提炼四类信息：核心冲突、关键数字、流程节点、最终结果。
- 视觉锚点控制在 3 至 4 个，并组织成一眼能理解的关系，例如流程、对比、前后变化或因果链。
- 标题负责给结论，画面负责补充正文细节；不要让标题和画面重复表达同一个抽象词。

## 选题转译

把抽象工具能力转成一个可视化物件隐喻：

- 效率提升：数字牌、日历、键盘、进度模块。
- AI 助手或 Agent：克制的小型机器人、棋子、模块化人物模型。
- 工作流与调度：中央芯片、节点、导线、层叠模块。
- 聊天分析：对话框、关系节点、平板或档案卡。
- 视频与笔记：打开的笔记本、分镜纸、场记板、时间线积木。
- 代码与命令：机械键盘、命令卡片、字母积木、终端形状模块。

机器人不是账号固定吉祥物。只有选题涉及 AI 助手、Agent、桌宠或拟人化能力时才使用；其他选题优先选择更直接的工具物件。

## 3:4 构图

- 中文标题中心点位于画面高度约 38% 至 50%，标题整体占画面高度约 18% 至 28%。
- 3D 主场景放在中下部，相关叙事物件可向两侧环绕，但不得穿过标题字面。
- 四周保留至少 6% 安全边距。

## 4:3 构图

- 成品尺寸为 1440×1080。
- 中文标题仍然居中，优先放在画面上半部或中央偏上；最多两行，每行不超过 7 个汉字或等宽视觉字符。
- 四阶段流程适合横向展开在画面下半部，主体之间保持清晰顺序和连接关系。
- 四周保留至少 6% 安全边距，避免标题和关键物体贴近左右边缘。
- 4:3 必须单独由 imagegen 构图，不能由 3:4 裁切、扩图或本地搬运元素得到。

## Imagegen 提示词骨架

```text
Use case: ads-marketing
Asset type: final 3:4 vertical short-video cover with integrated Chinese typography
Input images: Image 1 is the account style reference only; inherit its editorial design language, warm neutral palette, lighting, materials, and restraint, but do not treat it as an edit target or preserve its exact scene
Primary request: visualize <topic> through one immediately recognizable 3D scene; when source material exists, encode its 3 to 4 strongest content anchors into one coherent relationship
Scene/backdrop: bright warm ivory studio backdrop with subtle paper or plaster texture
Subject: <single hero object or one tightly related narrative object group>
Style/medium: premium editorial product still life, refined realistic 3D render, tactile matte materials
Composition/framing: integrate the title into the scene as the central visual anchor; organize the hero scene in the middle-lower area and related narrative objects around the title with 3:4 safe margins; typography and objects must feel designed together, not overlaid afterward
Lighting/mood: soft upper-left daylight, gentle realistic shadow, calm and intelligent
Color palette: warm ivory, beige, light gray, black details, one restrained topic accent color
Text (verbatim with fixed line break): "<第一行>\n<第二行>"
Typography: exact simplified Chinese; centered in exactly the supplied one or two lines; maximum 7 visual characters per line; modern Chinese sans-serif Bold or Black; deep charcoal or near-black only; editorial, restrained, highly legible at thumbnail size
Constraints: render the title exactly once and exactly as supplied; no misspelling, missing character, repeated character, garbled glyph, extra caption, English subtitle, logo, signature, or watermark; preserve safe margins
Avoid: dark background, neon glow, cyberpunk, purple gradient, busy dashboard UI, photorealistic office people, clutter, glossy toy look, cheap advertising template
```

## 排版与验收

- 中文标题必须逐字准确，最多两行，每行不超过 7 个汉字或等宽视觉字符。
- 深炭灰标题必须保持足够对比；如背景明暗不均，只加 1 至 3 像素暖白描边或轻柔投影。
- 标题必须与物体构图、空间关系和光影自然融合，不能像后期贴在空白底图上的独立文字层。
- 缩小到手机主页网格尺寸后，中文标题仍应可读，核心 3D 物件仍应可辨。
- 拒绝任何文字截断、主体遮挡标题、粗重描边、重点词不突出或比例错误的结果。
