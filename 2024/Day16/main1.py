import sys
import util
import time

args = sys.argv

filePath = "2024\\Day16\\test.txt" if len(args) == 1 else args[1]

start = time.time()

lines = util.readFile(filePath)

scores = [[-1 for tile in line] for line in lines]
unvisited = set()

for i in range(len(lines)):
    for j in range(len(lines[i])):
        unvisited.add((i,j))

scores[-2][1] = 0

nonInfinityNodes = []
nonInfinityNodes.append(((len(lines) - 2, 1), 0, 0))

util.dijkstra(scores, lines, len(lines) - 2, 1, unvisited, nonInfinityNodes, 1, 0)

score = scores[1][-2]

print(score)

end = time.time()

print(end - start)