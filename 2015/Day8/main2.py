from util import readFile
import sys

if __name__ == "__main__":
    filePath = "2015\\Day8\\test.txt" if len(sys.argv) < 2 else sys.argv[1]

    lines = readFile(filePath)

    rawCount = 0
    increasedCount = 0

    for line in lines:
        rawCount += len(line)

        processCount = len(line) + 2

        for i in range(len(line)):
            if line[i] == "\"":
                processCount += 1
            elif line[i] == "\\":
                processCount += 1
        
        increasedCount += processCount

    print(increasedCount - rawCount)