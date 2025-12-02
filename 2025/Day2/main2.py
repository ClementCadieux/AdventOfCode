import sys
from util import readFile

def isPattern(iStr):
    for i in range(1, int(len(iStr)/2) + 1):
        if len(iStr) % i == 0:
            if isPatternAtLen(iStr, i):
                return True

    return False


def isPatternAtLen(iStr, length):
    segment = iStr[:length]
    for i in range(length, len(iStr), length):
        newSegment = iStr[i : i + length]
        if newSegment != segment:
            return False
    
    return True

if __name__ == "__main__":
    filePath = "2025\\Day2\\test.txt" if len(sys.argv) == 1 else sys.argv[1]

    ranges = readFile(filePath)
    
    invalids = []

    for idRange in ranges:
        start = int(idRange[0])
        end = int(idRange[1])

        for i in range(start, end + 1):
            iStr = str(i)

            if isPattern(iStr):
                invalids.append(i)


    total = sum(invalids)
    
    print(total)


