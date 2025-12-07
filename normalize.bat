@echo off
REM Code Coral 项目规范化工具脚本
REM Windows PowerShell 版本

echo ======================================
echo Code Coral 代码规范化工具
echo ======================================
echo.

setlocal enabledelayedexpansion

REM 检查 Python 是否安装
python --version >nul 2>&1
if errorlevel 1 (
    echo [错误] 未找到 Python，请先安装 Python
    exit /b 1
)

echo [1/4] 检查依赖...
python -m pip show black >nul 2>&1
if errorlevel 1 (
    echo [信息] 安装 black 代码格式化工具...
    python -m pip install black
)

python -m pip show isort >nul 2>&1
if errorlevel 1 (
    echo [信息] 安装 isort 导入整理工具...
    python -m pip install isort
)

python -m pip show pylint >nul 2>&1
if errorlevel 1 (
    echo [信息] 安装 pylint 代码检查工具...
    python -m pip install pylint
)

echo [2/4] 格式化代码...
python -m black . --quiet
if errorlevel 1 echo [警告] black 格式化失败

echo [3/4] 整理导入...
python -m isort . --quiet
if errorlevel 1 echo [警告] isort 整理失败

echo [4/4] 检查代码质量...
python -m pylint *.py --disable=C0114,C0115,C0116
if errorlevel 1 echo [提示] 存在 pylint 警告，请参考 STYLE_GUIDE.md

echo.
echo ======================================
echo 规范化完成！
echo ======================================
echo.
echo 建议：
echo - 查看 README_NEW.md 了解项目信息
echo - 查看 STYLE_GUIDE.md 了解代码规范
echo - 查看 CONTRIBUTING.md 了解贡献指南
echo.
