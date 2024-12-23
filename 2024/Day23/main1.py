import sys
import util
import time

args = sys.argv

filePath = "2024\\Day23\\test.txt" if len(args) == 1 else args[1]

startTime = time.time()

connections = util.readFile(filePath)

tripleConnections = util.getTripleConnections(connections)

total = 0

for connection in tripleConnections:
    containsT = False
    
    for node in connection:
        if node[0] == "t":
            containsT = True
            break
    
    if containsT:
        total += 1

print(total)

endTime = time.time()

print(endTime - startTime)