import main1 as base

def calcRegionInfo(lines):
    sideGrid = sideByTiles(lines)

    return None

def sideByTiles(lines):
    sideGrid = [[[] for tile in line] for line in lines]

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            regionNum = lines[i][j]

            left = j == 0 or lines[i][j - 1] != regionNum
            right = j == len(lines[i]) - 1 or lines[i][j + 1] != regionNum
            up = i == 0 or lines[i - 1][j] != regionNum
            down = i == len(lines) - 1 or lines[i + 1][j] != regionNum

            sides = 0

            if left:
                sides += 1000
            if right:
                sides += 10
            if up:
                sides += 100
            if down:
                sides += 1
            
            sideGrid[i][j] = sides
    
    return sideGrid

if __name__ == "__main__":
    lines = base.readFile("2024\\Day12\\test.txt")

    lines  = base.makeRegionsNumbers(lines)

    regionInfo = calcRegionInfo(lines)

    cost = base.calcCost(regionInfo)

    print(cost)