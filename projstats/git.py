import subprocess
import re


def _exec_git(cmd, cwd=None):
  proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, cwd=cwd)
  while True:
    line = proc.stdout.readline()
    if not line:
      break
    line = line.decode("utf-8").rstrip()
    yield line
  return None


def get_commit_years(path):
  pattern = re.compile("^(\d\d\d\d)-\d\d-\d\d\s.*$")
  years = set()
  for line in _exec_git(["git", "log", "--pretty=format:%ai"], cwd=path):
    if not line:
      break
    result = pattern.match(line)
    if result:
      years.add(int(result.group(1)))
  return sorted(years)


def calc_stats(path, year):
  pattern = re.compile("^(\d+)\s+(\d+)\s+([^\s]+)$")
  added = 0
  removed = 0
  for line in _exec_git(
    ["git", "log", "--since={}-01-01".format(year), "--until={}-12-31".format(year), "--pretty=tformat:", "--numstat"],
    cwd=path):
    if not line:
      break
    result = pattern.match(line)
    if result:
      added = added + int(result.group(1))
      removed = removed + int(result.group(2))

  return (added, removed)
