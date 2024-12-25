import sys
import time
import util

args = sys.argv

filePath = "2024\\Day25\\test.txt" if len(args) == 1 else args[1]

startTime = time.time()

keys, locks = util.readFile(filePath)

total = 0

for key in keys:
    for lock in locks:
        if util.matchingKey(key, lock):
            total += 1

print(total)

endTime = time.time()

print(endTime - startTime)