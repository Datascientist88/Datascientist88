"""Calculate verified GitHub analytics metrics."""


def calculate_growth(current: int, previous: int):
    if previous == 0:
        return None
    return round(((current - previous) / previous) * 100, 2)


def repository_kpis(repositories):
    return {
        "repositories": len(repositories),
        "stars": sum(r.get("stars", 0) for r in repositories),
        "forks": sum(r.get("forks", 0) for r in repositories),
    }
