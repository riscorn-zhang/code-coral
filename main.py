"""主程序入口模块。

此模块提供了 Code Coral 项目的主要工作流程：
1. 获取用户需求
2. 使用 AI 生成代码
3. 用户调试和反馈循环
"""

import os
import sys
from typing import Dict

# 添加 src 目录到 Python 路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from code_coral import code_response, debug_response, globals, load_prompt


def ask_for_original_requirement() -> str:
    """询问用户输入代码生成需求。

    Returns:
        用户输入的需求字符串，或默认提示的内容
    """
    file_of_default_prompt = load_prompt.file_of_prompt("default_prompt")
    prompt = input(
        f"请输入你想让AI生成代码的描述 ( 默认: {file_of_default_prompt} ): "
    )
    if prompt.strip() == "":
        prompt = load_prompt.load_prompt("default_prompt")

    return prompt


def main() -> None:
    """运行 Code Coral 的主循环。

    工作流程：
    1. 获取用户需求
    2. 生成初始代码
    3. 循环：用户调试和反馈
    """
    prompt = ask_for_original_requirement()
    code_responser = code_response.CodeResponser()
    code_file_name = code_responser.make_original_code(prompt)

    print(f"\n\n\n{code_responser.message_list}\n\n\n")

    while True:
        result: Dict = debug_response.human_debug(code_file_name)
        if result["type"] == "suggestion":
            if result["content"].strip() == "":
                break
            code_file_name = code_responser.make_suggested_code(result["content"])
        else:
            code_file_name = code_responser.make_excepted_code(result["content"])


if __name__ == "__main__":
    print(
        "Available models before running the chat "
        "(And for starting the service of Ollama if it is not running):"
    )
    os.system("ollama list")
    print("")
    main()