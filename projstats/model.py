import collections

Stats = collections.namedtuple('Stats', ['added', 'removed', "commit_count"])


class Project(object):
    def __init__(self, name, path):
        self.name = name
        self.path = path
        self.stats_by_year = {}

    def record(self, year, added, removed, commit_count):
        stats = self.stats_by_year.get(year)
        if stats is None:
            stats = Stats(added=0, removed=0, commit_count=0)
        self.stats_by_year[year] = Stats(stats.added + added, stats.removed + removed, commit_count)
