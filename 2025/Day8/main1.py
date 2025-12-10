from util import readFile, calcEveryPair, joinPair
import sys

if __name__ == "__main__":
    filePath = "2025\\Day8\\test.txt" if len(sys.argv) < 2 else sys.argv[1]
    iterations = 10 if len(sys.argv) < 3 else int(sys.argv[2])

    boxes = readFile(filePath)

    sortedPairs = calcEveryPair(boxes)

    circuits = []

    joinsMade = 0

    while joinsMade < iterations:
        joinPair(circuits, sortedPairs)

        joinsMade += 1

    circuits = sorted(circuits, key=lambda x : -len(x))

    total = 1

    for i in range(3):
        total *= len(circuits[i])

    print(total)