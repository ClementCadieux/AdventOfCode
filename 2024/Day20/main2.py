import sys
import util
import time

args = sys.argv

filePath = "2024\\Day20\\test.txt" if len(args) == 1 else args[1]
minScore = 74 if len(args) == 1 else int(args[2])

startTime = time.time()

grid = util.readFile(filePath)

start = util.findStart(grid)

maxScore = util.scorePath(grid, start)

shortcutsByScore = [0 for i in range(maxScore + 1)]

total = util.findShortcutsPart2(grid, minScore)

print(total)

endTime = time.time()

print(endTime - startTime)