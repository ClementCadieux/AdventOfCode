import sys
import util
import time

start = time.time()

args = sys.argv

filePath = "2024\\Day18\\test.txt" if len(args) == 1 else args[1]
bound = 7 if len(args) == 1 else int(args[2])

coordsList = util.readFile(filePath)

left = 0
right = len(coordsList)

while left < right:
    mid = int((left + right)/2)

    grid = util.genGrid(coordsList, bound, mid)

    scoreGrid = [[bound**2 + 1 for y in range(bound)] for x in range(bound)]

end = time.time()

print(end - start)