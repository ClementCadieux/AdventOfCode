from util import readFile
import sys

def isInRange(ranges, num):
    for i in range(len(ranges)):
        currRange = ranges[i]
        if num >= currRange[0] and num <= currRange[1]:
            return i
        
    return -1

def buildSmartRanges(ranges):
    newRanges = []

    for i in range(len(ranges)):
        currRange = ranges[i]

        start = currRange[0]
        end = currRange[1]

        startIn = isInRange(newRanges, start)
        endIn = isInRange(newRanges, end)

        if startIn != -1 and endIn != -1:
            if startIn != endIn:
                newRanges[startIn][1] = newRanges[endIn][1]
                newRanges.remove(newRanges[endIn])
        elif startIn != -1:
            newRanges[startIn][1] = end
        elif endIn != -1:
            newRanges[endIn][0] = start
        else:
            newRanges.append(currRange)
    
    return cleanUpRanges(newRanges)

def cleanUpRanges(newRanges):
    newRangesCopy = []

    for i in range(len(newRanges)):
        if toCopy(newRanges, i):
            newRangesCopy.append(newRanges[i])

    return newRangesCopy
        
def toCopy(newRanges, i):
    currRange = newRanges[i]
    for j in range(i + 1, len(newRanges)):
        nextRange = newRanges[j]

        if currRange[0] >= nextRange[0] and currRange[1] <= nextRange[1]:
            return False
        
    return True


if __name__ == "__main__":
    filePath = "2025\\Day5\\test.txt" if len(sys.argv) < 2 else sys.argv[1]

    ranges, ids = readFile(filePath)

    smartRanges = buildSmartRanges(ranges)

    count = 0

    for val in ids:
        if isInRange(smartRanges, val) != -1:
            count += 1

    print(count)