# 📖 项目规范化文档索引

本文档是规范化工作的总导航，帮助您快速找到需要的信息。

## 🎯 快速链接

### 👤 初次使用者
1. **[README_NEW.md](./README_NEW.md)** - 项目概览和快速开始
2. **[STYLE_GUIDE.md](./STYLE_GUIDE.md)** - 代码规范速查表
3. **[运行规范化](#快速命令)**

### 👨‍💻 开发者
1. **[CONTRIBUTING.md](./CONTRIBUTING.md)** - 完整的贡献指南
2. **[STYLE_GUIDE.md](./STYLE_GUIDE.md)** - 代码规范详解
3. **[CHANGELOG.md](./CHANGELOG.md)** - 版本历史

### 📋 项目管理员
1. **[STANDARDIZATION_REPORT.md](./STANDARDIZATION_REPORT.md)** - 规范化完成报告
2. **[CHANGELOG.md](./CHANGELOG.md)** - 更新日志
3. **[pyproject.toml](./pyproject.toml)** - 项目配置

---

## 📁 规范化文件清单

### 📄 文档文件

| 文件 | 用途 | 优先级 |
|------|------|--------|
| `README_NEW.md` | 项目说明 | ⭐⭐⭐ |
| `CONTRIBUTING.md` | 贡献指南 | ⭐⭐⭐ |
| `STYLE_GUIDE.md` | 代码规范速查 | ⭐⭐⭐ |
| `CHANGELOG.md` | 版本更新日志 | ⭐⭐ |
| `STANDARDIZATION_REPORT.md` | 规范化报告 | ⭐⭐ |

### ⚙️ 配置文件

| 文件 | 用途 | 说明 |
|------|------|------|
| `pyproject.toml` | 项目配置 | black/isort/pylint 配置 |
| `.editorconfig` | 编辑器配置 | 缩进、换行符等 |
| `.pylintrc` | Pylint 配置 | 代码检查规则 |
| `.vscode/settings.json` | VS Code 设置 | 编辑器和格式化 |
| `.vscode/tasks.json` | VS Code 任务 | 检查、格式化任务 |
| `.gitignore` | Git 忽略规则 | Python 项目规范 |

### 📦 依赖文件

| 文件 | 用途 | 安装命令 |
|------|------|--------|
| `requirements.txt` | 项目依赖 | `pip install -r requirements.txt` |
| `requirements-dev.txt` | 开发工具 | `pip install -r requirements-dev.txt` |

### 🛠️ 脚本文件

| 文件 | 用途 | 平台 |
|------|------|------|
| `normalize.bat` | 一键规范化 | Windows |
| `normalize.sh` | 一键规范化 | Linux/Mac |

---

## 🚀 快速命令

### 第一次设置开发环境

```bash
# 1. 创建虚拟环境
python -m venv env

# 2. 激活虚拟环境
# Windows
env\Scripts\activate
# Linux/Mac
source env/bin/activate

# 3. 安装依赖
pip install -r requirements.txt
pip install -r requirements-dev.txt

# 4. 配置 VS Code（自动读取 .vscode/settings.json）
```

### 提交前规范化

```bash
# 一键执行（Windows）
normalize.bat

# 一键执行（Linux/Mac）
bash normalize.sh

# 或手动执行
black .           # 代码格式化
isort .           # 导入整理
pylint *.py       # 代码检查
```

### 常用命令

```bash
# 仅格式化 main.py
black main.py

# 仅检查某文件
pylint code_response.py

# 显示详细的 pylint 报告
pylint *.py --output-format=colorized
```

---

## 📚 规范标准参考

### 遵循的标准

- **[PEP 8](https://www.python.org/dev/peps/pep-0008/)** - Python 代码风格
- **[Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)** - Docstring 风格
- **[Semantic Versioning](https://semver.org/lang/zh-CN/)** - 版本号规范
- **[Keep a Changelog](https://keepachangelog.com/zh-CN/)** - 更新日志规范

### 工具说明

| 工具 | 作用 | 官方文档 |
|------|------|---------|
| Black | 代码格式化 | [black.readthedocs.io](https://black.readthedocs.io/) |
| isort | 导入整理 | [pycqa.github.io/isort/](https://pycqa.github.io/isort/) |
| Pylint | 代码检查 | [pylint.readthedocs.io](https://pylint.readthedocs.io/) |

---

## 🎓 学习路径

### 新手开发者
1. 阅读 README_NEW.md（5 分钟）
2. 查看 STYLE_GUIDE.md（10 分钟）
3. 阅读 CONTRIBUTING.md 开发工作流部分（15 分钟）
4. 开始编写代码，参考示例

### 资深开发者
1. 浏览 STANDARDIZATION_REPORT.md（5 分钟）
2. 检查 pyproject.toml 和 .pylintrc 配置（10 分钟）
3. 参考 CONTRIBUTING.md 完整指南（20 分钟）
4. 参与项目贡献

---

## 💡 常见问题

### Q: VS Code 没有自动格式化？
A: 确保安装了 Black 扩展，或在终端运行 `pip install black`

### Q: pylint 提示太多警告？
A: 参考 STYLE_GUIDE.md 中的示例调整代码，或查看 .pylintrc 配置

### Q: 如何修改代码规范？
A: 编辑 pyproject.toml 和 .pylintrc，具体说明见文件注释

### Q: 规范化脚本出错？
A: 检查 Python 是否安装，运行 `pip install -r requirements-dev.txt`

---

## 📞 获取帮助

- 📖 查看对应的文档文件
- 🔍 搜索 CONTRIBUTING.md 中的常见问题
- 💬 提交 GitHub Issue
- 🤝 参考历史 PR 和 commits

---

## ✅ 规范化检查清单

在提交 PR 前，请检查：

- [ ] 代码已用 Black 格式化
- [ ] 导入已用 isort 整理
- [ ] Pylint 检查无错误（警告可接受）
- [ ] 添加或修改的函数有 docstring
- [ ] 代码包含类型注解
- [ ] 最大行长不超过 120 字符
- [ ] CHANGELOG 已更新
- [ ] 代码可正常运行

---

## 🎯 下次规范化任务

- [ ] 运行 `normalize.bat` 或 `normalize.sh`
- [ ] 根据 pylint 建议调整代码
- [ ] 提交规范化的代码到 Git
- [ ] 参考 CHANGELOG 编写更新说明

---

**最后更新**：2025年12月7日  
**维护者**：@riscorn-zhang  
**许可证**：MIT

