import subprocess


def calc_stats(since=None, until=None):
  proc = subprocess.Popen(
    ["git", "log", "--since=2020-01-01", "--until=2020-12-31", "--pretty=tformat:", "--numstat"],
    stdout=subprocess.PIPE)
  while True:
    line = proc.stdout.readline()
    if not line:
      break
    line = line.decode("utf-8").rstrip()
    print("stats: {}".format(line))
