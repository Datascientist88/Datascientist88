export interface GitHubAnalytics {
  repositories: number;
  stars: number;
  forks: number;
  commits: number;
  contributors: number;
  languages: number;
  lastUpdated: string;
}

export interface RepositoryMetric {
  name: string;
  stars: number;
  forks: number;
  language: string;
}
