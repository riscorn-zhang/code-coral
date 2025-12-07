"""代码生成模块的单元测试。"""

import pytest
import sys
import os

# 添加 src 目录到路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from code_coral import code_response


class TestCodeResponser:
    """CodeResponser 类的测试。"""

    def test_extract_code_blocks(self):
        """测试代码块提取功能。"""
        responser = code_response.CodeResponser()
        
        # 测试单个代码块
        markdown_text = """
Some text before

```python
def hello():
    print("Hello, World!")
```

Some text after
        """
        
        blocks = responser.extract_code_blocks(markdown_text)
        assert len(blocks) == 1
        assert 'def hello():' in blocks[0]
        assert 'print("Hello, World!")' in blocks[0]

    def test_extract_multiple_code_blocks(self):
        """测试多个代码块提取。"""
        responser = code_response.CodeResponser()
        
        markdown_text = """
```python
x = 1
```

Some text

```python
y = 2
```
        """
        
        blocks = responser.extract_code_blocks(markdown_text)
        assert len(blocks) == 2
        assert 'x = 1' in blocks[0]
        assert 'y = 2' in blocks[1]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
