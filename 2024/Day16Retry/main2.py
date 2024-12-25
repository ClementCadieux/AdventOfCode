import sys
import util
import time

args = sys.argv

filePath = "2024\\Day16\\test.txt" if len(args) == 1 else args[1]

startTime = time.time()

grid = util.readFile(filePath)

paths = util.dijkstraP2(grid)

seats = set()
for path in paths:
    seats |= set(path)
    
print(len(seats))

endTime = time.time()

print(endTime - startTime)