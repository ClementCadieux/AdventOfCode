from util import readFile, presentAreas, validate
import sys

if __name__ == "__main__":
    args = sys.argv

    filePath = "2025\\Day12\\test.txt" if len(args) < 2 else args[1]

    presents, regions = readFile(filePath)

    presentAreaList = presentAreas(presents)

    count = 0

    for region in regions:
        if validate(region, presents, presentAreaList):
            count += 1


    print(count)