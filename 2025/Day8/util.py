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

    sortedPairs = sorted(sortedPairs, key=lambda x : distancePairs[x])

    return sortedPairs, distancePairs