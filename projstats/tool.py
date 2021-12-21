import sys
import logging

from projstats import git
from projstats.model import Project
import os

log = logging.getLogger(__name__)


class Tool(object):
    def __init__(self):
        self.projects = []

    def run(self, args):
        self._load_projects(args)
        self._collect_stats()
        self._print_stats()

    def _load_projects(self, args):
        for arg in args:
            name = os.path.basename(arg)
            project = Project(name, arg)
            self.projects.append(project)

    def _collect_stats(self):
        for project in self.projects:
            path = project.path
            commits_by_year = git.get_commits_by_year(path)
            for year in commits_by_year.keys():
                log.info("Collecting stats for {} from {}".format(year, path))
                added, removed = git.calc_stats(path, year)
                project.record(year, added, removed, commits_by_year[year])


    def _print_stats(self):
        for project in self.projects:
            print("{}: {}".format(project.name, project.stats_by_year))

    def print_usage(self):
        print("projstats { project1 | project2 | ... }")
        sys.exit(1)
