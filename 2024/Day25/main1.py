import sys
import time
import util

args = sys.argv

filePath = "2024\\Day25\\test.txt" if len(args) == 1 else args[1]

startTime = time.time()

keys, locks = util.readFile(filePath)

for key in keys:
    print(key)

for lock in locks:
    print(lock)