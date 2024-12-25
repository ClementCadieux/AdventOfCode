import sys
import util
import time

args = sys.argv

filePath = "2024\\Day16\\test.txt" if len(args) == 1 else args[1]

startTime = time.time()

grid = util.readFile(filePath)

boundI = len(grid)
boundJ = len(grid[0])

scoreGrid = [[boundJ*boundI + 1 for y in range(boundJ)] for x in range(boundI)]
unvisited = set()

for i in range(boundI):
    for j in range(boundJ):
        unvisited.add((i, j))

scoreGrid[boundI - 2][1] = 0

nonInfinityNodes = []
nonInfinityNodes.append((boundI - 2, 1))

util.dijkstra(scoreGrid, grid, boundI - 2, 1, unvisited, nonInfinityNodes, 1, 0)

score = scoreGrid[1][-2]

print(score)

endTime = time.time()

print(endTime - startTime)