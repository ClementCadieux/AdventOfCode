def readFile(filePath):
    file = open(filePath, 'r')

    lines = [line.strip("\n") for line in file.readlines()]

    splitLines = [line.split(",") for line in lines]

    output = [[int(val) for val in line] for line in splitLines]

    return output

def calcEveryPair(boxes):
    sortedPairs = []
    distancePairs = {}

    for i in range(len(boxes) - 1):
        box1 = boxes[i]
        for j in range(i + 1, len(boxes)):
            box2 = boxes[j]
            pairKey = (i, j)
            sortedPairs.append(pairKey)

            xDistanceVal = (box1[0]-box2[0])**2
            yDistanceVal = (box1[1]-box2[1])**2
            zDistanceVal = (box1[2]-box2[2])**2

            distance = (xDistanceVal + yDistanceVal + zDistanceVal)**(1/2)

            distancePairs[pairKey] = distance

    sortedPairs = sorted(sortedPairs, key=lambda x : -distancePairs[x])

    return sortedPairs

def joinPair(circuits, sortedPairs):
    nextPair = sortedPairs.pop()

    box1 = nextPair[0]
    box2 = nextPair[1]

    box1Circuit = -1
    box2Circuit = -1

    for i in range(len(circuits)):
        circuit = circuits[i]
        if box1 in circuit:
            box1Circuit = i
        
        if box2 in circuit:
            box2Circuit = i

    if box1Circuit == -1:
        if box2Circuit == -1:
            circuits.append(set())
            circuits[-1].add(box1)
            circuits[-1].add(box2)
        else:
            circuits[box2Circuit].add(box1)
    else:
        if box2Circuit == -1:
            circuits[box1Circuit].add(box2)
        elif box1Circuit != box2Circuit:
            circuitWithBox1 = circuits[box1Circuit]
            circuitWithBox2 = circuits[box2Circuit]
            circuits[box1Circuit] = circuitWithBox1 | circuitWithBox2
            circuits.remove(circuitWithBox2)