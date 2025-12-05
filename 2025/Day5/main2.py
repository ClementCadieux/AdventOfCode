from util import readFile
import sys
from main1 import buildSmartRanges

if __name__ == "__main__":
    filePath = "2025\\Day5\\test.txt" if len(sys.argv) < 2 else sys.argv[1]

    ranges, _ = readFile(filePath)

    smartRanges = buildSmartRanges(ranges)

    count = 0

    for smartRange in smartRanges:
        size = smartRange[1] - smartRange[0] + 1

        count += size

    print(count)