def presentAreas(presents):
    areas = []

    for present in presents:
        area = 0

        for line in present:
            for char in line:
                if char == "#":
                    area += 1

        areas.append(area)

    return areas

def validate(region, presents, presentAreas):
    size = region[0]
    area = size[0]*size[1]

    pList = region[1]

    #Quick check 1: if all presents can fit as 3x3
    maximumSize = 0

    maximumSize += sum(pList)*9

    if maximumSize <= area:
        return True
    
    #Quick check 2: if total area of "#" in presents is too large
    totalArea = 0

    for i in range(len(pList)):
        totalArea += pList[i]*presentAreas[i]

    if totalArea > area:
        return False

    #Long check
    

    return True

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