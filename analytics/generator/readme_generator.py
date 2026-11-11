"""README analytics section generator.

Generates only the protected analytics block. Existing profile content remains untouched.
"""
from datetime import datetime, timezone

START = "<!-- ANALYTICS-START -->"
END = "<!-- ANALYTICS-END -->"


def generate_analytics_section(metrics: dict) -> str:
    updated = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
    return f"""{START}

## 📊 GitHub Analytics Dashboard

| Metric | Value |
|---|---:|
| Repositories | {metrics.get('repositories', 0)} |
| Stars | {metrics.get('stars', 0)} |
| Forks | {metrics.get('forks', 0)} |
| Commits | {metrics.get('commits', 'N/A')} |
| Contributors | {metrics.get('contributors', 'N/A')} |

_Last verified synchronization: {updated}_

{END}"""


def update_readme(content: str, metrics: dict) -> str:
    section = generate_analytics_section(metrics)
    if START in content and END in content:
        before = content.split(START)[0]
        after = content.split(END)[1]
        return before + section + after
    return content + "\n\n" + section
