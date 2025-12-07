"""全局配置模块的单元测试。"""

import pytest
import sys
import os
import tempfile

# 添加 src 目录到路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from code_coral import globals as globals_module


class TestGlobals:
    """全局配置的测试。"""

    def test_globals_initialization(self):
        """测试全局配置初始化。"""
        assert "tmp_dir" in globals_module.globals
        assert "initialed" in globals_module.globals
        assert globals_module.globals["initialed"] is True

    def test_tmp_dir_exists(self):
        """测试临时目录是否存在。"""
        tmp_dir = globals_module.globals["tmp_dir"]
        assert os.path.exists(tmp_dir)
        assert os.path.isdir(tmp_dir)

    def test_tmp_dir_contains_codecoral(self):
        """测试临时目录包含 CodeCoral。"""
        tmp_dir = globals_module.globals["tmp_dir"]
        assert "CodeCoral" in tmp_dir


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
