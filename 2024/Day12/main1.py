def readFile(path):
    file = open(path, "r")

    lines = file.readlines()

    lines = [line[:-1] if line[-1] == "\n" else line for line in lines]

    return lines

def makeRegionsNumbers(lines):
    newGrid = [[-1 for tile in line] for line in lines]

    currRegionNumber = 0

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if newGrid[i][j] == -1:
                propagateRegion(lines, newGrid, currRegionNumber, lines[i][j], i, j)
                currRegionNumber += 1
    
    return newGrid

def propagateRegion(lines, newGrid, regionNumber, regionLetter, i, j):
    if i == len(lines) or i == -1 or j == len(lines[i]) or j == -1:
        return

    if lines[i][j] != regionLetter or newGrid[i][j] != -1:
        return
    
    newGrid[i][j] = regionNumber

    propagateRegion(lines, newGrid, regionNumber, regionLetter, i - 1, j)
    propagateRegion(lines, newGrid, regionNumber, regionLetter, i + 1, j)
    propagateRegion(lines, newGrid, regionNumber, regionLetter, i, j - 1)
    propagateRegion(lines, newGrid, regionNumber, regionLetter, i, j + 1)

def calcRegionInfo(lines):
    regionInfo = []

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            regionNumber = lines[i][j]

            while regionNumber >= len(regionInfo):
                regionInfo.append([0, 0])

            regionInfo[regionNumber][0] += 1

            fenceLeft = j == 0 or lines[i][j - 1] != regionNumber
            fenceRight = j == len(lines[i]) - 1 or lines[i][j + 1] != regionNumber
            fenceUp = i == 0 or lines[i - 1][j] != regionNumber
            fenceDown = i == len(lines) - 1 or lines[i + 1][j] != regionNumber

            fences = 0
            fences += 1 if fenceLeft else 0
            fences += 1 if fenceRight else 0
            fences += 1 if fenceUp else 0
            fences += 1 if fenceDown else 0

            regionInfo[regionNumber][1] += fences

    return regionInfo
 
def calcCost(regionInfo):
    cost = 0
    for region in regionInfo:
        cost += region[0] * region[1]
    return cost

if __name__ == "__main__":
    lines = readFile("2024\\Day12\\input.txt")

    lines = makeRegionsNumbers(lines)

    regionInfo = calcRegionInfo(lines)

    cost = calcCost(regionInfo)

    print(cost)