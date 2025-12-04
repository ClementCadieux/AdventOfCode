from util import readFile
import sys

if __name__ == "__main__":
    filePath = "2015\\Day8\\test.txt" if len(sys.argv) < 2 else sys.argv[1]

    lines = readFile(filePath)

    rawCount = 0
    reducedCount = 0

    for line in lines:
        rawCount += len(line)

        processedCount = len(line) - 2

        for i in range(1, len(line) - 2):
            if line[i] == "\\":
                processedCount -= 1

                i += 1

                next = line[i]

                if next == "x":
                    i += 2
                    processedCount -= 2
            
        reducedCount += processedCount

    print(rawCount - reducedCount)