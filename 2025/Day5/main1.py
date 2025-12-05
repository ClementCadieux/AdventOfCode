from util import readFile
import sys

def isInRange(ranges, num):
    for i in range(len(ranges)):
        currRange = ranges[i]
        if num >= currRange[0] or num <= currRange[1]:
            return i
        
    return -1

def buildSmartRanges(ranges):
    

if __name__ == "__main__":
    filePath = "2025\\Day5\\test.txt" if len(sys.argv) < 2 else sys.argv[1]

    ranges, ids = readFile(filePath)

