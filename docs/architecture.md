# 项目架构文档

## 目录结构

```
code-coral/
├── src/
│   └── code_coral/              # 主源代码包
│       ├── __init__.py
│       ├── code_response.py      # 代码生成模块
│       ├── debug_response.py     # 调试执行模块
│       ├── globals.py            # 全局配置
│       ├── load_prompt.py        # 提示词加载
│       ├── config_loader.py      # 配置加载
│       └── utils/                # 工具模块
│           ├── __init__.py
│           └── directory_operations.py
├── tests/                         # 测试目录
│       ├── __init__.py
│       ├── test_code_response.py
│       └── test_globals.py
├── docs/                          # 文档目录
│       └── architecture.md
├── config/                        # 配置文件
│       ├── general.yaml
│       └── description.md
├── prompts/                       # 提示词模板
│       ├── default_prompt.md
│       ├── python_simple.md
│       ├── suggestion_addition.md
│       ├── exception_addition.md
│       └── debugger.md
├── main.py                        # 主程序入口
├── pyproject.toml                 # 项目配置
├── setup.py                       # 安装脚本
├── requirements.txt               # 依赖列表
├── requirements-dev.txt           # 开发依赖
├── README.md                      # 项目说明
├── CONTRIBUTING.md                # 贡献指南
├── CHANGELOG.md                   # 更新日志
├── STYLE_GUIDE.md                 # 代码规范
└── .gitignore                     # Git 忽略规则
```

## 包结构说明

### src/code_coral/
主源代码包，包含项目的核心功能。

- `__init__.py` - 包初始化文件
- `code_response.py` - AI 代码生成
- `debug_response.py` - 代码执行和调试
- `globals.py` - 全局配置和初始化
- `load_prompt.py` - 加载 AI 提示词
- `config_loader.py` - 加载项目配置
- `utils/` - 工具函数包

### tests/
单元测试目录。

- `test_code_response.py` - 代码生成模块测试
- `test_globals.py` - 全局配置测试

### docs/
项目文档目录。

- `architecture.md` - 项目架构文档

## 导入规范

### 项目内部导入

在 `src/code_coral/` 内：

```python
# 相对导入
from . import globals
from . import load_prompt
from .utils import directory_operations

# 或使用完整包路径
from code_coral import globals
from code_coral import load_prompt
from code_coral.utils import directory_operations
```

### 从外部导入

```python
import sys
import os

# 添加 src 目录到路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

# 然后导入
from code_coral import code_response
from code_coral import debug_response
```

## 开发流程

1. **新功能开发**：在 `src/code_coral/` 中实现
2. **编写测试**：在 `tests/` 中添加测试
3. **运行测试**：`pytest tests/`
4. **代码检查**：`pylint src/`
5. **提交变更**：遵循 commit 规范

## 安装方式

### 本地开发安装

```bash
# 创建虚拟环境
python -m venv env
source env/bin/activate  # Linux/Mac
env\Scripts\activate     # Windows

# 安装项目（开发模式）
pip install -e .

# 安装依赖
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

### 从 PyPI 安装（未来）

```bash
pip install code-coral
```

## 配置管理

配置文件存储在 `config/` 目录：

- `general.yaml` - 通用配置
- `description.md` - 项目描述

配置通过 `config_loader.py` 加载。

## 日志和临时文件

- 临时生成的代码存储在系统临时目录的 `CodeCoral/` 子目录
- 位置由 `globals.py` 中的 `globals["tmp_dir"]` 定义

## 扩展建议

### 添加新模块

1. 在 `src/code_coral/` 下创建新 `.py` 文件
2. 在 `src/code_coral/__init__.py` 中导出
3. 为新模块添加单元测试
4. 更新文档

### 添加新工具

1. 在 `src/code_coral/utils/` 下创建新 `.py` 文件
2. 在 `src/code_coral/utils/__init__.py` 中导出
3. 从其他模块通过相对导入使用

---

**创建日期**：2025-12-07  
**维护者**：@riscorn-zhang
