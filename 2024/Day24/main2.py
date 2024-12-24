import util
import sys
import time

args = sys.argv

filePath = "2024\\Day24\\test.txt" if len(args) == 1 else args[1]

startTime = time.time()

nodes, nodeIndex = util.readFile(filePath)

util.processOps(nodes)

xStr = util.getBinary(nodes, nodeIndex, "x")
yStr = util.getBinary(nodes, nodeIndex, "y")

x = int(xStr, 2)
y = int(yStr, 2)

expectedRes = x + y

resStr = util.getBinary(nodes, nodeIndex, "z")

res = int(resStr, 2)

print(x)
print(y)

print(res)
print(expectedRes)

endTime = time.time()

print(endTime - startTime)