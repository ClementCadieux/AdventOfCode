import util
import sys
import time

args = sys.argv

filePath = "2024\\Day24\\test.txt" if len(args) == 1 else args[1]

startTime = time.time()

nodes, nodeIndex = util.readFile(filePath)

util.processOps(nodes, nodeIndex)

resStr = util.getBinary(nodes, nodeIndex, "z")

res = int(resStr, 2)

print(res)

endTime = time.time()

print(endTime - startTime)