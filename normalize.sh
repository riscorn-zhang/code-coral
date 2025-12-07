#!/bin/bash
# Code Coral 项目规范化工具脚本
# Linux/Mac 版本

echo "======================================"
echo "Code Coral 代码规范化工具"
echo "======================================"
echo ""

# 检查 Python 是否安装
if ! command -v python3 &> /dev/null; then
    echo "[错误] 未找到 Python3，请先安装 Python"
    exit 1
fi

echo "[1/4] 检查依赖..."
python3 -m pip show black > /dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "[信息] 安装 black 代码格式化工具..."
    python3 -m pip install black
fi

python3 -m pip show isort > /dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "[信息] 安装 isort 导入整理工具..."
    python3 -m pip install isort
fi

python3 -m pip show pylint > /dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "[信息] 安装 pylint 代码检查工具..."
    python3 -m pip install pylint
fi

echo "[2/4] 格式化代码..."
python3 -m black . --quiet
if [ $? -ne 0 ]; then echo "[警告] black 格式化失败"; fi

echo "[3/4] 整理导入..."
python3 -m isort . --quiet
if [ $? -ne 0 ]; then echo "[警告] isort 整理失败"; fi

echo "[4/4] 检查代码质量..."
python3 -m pylint *.py --disable=C0114,C0115,C0116
if [ $? -ne 0 ]; then echo "[提示] 存在 pylint 警告，请参考 STYLE_GUIDE.md"; fi

echo ""
echo "======================================"
echo "规范化完成！"
echo "======================================"
echo ""
echo "建议："
echo "- 查看 README_NEW.md 了解项目信息"
echo "- 查看 STYLE_GUIDE.md 了解代码规范"
echo "- 查看 CONTRIBUTING.md 了解贡献指南"
echo ""
