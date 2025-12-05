def readFile(filePath):
    file = open(filePath, 'r')

    lines = file.readlines()

    strippedLines = [line.strip("\n") for line in lines]

    ranges = []
    ids = []

    isRanges = True

    for line in strippedLines:
        if isRanges:
            if line == "":
                isRanges = False
            else:
                splitLine = line.split("-")

                rangeStart = int(splitLine[0])
                rangeEnd = int(splitLine[1])

                ranges.append([rangeStart, rangeEnd])
        else:
            ids.append(int(line))

    return ranges, ids