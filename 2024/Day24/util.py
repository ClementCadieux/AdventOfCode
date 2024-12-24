def readFile(path):
    file = open(path, "r")

    lines = file.readlines()

    lines = [line[:-1] if line[-1] == "\n" else line for line in lines]

    nodeIndex = {}
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

    return (nodes, nodeIndex)

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

def getBinary(nodes, nodeIndex, letter):
    res = ""

    num = 0

    node = letter + ("0" if num < 10 else "") + str(num)

    while node in nodeIndex:
        value = nodes[nodeIndex[node]]

        bit = "1" if value else "0"

        res = bit + res

        num += 1

        node = "z" + ("0" if num < 10 else "") + str(num)
    
    return res