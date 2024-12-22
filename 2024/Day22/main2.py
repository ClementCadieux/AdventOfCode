import sys
import time
import util

args = sys.argv

filePath = "2024\\Day22\\test2.txt" if len(args) == 1 else args[1]

startTime = time.time()

nums = util.readFile(filePath)

endTime = time.time()

print(endTime - startTime)