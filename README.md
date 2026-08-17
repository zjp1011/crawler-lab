# Crawler Lab

Crawler Lab is a Codex skill/plugin for designing, reviewing, and demonstrating compliant Python static web crawlers.

It is built for two use cases:

- **Portfolio and interviews**: show a repeatable crawler demo with clear compliance boundaries.
- **Daily Codex use**: ask Codex to design, review, or scaffold a crawler with safety checks, structured output, and local fixtures.

## What It Does

- Designs Python static crawler workflows.
- Reviews crawler code for compliance and reliability risks.
- Parses HTML into structured CSV/JSON outputs.
- Uses local HTML fixtures for stable demos without live network scraping.
- Documents safe defaults for robots.txt, rate limits, timeouts, retries, and sensitive data handling.

## Compliance Boundaries

Crawler Lab is intentionally conservative:

- Confirm authorization before crawling third-party or private systems.
- Respect robots.txt, terms of service, official APIs, and published rate limits.
- Do not bypass CAPTCHA, paywalls, login walls, bans, or anti-bot controls.
- Do not collect sensitive personal data unless there is explicit lawful authorization and a clear minimization plan.
- Stop on repeated `401`, `403`, `429`, CAPTCHA-like pages, or block responses.

## Repository Layout

```text
.
├── .agents/plugins/marketplace.json        # Codex marketplace definition
├── .codex-plugin/plugin.json               # Plugin manifest for root plugin layout
├── plugins/crawler-lab/                    # Marketplace-installable plugin copy
└── skills/crawler-lab/                     # Direct skill install copy
    ├── SKILL.md
    ├── agents/openai.yaml
    ├── assets/fixtures/sample_catalog.html
    ├── references/compliance-and-reliability.md
    └── scripts/crawl_fixture.py
```

## Install As A Codex Skill

This is the simplest and most reliable installation path.

### Windows PowerShell

```powershell
Copy-Item -LiteralPath ".\skills\crawler-lab" -Destination "$env:USERPROFILE\.codex\skills\crawler-lab" -Recurse -Force
```

### Windows CMD

```cmd
xcopy ".\skills\crawler-lab" "%USERPROFILE%\.codex\skills\crawler-lab" /E /I /Y
```

After copying, restart Codex or open a new task. Then try:

```text
用 Crawler Lab 帮我设计一个合规爬虫
```

## Install As A Codex Plugin Marketplace

If your Codex environment can access GitHub, add this repository as a marketplace:

```text
https://github.com/zjp1011/crawler-lab
```

Then install the `crawler-lab` plugin from `Crawler Lab Marketplace`.

If GitHub cloning fails because of network or proxy issues, use the direct skill installation method above.

## Run The Local Demo

The demo performs no network requests. It parses the bundled local HTML fixture and exports CSV/JSON.

From the repository root:

Windows:

```powershell
py .\skills\crawler-lab\scripts\crawl_fixture.py
```

macOS/Linux or environments where `python` is on PATH:

```powershell
python .\skills\crawler-lab\scripts\crawl_fixture.py
```

Expected output:

```text
Parsed 3 records
CSV: ...\skills\crawler-lab\tmp\sample_catalog.csv
JSON: ...\skills\crawler-lab\tmp\sample_catalog.json
```

Output schema:

```json
{
  "title": "Robots And Rate Limits",
  "url": "/reports/robots-and-rate-limits",
  "category": "Policy",
  "date": "2026-03-18",
  "summary": "A practical note on respectful request pacing for public pages."
}
```

## Example Prompts

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

## Interview Talking Point

You can describe the project like this:

> I built a Codex skill/plugin for compliant crawler engineering. It checks authorization and robots.txt expectations, avoids bypassing access controls, uses local HTML fixtures for repeatable parser tests, separates fetching/parsing/validation/export, and exports deterministic CSV/JSON results.

## Notes

- The bundled demo uses Python standard-library parsing so it can run without extra dependencies.
- For real-world pages, use `beautifulsoup4` or `lxml` when dependencies are available.
- Prefer official APIs over scraping whenever a reliable API exists.
