"""代码生成模块。

此模块负责与 Ollama AI 模型交互生成、修改和调试代码。
"""

import os
import time
from typing import Dict, List

import markdown_it
import ollama

from . import globals, load_prompt


class CodeResponser:
    """负责代码生成和修改的类。

    与 Ollama AI 模型交互，根据用户需求生成代码，并能根据建议和异常反馈进行修改。
    """

    model: str = "codegemma"
    message_list: List[Dict] = []
    md: markdown_it.MarkdownIt = markdown_it.MarkdownIt("commonmark")

    def __init__(self) -> None:
        """初始化 CodeResponser。

        设置系统提示和对话历史。
        """
        self.message_list.append(
            {
                "role": "system",
                "content": load_prompt.load_prompt("python_simple"),
            }
        )

    def make_original_code(self, requirement: str) -> str:
        """根据用户需求生成初始代码。

        Args:
            requirement: 用户描述的功能需求

        Returns:
            生成的代码文件路径
        """
        return self.make_code(requirement)

    def make_suggested_code(self, requirement: str) -> str:
        """根据用户建议修改代码。

        Args:
            requirement: 用户的建议内容

        Returns:
            修改后的代码文件路径
        """
        prompt = load_prompt.load_prompt("suggestion_addition").format(
            suggestion=requirement
        )
        return self.make_code(prompt)

    def make_excepted_code(self, requirement: str) -> str:
        """根据异常信息修复代码。

        Args:
            requirement: 异常信息或错误描述

        Returns:
            修复后的代码文件路径
        """
        prompt = load_prompt.load_prompt("exception_addition").format(
            exception=requirement
        )
        return self.make_code(prompt)

    def make_code(self, prompt: str) -> str:
        """与 AI 模型交互生成或修改代码。

        Args:
            prompt: 发送给 AI 模型的提示

        Returns:
            保存生成代码的文件路径
        """
        while True:
            self.message_list.append(
                {
                    "role": "user",
                    "content": prompt,
                }
            )
            stream = ollama.chat(
                model=self.model,
                messages=self.message_list,
                stream=True,
            )
            tmp_file = os.path.join(
                globals.globals["tmp_dir"], str(time.time()) + ".py"
            )

            original_response = ""
            code_response = ""

            for chunk in stream:
                print(chunk["message"]["content"], end="", flush=True)
                original_response += chunk["message"]["content"]

            try:
                code_response = self.extract_code_blocks(original_response)[0]
                break
            except (IndexError, ValueError):
                pass

        self.message_list.append(
            {"role": "assistant", "content": code_response}
        )

        with open(tmp_file, "w", encoding="utf-8") as tmp_file_obj:
            tmp_file_obj.write(code_response)

        print("\n\nResponse saved to:", tmp_file)

        return tmp_file

    def extract_code_blocks(self, markdown_text: str) -> List[str]:
        """从 Markdown 文本中提取代码块。

        Args:
            markdown_text: 包含代码块的 Markdown 文本

        Returns:
            代码块列表
        """
        tokens = self.md.parse(markdown_text)
        code_blocks = []
        for token in tokens:
            if token.type == "fence":
                code_blocks.append(token.content)
        return code_blocks
