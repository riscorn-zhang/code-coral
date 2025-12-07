"""配置加载模块。

负责从配置文件加载项目配置信息。
"""

import os
from typing import Any

from .utils import directory_operations

# 项目配置目录
config_dir = os.path.join(
    directory_operations.locate_directory(__file__),
    "..",
    "..",
    "config",
)


def get_config(item: str, name: str) -> Any:
    """从配置文件获取配置值。

    Args:
        item: 配置文件名称（含扩展名）
        name: 配置项的键

    Returns:
        配置项的值
    """
    config_file = os.path.join(config_dir, item)
    # TODO: 实现配置文件解析逻辑
    pass
