# 贡献指南

感谢对 Code Coral 项目的关注！以下是贡献代码的指南。

## 代码风格规范

### Python 代码风格

项目遵循 [PEP 8](https://www.python.org/dev/peps/pep-0008/) 标准。

#### 格式要求

- **缩进**：使用 4 个空格
- **最大行长**：120 字符
- **字符编码**：UTF-8

#### 命名规范

```python
# 模块名：小写，下划线分隔
my_module.py

# 函数和变量：小写，下划线分隔
def calculate_total():
    user_input = ""

# 常量：全大写，下划线分隔
MAX_ATTEMPTS = 3
DEFAULT_MODEL = "codegemma"

# 类名：大驼峰式
class CodeResponser:
    pass
```

#### 类型注解

所有函数必须包含类型注解：

```python
def process_data(data: List[str], count: int) -> Dict[str, int]:
    """处理数据的函数。
    
    Args:
        data: 字符串列表
        count: 计数
        
    Returns:
        处理结果字典
    """
    pass
```

### 文档字符串（Docstrings）

使用 Google 风格的 docstrings：

```python
def calculate_average(values: List[float]) -> float:
    """计算值的平均数。
    
    Args:
        values: 浮点数值列表
        
    Returns:
        平均值
        
    Raises:
        ValueError: 如果列表为空
        
    Example:
        >>> calculate_average([1.0, 2.0, 3.0])
        2.0
    """
    if not values:
        raise ValueError("列表不能为空")
    return sum(values) / len(values)
```

## 开发工作流

### 1. 设置开发环境

```bash
# 克隆仓库
git clone https://github.com/riscorn-zhang/code-coral.git
cd code-coral

# 创建虚拟环境
python -m venv env
source env/bin/activate  # Linux/Mac
# 或
env\Scripts\activate  # Windows

# 安装开发依赖
pip install -r requirements.txt
pip install pylint black isort
```

### 2. 创建功能分支

```bash
git checkout -b feature/your-feature-name
```

### 3. 开发并测试

```bash
# 代码格式化
black .
isort .

# 代码检查
pylint *.py
```

### 4. 提交代码

```bash
git add .
git commit -m "feat: 简洁的功能描述"
```

提交信息规范：
- `feat:` 新功能
- `fix:` 修复 bug
- `docs:` 文档更新
- `style:` 代码格式调整
- `refactor:` 代码重构
- `test:` 添加或修改测试
- `chore:` 构建过程或依赖管理

### 5. 推送并创建 Pull Request

```bash
git push origin feature/your-feature-name
```

在 GitHub 上创建 Pull Request，描述你的改动内容。

## 提交 Issue

提交 issue 前，请检查是否已有相同问题。

使用以下模板：

```markdown
## 问题描述
简洁地描述问题

## 复现步骤
1. 第一步
2. 第二步
3. ...

## 预期结果
应该发生什么

## 实际结果
实际发生了什么

## 环境信息
- Python 版本：
- 操作系统：
- 相关依赖版本：
```

## 代码审查

所有 Pull Request 都需要通过代码审查。审查员会检查：

- 代码风格是否符合规范
- 功能是否完整且正确
- 文档是否清晰
- 是否有测试覆盖

## 许可证

通过提交代码，你同意你的贡献将在 MIT 许可证下发布。

---

再次感谢你的贡献！
