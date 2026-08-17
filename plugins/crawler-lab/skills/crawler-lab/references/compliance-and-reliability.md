# Compliance And Reliability Reference

# Boundaries
- Treat crawling as authorized data access. Ask for authorization when the target is a third-party site, private system, login-only area, or ambiguous source.
- Respect robots.txt, terms of service, API alternatives, and published rate limits for live websites.
- Do not help bypass CAPTCHA, IP bans, login walls, anti-bot controls, paywalls, or other access restrictions.
- Avoid collecting sensitive personal data. If the user has a legitimate need, minimize fields, document purpose, and avoid storing secrets or unnecessary identifiers.

# Safe Defaults For Live Crawlers
- Set a clear User-Agent that identifies the script or organization.
- Use timeouts on all network requests.
- Limit concurrency. Start with serial requests or very small concurrency.
- Add delay between requests and exponential backoff for transient failures.
- Stop on repeated 401, 403, 429, or CAPTCHA-like responses.
- Log request counts, skipped records, and parse failures without logging secrets.

# Engineering Checklist
- Define an output schema before coding.
- Prefer stable semantic selectors over brittle visual selectors.
- Normalize URLs, whitespace, dates, and missing values.
- Separate fetching, parsing, validation, and exporting functions.
- Test parsers against saved HTML fixtures before touching live sites.
- Keep examples reproducible without network access whenever possible.

