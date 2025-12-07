"""目录操作工具模块。

提供文件系统目录操作的实用工具函数。
"""

import os


def locate_directory(item_name: str) -> str:
    """定位给定项目的所在目录。

    Args:
        item_name: 项目名称或文件路径

    Returns:
        项目所在目录的绝对路径

    Example:
        >>> locate_directory(__file__)
        '/path/to/project'
    """
    return os.path.dirname(os.path.abspath(item_name))
