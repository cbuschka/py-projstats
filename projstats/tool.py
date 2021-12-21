import sys

from projstats import git
from projstats.model import Project
import os


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
      added, removed = git.calc_stats(path)
      project.record(added, removed)

  def _print_stats(self):
    for project in self.projects:
      print("{}: +{} -{}".format(project.name, project.added, project.removed))

  def print_usage(self):
    print("projstats { project1 | project2 | ... }")
    sys.exit(1)
