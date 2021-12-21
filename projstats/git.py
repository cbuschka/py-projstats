import subprocess
import re


def calc_stats(path, since=None, until=None):
  proc = subprocess.Popen(
    ["git", "log", "--since=2020-01-01", "--until=2021-12-31", "--pretty=tformat:", "--numstat"],
    stdout=subprocess.PIPE, cwd=path)
  pattern = re.compile("^(\d+)\s+(\d+)\s+([^\s]+)$")
  added = 0
  removed = 0
  while True:
    line = proc.stdout.readline()
    if not line:
      break
    line = line.decode("utf-8").rstrip()
    result = pattern.match(line)
    if result:
      added = added + int(result.group(1))
      removed = removed + int(result.group(2))

  return (added, removed)
