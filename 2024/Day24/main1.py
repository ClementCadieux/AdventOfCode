import util
import sys
import time

args = sys.argv

filePath = "2024\\Day24\\test.txt" if len(args) == 1 else args[1]

startTime = time.time()

nodes, nodeIndex = util.readFile(filePath)

util.processOps(nodes)

resStr = util.getZBinary(nodes, nodeIndex)

