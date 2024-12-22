import sys
import time
import util

args = sys.argv

filePath = "2024\\Day22\\test.txt" if len(args) == 1 else args[1]

startTime = time.time()

nums = util.readFile(filePath)

total = 0

for val in nums:
    num = val
    for i in range(2000):
        num = util.calcNumPart1(num)

    total += num

print(total)

endTime = time.time()

print(endTime - startTime)