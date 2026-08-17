---
name: crawler-lab
description: Build, review, and demonstrate compliant Python static web crawlers. Use when Codex is asked to create a web scraping/crawling script, check whether a crawler is compliant or robust, parse HTML into CSV/JSON, explain crawler engineering experience for interviews, or produce a stable local crawler demo without relying on live websites.
---

# Crawler Lab

Use this skill for compliant, testable Python static crawling work. Favor stable demos, explicit boundaries, and structured outputs over clever scraping tricks.

# Required Workflow
- Confirm or infer the crawler goal, data owner/authorization, data use, target scope, request frequency, and output format before implementation when those details affect legality, safety, or load.
- Prefer local fixtures or user-provided HTML for demonstrations. Use live websites only when the user has authorization and the task can respect robots.txt, terms, and rate limits.
- Refuse or redirect requests to bypass access controls, evade bans, defeat CAPTCHAs, scrape behind unauthorized login walls, collect sensitive personal data, or violate site terms.
- Implement the smallest crawler that meets the goal: fetch or load HTML, parse stable selectors, normalize records, validate required fields, and export CSV/JSON.
- Include operational safeguards for real sites: descriptive User-Agent, timeout, retry budget, rate limit, robots.txt check, logging, and respectful failure behavior.
- Deliver scripts with a short run command, dependency notes, output schema, verification steps, and any remaining risks.

# Bundled Resources
- For compliance and reliability guidance, read `references/compliance-and-reliability.md`.
- For a stable demo, use `assets/fixtures/sample_catalog.html` and `scripts/crawl_fixture.py`.

# Implementation Defaults
- Use Python 3.10+.
- For local demos, avoid network access and parse fixture HTML from disk.
- For simple deterministic extraction, Python standard-library parsers are acceptable. For real-world HTML, recommend `beautifulsoup4` or `lxml` when dependencies can be installed.
- Write outputs next to the chosen output path, not into source fixtures.
- Keep selectors easy to explain in interviews: record container, title, URL, category, date, and summary are enough for v1.

# Review Checklist
- Authorization and intended use are clear.
- Scope and rate are limited.
- robots.txt or equivalent policy is respected for live targets.
- No credentials, session cookies, CAPTCHAs, paywalls, or access controls are bypassed.
- Personal or sensitive data is avoided unless there is explicit lawful authorization and minimization.
- Parser handles missing optional fields and reports skipped malformed records.
- Outputs have a documented schema and deterministic encoding.

