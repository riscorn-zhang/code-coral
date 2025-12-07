"""全局配置模块。

存储项目全局变量和初始化逻辑。
"""

import os
import tempfile
from typing import Any, Dict

# 全局配置字典
globals: Dict[str, Any] = {
    "tmp_dir": os.path.join(tempfile.gettempdir(), "CodeCoral"),
    "initialed": False,
}


def init() -> None:
    """初始化全局配置。

    创建必要的临时目录。
    """
    os.makedirs(globals["tmp_dir"], exist_ok=True)


# 自动初始化
if not globals["initialed"]:
    globals["initialed"] = True
    init()
