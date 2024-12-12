import main1 as base

def calcRegionInfo(lines):
    sideGrid = sideByTiles(lines)

    regionInfo = []

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            regionNumber = lines[i][j]

            while regionNumber >= len(regionInfo):
                regionInfo.append([0, 0])
            
            regionInfo[regionNumber][0] += 1

            sides = sideGrid[i][j]

            upLeft = sides[0] or j == 0 or not sideGrid[i][j - 1][2]

            if sides[2] and upLeft:
                regionInfo[regionNumber][1] += 1
            
            downLeft = sides[0] or j == 0 or not sideGrid[i][j - 1][3]

            if sides[3] and downLeft:
                regionInfo[regionNumber][1] += 1

            leftUp = sides[2] or i == 0 or not sideGrid[i - 1][j][0]

            if sides[0] and leftUp:
                regionInfo[regionNumber][1] += 1
            
            leftDown = sides[2] or i == 0 or not sideGrid[i - 1][j][1]

            if sides[1] and leftDown:
                regionInfo[regionNumber][1] += 1

    return regionInfo

def sideByTiles(lines):
    sideGrid = [[[] for tile in line] for line in lines]

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            regionNum = lines[i][j]

            left = j == 0 or lines[i][j - 1] != regionNum
            right = j == len(lines[i]) - 1 or lines[i][j + 1] != regionNum
            up = i == 0 or lines[i - 1][j] != regionNum
            down = i == len(lines) - 1 or lines[i + 1][j] != regionNum
            
            sideGrid[i][j] = [left, right, up, down]
    
    return sideGrid

if __name__ == "__main__":
    lines = base.readFile("2024\\Day12\\input.txt")

    lines  = base.makeRegionsNumbers(lines)

    regionInfo = calcRegionInfo(lines)
    
    cost = base.calcCost(regionInfo)

    print(cost)