def readFile(path):
    file = open(path, "r")

    lines = file.readlines()

    lines = [line[:-1] if line[-1] == "\n" else line for line in lines]

    nodeIndex = {}
    zNodes = {}
    nodes = []

    inWires = True

    for line in lines:
        if inWires:
            if line == "":
                inWires = False
            else:
                splitLine = line.split(":")

                node = splitLine[0]
                value = True if splitLine[1].strip() == "1" else False

                nodeIndex[node] = len(nodes)
                nodes.append(value)
                
                if node[0] == "z":
                    zNodes[node] = nodeIndex[node]
        else:
            splitLine = line.split("->")

            leftSplit = splitLine[0].split(" ")

            targetNode = splitLine[1].strip()

            opLeftNode = leftSplit[0]
            opRightNode = leftSplit[2]

            op = leftSplit[1]

            if opLeftNode not in nodeIndex:
                nodeIndex[opLeftNode] = len(nodes)
                nodes.append(-1)

            if opRightNode not in nodeIndex:
                nodeIndex[opRightNode] = len(nodes)
                nodes.append(-1)

            if targetNode not in nodeIndex:
                nodeIndex[targetNode] = len(nodes)
                nodes.append(-1)

            nodes[nodeIndex[targetNode]] = (nodeIndex[opLeftNode], op, nodeIndex[opRightNode])
            if targetNode[0] == "z":
                zNodes[node] = nodeIndex[node]

    return nodes, zNodes

def processOps(nodes):
    changed = True

    while changed:
        changed = False

        for i in range(len(nodes)):
            node = nodes[i]
            if not isinstance(node, bool):
                leftNode = nodes[node[0]]
                rightNode = nodes[node[2]]

                validOp = isinstance(leftNode, bool) and isinstance(rightNode, bool)

                if validOp:
                    match node[1]:
                        case "AND":
                            node = leftNode and rightNode
                        case "XOR":
                            node = leftNode != rightNode
                        case "OR":
                            node = leftNode or rightNode

                    changed = True
                    nodes[i] = node

