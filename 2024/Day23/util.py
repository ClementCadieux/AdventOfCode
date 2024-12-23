import copy

def readFile(path):
    file = open(path, "r")

    lines = file.readlines()

    lines = [line[:-1] if line[-1] == "\n" else line for line in lines]

    splitLines = [line.split("-") for line in lines]

    connections = {}

    for line in splitLines:
        left = line[0]
        right = line[1]

        if left not in connections:
            connections[left] = set()
        if right not in connections:
            connections[right] = set()
        
        connections[left].add(right)
        connections[right].add(left)

    return connections

def getTripleConnections(connections):
    tripleConnections = []

    for node in connections:
        seenNodes = set()
        connectTo = connections[node]

        for nextNode in connectTo:
            nextConnectTo = connections[nextNode]

            intersectSet = connectTo & nextConnectTo

            for thirdNode in intersectSet:
                if thirdNode in seenNodes:
                    continue
                group = set()
                group.add(node)
                group.add(nextNode)
                group.add(thirdNode)

                tripleConnections.append(group)
                if node in connections[thirdNode]:
                    connections[thirdNode].remove(node)

            seenNodes.add(nextNode)
        
        connections[node].clear()
    return tripleConnections
    
def buildLongestConnections(tripleConnections, connections):
    for tripleConnection in tripleConnections:
        allConnections = set()
        assigned = False

        for node in tripleConnection:
            if not assigned:
                allConnections = connections[node]
                assigned = True
            else:
                allConnections = allConnections & connections[node]

        tripleConnection.update(allConnections)            

        