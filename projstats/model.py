import collections

Stats = collections.namedtuple('Stats', ['added', 'removed'])


class Project(object):
    def __init__(self, name, path):
        self.name = name
        self.path = path
        self.stats_by_year = {}

    def record(self, year, added, removed):
        stats = self.stats_by_year.get(year)
        if stats is None:
            stats = Stats(added=0, removed=0)
        self.stats_by_year[year] = Stats(stats.added + added, stats.removed + removed)
