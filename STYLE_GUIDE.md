# Code Coral 代码规范快速参考

## 📌 核心规范

### 1. 代码风格
```python
# ✅ 正确
def calculate_average(values: list[float]) -> float:
    """计算平均值。"""
    return sum(values) / len(values)

# ❌ 错误
def CalcAvg(vals):
    return sum(vals)/len(vals)
```

### 2. 导入顺序
```python
# 标准库
import os
import sys
from typing import Dict, List

# 第三方库
import ollama
import markdown_it

# 本地模块
import globals
import load_prompt
```

### 3. 类型注解
```python
# ✅ 正确
def process_data(data: List[str], count: int) -> Dict[str, int]:
    pass

# ❌ 不够规范
def process_data(data, count):
    pass
```

### 4. Docstrings
```python
def create_file(path: str, content: str) -> bool:
    """创建文件并写入内容。
    
    Args:
        path: 文件路径
        content: 文件内容
        
    Returns:
        成功返回 True，失败返回 False
        
    Raises:
        IOError: 如果无法创建文件
    """
    pass
```

### 5. 变量命名
```python
# ✅ 正确
user_name = "Alice"
MAX_RETRIES = 3
class DataProcessor:
    pass

# ❌ 错误
userName = "Alice"
max_retries = 3
class dataprocessor:
    pass
```

## 🛠️ 工具命令

```bash
# 代码格式化
black .

# 导入整理
isort .

# 代码检查
pylint *.py

# 一键整理所有文件
black . && isort . && pylint *.py
```

## 📋 提交前检查清单

- [ ] 所有函数/类有 docstrings
- [ ] 使用了类型注解
- [ ] 代码通过 black 格式化
- [ ] 代码通过 pylint 检查（无错误）
- [ ] 导入使用 isort 整理
- [ ] 最大行长不超过 120 字符
- [ ] 代码可以正常执行

## 🚀 快速开始

1. 复制粘贴代码规范
2. 在 IDE 中配置 black 自动格式化
3. 提交前运行 `black . && isort . && pylint *.py`
4. 如果 pylint 有警告，参考上面的示例修改

## 📚 更多资源

- [PEP 8 官方文档](https://www.python.org/dev/peps/pep-0008/)
- [Google Python 风格指南](https://google.github.io/styleguide/pyguide.html)
- [Black 格式化工具](https://black.readthedocs.io/)
- [Pylint 代码检查](https://pylint.readthedocs.io/)
