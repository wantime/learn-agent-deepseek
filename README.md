# Learn Agent DeepSeek

一个基于 DeepSeek 大语言模型的轻量级 Agent 框架，专为学习和研究智能体（Agent）相关技术而设计。通过模块化组件和简洁的接口，帮助你快速实现并实验各种 Agent 范式，如 ReAct、Plan-and-Execute、多智能体协作等。

## 📖 简介
Agent DeepSeek 旨在为研究人员和爱好者提供一个灵活、可扩展的实验平台，以探索基于大语言模型的智能体行为。框架核心围绕以下几个设计原则：

简单易用：用最少的代码启动一个能调用工具、进行推理的 Agent。

模块化：Agent、工具、记忆、规划器等组件均可自由组合与替换。

可研究性：内置日志、中间结果暴露等机制，方便分析 Agent 的思考过程，并支持快速对接学术论文中的方法。

DeepSeek 优先：原生支持 DeepSeek API，同时预留接口可扩展到其他 LLM。

## ✨ 特性
多种 Agent 类型：提供 ReAct、Plan-and-Execute、Tool-using 等经典 Agent 实现。

工具调用：内置bash执行、任务规划等工具，并支持自定义工具。

记忆管理：支持短期对话记忆、上下文压缩和长期记忆。

结构化输出：Agent 可以生成 JSON、代码等结构化数据，便于下游任务使用。

可观测性：每一步的推理、工具调用、记忆更新均可记录，便于调试和研究。

易扩展：可轻松添加新的 Agent 类型、工具、记忆后端或 LLM 提供商。

## 🚀 快速开始
安装
bash
git clone https://github.com/yourname/deepseek-agent-framework.git
cd deepseek-agent-framework
pip install -r requirements.txt
配置 API 密钥
在项目根目录创建 .env 文件，或直接设置环境变量：

text
DEEPSEEK_API_KEY=your_deepseek_api_key_here
DEEPSEEK_BASE_URL=https://api.deepseek.com  # 可选，默认为官方地址

运行第一个 Agent
$ python agent-loop.py

更多示例请查看 examples/ 目录。

## 📁 项目结构
text
deepseek-agent-framework/
├── deepseek_agent/          # 核心代码
│   ├── agent/               # Agent 实现（ReAct, PlanExecute, ...）
│   ├── llm/                 # LLM 封装（DeepSeek 客户端）
│   ├── memory/              # 记忆模块
│   ├── tools/               # 内置工具
│   └── utils/                # 日志、解析器等工具
├── examples/                 # 示例脚本
├── tests/                    # 单元测试
├── docs/                     # 文档
├── requirements.txt          # 依赖
└── README.md                 # 本文件

## 📚 研究指南
此框架特别适合复现和对比 Agent 领域的经典工作，或快速验证新想法。

我们鼓励你基于此框架进行实验，并欢迎贡献新的 Agent 范式或工具。

## 🤝 贡献
欢迎任何形式的贡献！无论是报告 bug、提出新特性、完善文档，还是提交代码。请先阅读 CONTRIBUTING.md 了解开发流程。

## 📄 许可证
本项目采用 MIT 许可证，详情见 LICENSE 文件。

## 🙏 致谢

感谢 DeepSeek 提供强大的 API 服务。

感谢 [ShareAI-lab](https://github.com/shareAI-lab)开源的Claude Code版Agent。
 
灵感来自 [Learn-Claude-Code](https://github.com/shareAI-lab/learn-claude-code)、LangChain、AutoGPT 等优秀开源项目。

Happy Researching! 🧪🤖
