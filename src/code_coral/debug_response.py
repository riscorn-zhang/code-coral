"""调试和执行模块。

此模块负责执行生成的代码并收集用户反馈。
"""

import os
import subprocess
import sys
from typing import Dict


if sys.platform == "win32":
    # CREATE_NEW_CONSOLE 的值是 0x00000010
    CREATE_NEW_CONSOLE = 0x00000010
else:
    # 在非 Windows 系统上，将该标志设为 0，防止错误
    CREATE_NEW_CONSOLE = 0


def run_code(code_location: str) -> None:
    """执行指定路径的 Python 代码。

    Args:
        code_location: Python 代码文件的路径
    """
    try:
        print("\nExecuting the generated code:\n")
        subprocess.run(
            ["python", code_location],
            check=True,
            creationflags=CREATE_NEW_CONSOLE,
        )
        print("\nExecution completed.\n")
    except Exception as e:
        print(f"\nError: {e}")
        print("Execution completed with an exception.\n")


def ai_debug(requirement: str, responsed_code: str) -> str:
    """AI 调试函数（待实现）。

    Args:
        requirement: 调试需求
        responsed_code: 生成的代码

    Returns:
        调试结果
    """
    # TODO: 实现 AI 调试功能
    return ""


def human_debug(code_location: str) -> Dict:
    """运行用户调试循环。

    在循环中运行代码，允许用户重复执行，然后收集用户反馈（建议或异常）。

    Args:
        code_location: Python 代码文件的路径

    Returns:
        包含反馈类型和内容的字典：
        - type: 'suggestion' 或 'exception'
        - content: 用户的建议或异常信息
    """
    while True:
        run_code(code_location)
        if input("Execute again? (y/[n]): ") != "y":
            break

    suggestion = input("Type some suggestions:>\n")
    return {
        "type": "suggestion",
        "content": suggestion,
    }
