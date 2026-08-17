# Crawler Lab

Crawler Lab 是一个用于 Codex 的爬虫 Skill / Plugin，目标是帮助用户设计、审查和展示**合规、可验证、可复用**的 Python 静态网页爬虫工作流。

这个项目主要面向两个场景：

- **面试和作品展示**：用一个稳定的本地 Demo 展示爬虫工程能力、合规意识和结构化输出能力。
- **日常复用**：让 Codex 在生成或审查爬虫时，默认遵守授权、robots.txt、限速、隐私保护和错误处理等边界。

## 功能

- 设计 Python 静态网页爬虫方案。
- 审查爬虫代码中的合规风险和稳定性问题。
- 将 HTML 页面解析为结构化 CSV / JSON。
- 使用本地 HTML fixture 做稳定演示，不依赖真实网站网络环境。
- 提供 robots.txt、限速、User-Agent、重试、日志、隐私数据处理等合规参考。

## 合规边界

Crawler Lab 默认采用保守合规策略：

- 采集第三方网站或非公开系统前，先确认授权。
- 优先使用官方 API；如果必须爬取网页，应遵守 robots.txt、服务条款和公开限速规则。
- 不绕过验证码、登录墙、付费墙、封禁、反爬机制或访问控制。
- 不采集敏感个人信息，除非存在明确合法授权，并且只采集最小必要字段。
- 遇到连续 `401`、`403`、`429`、验证码页面或封禁提示时，应立即停止。

## 仓库结构

```text
.
├── .agents/plugins/marketplace.json        # Codex marketplace 定义
├── .codex-plugin/plugin.json               # 根目录插件 manifest
├── plugins/crawler-lab/                    # marketplace 安装用插件副本
└── skills/crawler-lab/                     # 直接安装用 Skill
    ├── SKILL.md
    ├── agents/openai.yaml
    ├── assets/fixtures/sample_catalog.html
    ├── references/compliance-and-reliability.md
    └── scripts/crawl_fixture.py
```

## 作为 Codex Skill 安装

这是最简单、最稳定的安装方式。

### Windows PowerShell

```powershell
Copy-Item -LiteralPath ".\skills\crawler-lab" -Destination "$env:USERPROFILE\.codex\skills\crawler-lab" -Recurse -Force
```

### Windows CMD

```cmd
xcopy ".\skills\crawler-lab" "%USERPROFILE%\.codex\skills\crawler-lab" /E /I /Y
```

复制完成后，重启 Codex 或新开一个任务，然后输入：

```text
用 Crawler Lab 帮我设计一个合规爬虫
```

如果 Codex 能识别 `crawler-lab`，说明安装成功。

## 作为 Codex Plugin Marketplace 安装

如果你的 Codex 环境可以正常访问 GitHub，可以把这个仓库作为 marketplace 添加：

```text
https://github.com/zjp1011/crawler-lab
```

添加后，安装 `Crawler Lab Marketplace` 里的 `crawler-lab` 插件。

如果添加 marketplace 时出现 GitHub clone 失败、连接被重置、代理不可用等问题，建议使用上面的 **Skill 直接安装方式**。

## 运行本地 Demo

Demo 不访问真实网站，只解析仓库内置的本地 HTML fixture，并导出 CSV / JSON。

在仓库根目录运行：

### Windows

```powershell
py .\skills\crawler-lab\scripts\crawl_fixture.py
```

### macOS / Linux 或已配置 `python` 命令的环境

```bash
python ./skills/crawler-lab/scripts/crawl_fixture.py
```

预期输出：

```text
Parsed 3 records
CSV: ...\skills\crawler-lab\tmp\sample_catalog.csv
JSON: ...\skills\crawler-lab\tmp\sample_catalog.json
```

输出字段示例：

```json
{
  "title": "Robots And Rate Limits",
  "url": "/reports/robots-and-rate-limits",
  "category": "Policy",
  "date": "2026-03-18",
  "summary": "A practical note on respectful request pacing for public pages."
}
```

## 示例提示词

```text
用 Crawler Lab 帮我设计一个合规爬虫
```

```text
检查这个爬虫有没有合规和稳定性问题
```

```text
把这个 HTML 页面解析成 CSV 和 JSON
```

```text
我面试时想展示一个 Python 爬虫项目，帮我组织讲法
```

## 说明

- 内置 Demo 使用 Python 标准库解析 HTML，不需要额外安装依赖。
- 真实项目中建议根据页面复杂度选择 `beautifulsoup4`、`lxml` 或官方 API。
- 如果网站提供稳定 API，应优先使用 API，而不是直接抓取网页。
