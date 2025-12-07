# Code Coral 🪸

AI 驱动的代码生成与调试工具，使用 Ollama 本地大语言模型。

## 📋 功能特性

- ✨ **AI 代码生成** - 使用本地 Ollama 模型根据自然语言描述生成 Python 代码
- 🔄 **迭代优化** - 支持基于用户建议持续改进生成的代码
- 🐛 **错误修复** - 自动根据异常信息修复代码
- 💻 **实时执行** - 立即运行生成的代码并查看结果

## 🚀 快速开始

### 前置要求

- Python 3.8+
- [Ollama](https://ollama.ai/) 已安装并运行
- `codegemma` 模型已下载（或其他兼容的代码生成模型）

### 安装

1. 克隆仓库
```bash
git clone https://github.com/riscorn-zhang/code-coral.git
cd code-coral
```

2. 创建虚拟环境
```bash
python -m venv env
# Windows
env\Scripts\activate
# Linux/Mac
source env/bin/activate
```

3. 安装依赖
```bash
pip install -r requirements.txt
```

### 使用

```bash
python main.py
```

按照提示输入代码需求，工具会：
1. 生成初始代码
2. 执行代码
3. 接收你的反馈或建议
4. 重复迭代直到满意

## 📁 项目结构

```
code-coral/
├── main.py                 # 主程序入口
├── code_response.py        # AI 代码生成模块
├── debug_response.py       # 代码执行与调试模块
├── globals.py              # 全局配置
├── config_loader.py        # 配置加载器
├── load_prompt.py          # 提示词加载
├── config/                 # 配置文件目录
│   ├── general.yaml        # 通用配置
│   └── description.md      # 项目描述
├── prompts/                # 提示词模板
│   ├── default_prompt.md   # 默认提示
│   ├── python_simple.md    # Python 简单模板
│   ├── suggestion_addition.md
│   ├── exception_addition.md
│   └── debugger.md
└── syntax/                 # 语法处理模块
    └── directory_operations.py
```

## 🔧 配置

在 `config/general.yaml` 中配置：
- Ollama 模型选择
- 临时文件存储位置
- 其他运行时参数

## 📝 开发规范

### 代码风格
- 遵循 [PEP 8](https://www.python.org/dev/peps/pep-0008/) 标准
- 使用 4 个空格缩进
- 最大行长 120 字符
- 使用 type hints（类型注解）

### 文档
- 所有模块、类和公共函数必须包含 docstrings
- 使用 Google 风格的 docstrings
- 保持代码注释简洁明了

### 质量保证
- 使用 `pylint` 进行代码检查
- 使用 `black` 格式化代码
- 使用 `isort` 组织导入

```bash
# 代码检查
pylint *.py

# 代码格式化
black .
isort .
```

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

MIT License

## 📧 联系方式

- GitHub: [@riscorn-zhang](https://github.com/riscorn-zhang)

---

**Successful features:**
- ✅ 使用 Ollama API 创建 Python 项目
- ✅ 运行生成的代码
- ✅ 根据用户建议修复代码
