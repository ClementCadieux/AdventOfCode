import util
import sys
import time

args = sys.argv

filePath = "2024\\Day24\\test.txt" if len(args) == 1 else args[1]

startTime = time.time()

nodes, nodeIndex = util.readFile(filePath)

# comment in below line if you want a visual display of the system
# util.visualDisplay(nodes, nodeIndex)

xBin = util.getBinary(nodes, nodeIndex, "x")
yBin = util.getBinary(nodes, nodeIndex, "y")

x = int(xBin, 2)
y = int(yBin, 2)

expected = x + y

util.processOps(nodes, nodeIndex)

resStr = util.getBinary(nodes, nodeIndex, "z")

res = int(resStr, 2)

print(res)
print(expected)
print(expected - res)

endTime = time.time()

print(endTime - startTime)