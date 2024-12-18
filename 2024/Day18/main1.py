import sys
import util
import time

start = time.time()

args = sys.argv

filePath = "2024\\Day18\\test.txt" if len(args) == 1 else args[1]
bound = 7 if len(args) == 1 else int(args[2])
sim = 12 if len(args) == 1 else int(args[3])

coordsList = util.readFile(filePath)

grid = util.genGrid(coordsList, bound, sim)

scoreGrid = [[bound**2 + 1 for y in range(bound)] for x in range(bound)]
unvisited = set()

for i in range(bound):
    for j in range(bound):
        unvisited.add((i, j))

scoreGrid[0][0] = 0

util.dijkstra(scoreGrid, grid, 0, 0, unvisited)

print(scoreGrid[-1][-1])

end = time.time()

print(end - start)