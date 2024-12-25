import sys
import util
import time

args = sys.argv

filePath = "2024\\Day16\\test.txt" if len(args) == 1 else args[1]

startTime = time.time()

grid = util.readFile(filePath)

boundI = len(grid)
boundJ = len(grid[0])

scoreGrid = [[-1 for y in range(boundJ)] for x in range(boundI)]
unvisited = set()
comesFrom = {}

for i in range(boundI):
    for j in range(boundJ):
        unvisited.add((i, j))
        comesFrom[(i,j)] = []

scoreGrid[boundI - 2][1] = 0

nonInfinityNodes = []
nonInfinityNodes.append((boundI - 2, 1))

util.dijkstra(scoreGrid, grid, boundI - 2, 1, unvisited, nonInfinityNodes, 1, 0, comesFrom)

endProcess = util.backtrackPath(comesFrom, 1, boundJ - 2, (boundI - 2, 1))

print(endProcess[1])

endTime = time.time()

print(endTime - startTime)