"""提示词加载模块。

负责从文件系统加载 AI 提示词模板。
"""

import os

from .utils import directory_operations


def file_of_prompt(item: str) -> str:
    """获取提示词文件的完整路径。

    Args:
        item: 提示词名称（不含 .md 扩展名）

    Returns:
        提示词文件的绝对路径
    """
    return os.path.join(
        directory_operations.locate_directory(__file__),
        "..",
        "..",
        "prompts",
        item + ".md",
    )


def load_prompt(item: str) -> str:
    """加载提示词文件内容。

    Args:
        item: 提示词名称（不含 .md 扩展名）

    Returns:
        提示词文件的内容

    Raises:
        FileNotFoundError: 如果提示词文件不存在
    """
    response_prompt = ""
    with open(file_of_prompt(item), "r", encoding="utf-8") as file:
        response_prompt = file.read()
    return response_prompt
