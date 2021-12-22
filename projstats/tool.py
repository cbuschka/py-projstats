import logging
import os

from projstats import git
from projstats.model import Project

log = logging.getLogger(__name__)


class Tool(object):
    def __init__(self):
        self.projects = []

    def run(self, args):
        self._load_projects(args.project_paths)
        self._collect_stats()
        self._print_stats()

    def _load_projects(self, project_paths):
        for project_path in project_paths:
            name = os.path.basename(project_path[0:-1] if project_path.endswith("/") else project_paths)
            project = Project(name, project_path)
            self.projects.append(project)

    def _collect_stats(self):
        for project in self.projects:
            path = project.path
            commits_by_year = git.get_commits_by_year(path)
            for year in commits_by_year.keys():
                log.info("Collecting stats of project {} for year {} from {}".format(project.name, year, path))
                added, removed = git.calc_stats(path, year)
                project.record(year, added, removed, commits_by_year[year])

    def _print_stats(self):
        for project in self.projects:
            print("{}: {}".format(project.name, project.stats_by_year))

    def print_usage(self):
        print("projstats { project1 | project2 | ... }")
