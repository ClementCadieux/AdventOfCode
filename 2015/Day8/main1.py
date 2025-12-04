from util import readFile
import sys

if __name__ == "__main__":
    filePath = "2015\\Day8\\test.txt" if len(sys.argv) < 2 else sys.argv[1]

    lines = readFile(filePath)

    rawCount = 0
    reducedCount = 0

    for line in lines:
        rawCount += len(line)
        
        processedCount = 0

        i = 1
        while i < len(line) - 1:
            if line[i] == "\\":
                i += 4 if line[i+1] == "x" else 2
            else:
                i += 1
            processedCount += 1

        reducedCount += processedCount

    print(rawCount - reducedCount)