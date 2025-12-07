"""Code Coral - AI-powered code generation and debugging tool.

使用 Ollama 本地大语言模型生成和修复代码。
"""

__version__ = "0.1.0"
__author__ = "riscorn-zhang"
__license__ = "MIT"

from . import code_response, debug_response, globals

__all__ = ["code_response", "debug_response", "globals"]
