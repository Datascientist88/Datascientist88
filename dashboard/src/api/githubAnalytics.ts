import type { GitHubAnalytics } from '../data/types';

export async function fetchAnalytics(): Promise<GitHubAnalytics> {
  const response = await fetch('/api/analytics');

  if (!response.ok) {
    throw new Error('Unable to retrieve analytics data');
  }

  return response.json();
}
