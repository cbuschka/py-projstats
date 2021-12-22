class ProgArgs(object):
    def __init__(self, project_paths):
        self.project_paths = project_paths


def parse(args):
    project_paths = []
    for i in range(0, len(args)):
        arg = args[i]
        project_paths.append(arg)

    return ProgArgs(project_paths)
