# 更新日志

所有项目的重要变更都将记录在这个文件中。

格式遵循 [Keep a Changelog](https://keepachangelog.com/zh-CN/) 规范，
版本号遵循 [Semantic Versioning](https://semver.org/lang/zh-CN/) 规范。

## [Unreleased]

### Added
- 代码风格和命名规范规范化
- 添加 pyproject.toml 配置文件
- 添加 .editorconfig 编辑器配置
- 添加 .pylintrc 代码检查配置
- 完整的项目文档和贡献指南
- 所有模块的 docstrings 和类型注解

### Changed
- 改进导入语句组织
- 优化代码格式和可读性
- 增强异常处理

### Fixed
- 拼写错误（code_locaition -> code_location）

## [0.1.0] - 2025-12-07

### Added
- 初始版本发布
- 基于 Ollama API 的代码生成功能
- 代码执行和调试功能
- 基于用户反馈的代码改进功能
- 异常自动修复功能

### Features
- ✨ AI 代码生成
- 🔄 迭代优化支持
- 🐛 错误修复
- 💻 实时代码执行

---

## 发布规范

### 创建新发布

1. 更新 CHANGELOG.md
2. 更新版本号在相关文件中
3. 创建 git tag: `git tag -a v0.2.0 -m "Release version 0.2.0"`
4. 推送 tag: `git push origin v0.2.0`

### 版本号规则

- MAJOR：有不兼容的 API 改动
- MINOR：新增功能，向后兼容
- PATCH：修复 bug，向后兼容

示例：v1.2.3
- 1：主版本号
- 2：次版本号
- 3：修订版本号
