import sys
from util import readFile

def isNice(line):
    twoSet = {}
    twoSizeRepeat = False
    splitRepeat = False
    
    for i in range(1, len(line)):
        if not twoSizeRepeat:
            pair = line[i-1:i+1]

            if pair in twoSet:
                startIdx = twoSet[pair]

                if startIdx != i - 2:
                    twoSizeRepeat = True
            else:
                twoSet[pair] = i - 1

        if not splitRepeat and i != len(line) - 1:
            prev = line[i - 1]
            nxt = line[i + 1]

            if prev == nxt:
                splitRepeat = True

    return splitRepeat and twoSizeRepeat

if __name__ == "__main__":
    filePath = "2015\\Day5\\test.txt" if len(sys.argv) < 2 else sys.argv[1]

    lines = readFile(filePath)

    count = 0

    for line in lines:
        if isNice(line):
            count += 1

    print(count)