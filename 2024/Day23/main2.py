import sys
import util
import time
import copy

args = sys.argv

filePath = "2024\\Day23\\test.txt" if len(args) == 1 else args[1]

startTime = time.time()

connections = util.readFile(filePath)

connectionsCopy = copy.deepcopy(connections)

tripleConnections = util.getTripleConnections(connections)

util.buildLongestConnections(tripleConnections, connectionsCopy)

longestConnection = tripleConnections[0]

for connection in tripleConnections:
    if len(connection) > len(longestConnection):
        longestConnection = connection

listConnection = list(longestConnection)

listConnection.sort()

res = ""

for node in listConnection:
    if len(res) != 0:
        res += ","
    res += node

print(res)

endTime = time.time()

print(endTime - startTime)