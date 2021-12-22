from projstats import prog_args
from projstats.tool import Tool
import sys
import logging

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    tool = Tool()
    args = prog_args.parse(sys.argv[1:])
    if len(args.project_paths) == 0:
        tool.print_usage()
        sys.exit(1)

    tool.run(args)
