"""Historical analytics data models.

Stores verified GitHub snapshots for trend analysis.
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class RepositorySnapshot:
    repository_name: str
    stars: int
    forks: int
    watchers: int
    open_issues: int
    language: Optional[str]
    collected_at: datetime


@dataclass
class ActivitySnapshot:
    repository_name: str
    commits: int
    contributors: int
    pull_requests: int
    issues: int
    collected_at: datetime
