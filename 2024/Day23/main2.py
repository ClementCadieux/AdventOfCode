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

for connection in tripleConnections:
    print(connection)