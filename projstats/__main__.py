from projstats.tool import Tool
import sys
import logging

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    tool = Tool()
    if len(sys.argv) > 1:
        tool.run(sys.argv[1:])
    else:
        tool.print_usage()
