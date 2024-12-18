import sys
import util

args = sys.argv

filePath = "2024\\Day18\\test.txt" if len(args) == 1 else args[1]
bound = 7 if len(args) == 1 else int(args[2])
sim = 12 if len(args) == 1 else int(args[3])

coordsList = util.readFile(filePath)

grid = util.genGrid(coordsList, bound, sim)

for line in grid:
    print(line)