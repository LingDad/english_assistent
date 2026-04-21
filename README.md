# English Assistant

一个带复古打字机界面的单页英文助手。

用户可以直接在页面中输入中文或英文，然后调用大模型完成以下任务：

- 中文转自然、美式英语表达
- 英文句子自然度判断
- 英文表达润色与改写建议

整个项目目前是一个纯前端静态页面，核心代码集中在 `index.html` 中，不依赖构建工具，打开即可运行。

## 功能特性

- 打字机风格 UI，输入内容会逐字渲染到“纸张”上
- Web Audio 模拟打字与退格音效
- 支持点击 `Analyze` 调用模型分析文本
- 自动判断输入是中文还是英文
- 中文输入：翻译为自然、地道的美式英语
- 英文输入：
  - 如果表达自然，给出简短鼓励
  - 如果表达不够自然，返回更合适的美式英语版本并解释修改原因
- 分析结果带有逐字打字展示效果
- 支持一键复制优化后的文本
- API Key、Endpoint、Model 保存在浏览器 `localStorage`

## 技术栈

- HTML
- CSS
- 原生 JavaScript
- Web Audio API
- Fetch API
- DeepSeek Chat Completions 兼容接口

## 项目结构

```text
.
├── index.html   # 页面、样式、交互逻辑全部集中在这里
└── README.md
```

## 快速开始

### 1. 克隆项目

```bash
git clone git@github.com:LingDad/english_assistent.git
cd english_assistent
```

### 2. 启动方式

这是一个静态页面项目，有两种常见使用方式：

直接打开文件：

```bash
open index.html
```

或启动一个本地静态服务：

```bash
python3 -m http.server 8000
```

然后访问：

[http://localhost:8000](http://localhost:8000)

## 使用说明

### 1. 配置模型接口

点击页面右上角的齿轮按钮，填写以下信息：

- `API Key`
- `API Endpoint`
- `Model`

当前默认值是：

- Endpoint: `https://api.deepseek.com/chat/completions`
- Model: `deepseek-chat`

配置会保存在当前浏览器的 `localStorage` 中，不会写入仓库。

### 2. 输入文本

点击打字机区域后直接输入内容：

- 输入中文：会翻译成自然的美式英语
- 输入英文：会判断是否自然，并给出润色建议

### 3. 触发分析

你可以通过以下任一方式触发分析：

- 点击 `Analyze`
- 按回车键（`Enter`）

### 4. 清空内容

点击 `Clear` 可清空当前输入和分析结果。

## 分析逻辑

页面会向配置好的接口发送一个请求，并要求模型严格返回 JSON。返回结果包含：

- `input_lang`
- `verdict`
- `improved`
- `explanation`

其中：

- `translation` 表示输入为中文，返回翻译结果
- `natural` 表示英文表达已经比较自然
- `needs_improvement` 表示英文表达可进一步优化

## 本地存储

以下配置会存储在浏览器本地：

- `kimiApiKey`
- `kimiEndpoint`
- `kimiModel`

项目中还包含一段迁移逻辑，用于清理旧版本保存的不兼容 endpoint 或 model 配置。

## 注意事项

- 这是一个前端直连模型接口的项目，`API Key` 会暴露在浏览器请求中，更适合个人使用或原型验证
- 如果后续需要公开部署，建议增加后端代理层来保护密钥
- 项目当前没有测试框架，也没有打包流程
- 当前全部实现都在 `index.html` 中，后续如果功能继续增长，建议拆分为 `style`、`script` 和组件化结构

## 后续可优化方向

- 拆分 HTML / CSS / JS，提升可维护性
- 增加多段文本、换行和历史记录支持
- 增加加载状态与错误提示的细化处理
- 支持更多模型提供商的预设配置
- 增加移动端交互细节优化

## License

当前仓库未声明 License。如需开源分发，建议补充明确的许可证文件。
