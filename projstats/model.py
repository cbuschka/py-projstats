class Project(object):
  def __init__(self, name, path):
    self.name = name
    self.path = path
    self.added = 0
    self.removed = 0

  def record(self, added, removed):
    self.added = self.added + added
    self.removed = self.removed + removed
