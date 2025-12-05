from util import readFile
import sys

def isInRange(ranges, num):
    for i in range(len(ranges)):
        currRange = ranges[i]
        if num >= currRange[0] and num <= currRange[1]:
            return i
        
    return -1

def buildSmartRanges(ranges):
    newList = []

    for currRange in ranges:
        start = ["start", currRange[0]]
        end = ["end", currRange[1]]

        newList.append(start)
        newList.append(end)

    sortedByString = sorted(newList, key=lambda x: x[0], reverse=True)
    sortedList = sorted(sortedByString, key=lambda x : x[1])

    smartRanges = []

    currPointer = 0
    lastStart = -1

    for pointer in sortedList:
        if pointer[0] == "start":
            if currPointer == 0:
                lastStart = pointer[1]
            
            currPointer += 1
        else:
            currPointer -= 1

            if currPointer == 0:
                smartRanges.append([lastStart, pointer[1]])

    return smartRanges

if __name__ == "__main__":
    filePath = "2025\\Day5\\test.txt" if len(sys.argv) < 2 else sys.argv[1]

    ranges, ids = readFile(filePath)

    smartRanges = buildSmartRanges(ranges)
    count = 0

    for val in ids:
        if isInRange(smartRanges, val) != -1:
            count += 1

    print(count)