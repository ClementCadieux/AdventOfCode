def readFile(filePath):
    file = open(filePath, 'r')

    lines = [line.strip("\n") for line in file.readlines()]

    presents = []

    linesIdx = 0

    for _ in range(6):
        linesIdx += 1

        present = []

        for i in range(linesIdx, linesIdx + 3):
            present.append(lines[i])
            linesIdx = i

        linesIdx += 2

        presents.append(present)

    regions = lines[linesIdx:]

    splitRegions = [[x.strip() for x in region.split(":")] for region in regions]

    regionDict = []

    for region in splitRegions:
        key = region[0]
        vals = region[1]

        splitKey = tuple([int(val) for val in key.split("x")])
        splitVals = [int(val) for val in vals.split(" ")]

        regionDict.append([splitKey, splitVals])

    return presents, regionDict