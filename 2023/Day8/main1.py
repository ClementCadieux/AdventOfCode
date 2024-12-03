def readFile(path):
    file = open(path, "r")

    instructionLine = file.readline().strip()

    file.readline()
    line = file.readline()


    nodes = {}

    while line != "":
        currNode = line[0:3]

        leftNode = line[7:10]

        rightNode = line[12:15]

        nodes[currNode] = (leftNode, rightNode)

        line = file.readline()

    return (instructionLine, nodes)

def nextNode(currNode, instructions, index, network):
    currInstruction = instructions[index % len(instructions)]

    if currInstruction == "R":
        return network[currNode][1]
    
    return network[currNode][0]


if __name__ == "__main__":
    fileRead = readFile("Day8\\input.txt")

    currNode = 'AAA'
    steps = 0

    while(currNode != 'ZZZ'):
        currNode = nextNode(currNode, fileRead[0], steps, fileRead[1])
        steps += 1

    print(steps)


