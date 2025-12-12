from util import readFile
import sys

if __name__ == "__main__":
    args = sys.argv

    filePath = "2025\\Day12\\test.txt" if len(args) < 2 else args[1]

    presents, regions = readFile(filePath)

    count = 0

    for region in regions:
        size = region[0]
        area = size[0]*size[1]

        pList = region[1]

        expectedSize = 0

        for val in pList:
            expectedSize += val*9

        if expectedSize <= area:
            count += 1

    print(count)