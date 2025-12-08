from util import readFile, calcEveryPair, joinPair
import sys

if __name__ == "__main__":
    filePath = "2025\\Day8\\test.txt" if len(sys.argv) < 2 else sys.argv[1]

    boxes = readFile(filePath)

    sortedPairs = calcEveryPair(boxes)

    circuits = []

    lastPair = None

    while len(circuits) == 0 or len(circuits[0]) != len(boxes):
        lastPair = sortedPairs[-1]
        
        joinPair(circuits, sortedPairs)

    lastBox1 = boxes[lastPair[0]]
    lastBox2 = boxes[lastPair[1]]

    lastX1 = lastBox1[0]
    lastX2 = lastBox2[0]

    res = lastX1 * lastX2

    print(res)
