import sys
import util
import time

args = sys.argv

filePath = "2024\\Day20\\test.txt" if len(args) == 1 else args[1]

start = time.time()

grid = util.readFile(filePath)

start, end = util.findStartAndEnd(grid)

