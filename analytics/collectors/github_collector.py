"""
GitHub Analytics Collector
Collects verified repository metrics from GitHub API.
"""

import os
from github import Github


class GitHubCollector:
    def __init__(self):
        token = os.getenv("GITHUB_TOKEN")
        if not token:
            raise RuntimeError("GITHUB_TOKEN is required")
        self.client = Github(token)

    def collect_repositories(self, username: str):
        user = self.client.get_user(username)
        repositories = []

        for repo in user.get_repos():
            repositories.append({
                "name": repo.name,
                "stars": repo.stargazers_count,
                "forks": repo.forks_count,
                "watchers": repo.watchers_count,
                "issues": repo.open_issues_count,
                "language": repo.language,
                "created_at": repo.created_at.isoformat(),
                "updated_at": repo.updated_at.isoformat()
            })

        return repositories


if __name__ == "__main__":
    collector = GitHubCollector()
    print(collector.collect_repositories("Datascientist88"))
