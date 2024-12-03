import main1 as baseFunct

def findPath(grid, i, j):
    pathTiles = set()

    prev = None

    sTowards = 0

    dist = 0

    tile = grid[i][j]

    while prev is None or tile != "S":
        match tile:
            case '|':
                nextPrev = (i,j)
                next = (i - 1, j)
                j = next[1]
                if next[0] != prev[0] or next[1] != prev[1]:
                    i = next[0]
                else:
                    i = next[0] + 2
                
                prev = nextPrev    
            case '-':
                nextPrev = (i,j)
                next = (i, j - 1)
                i = next[0]
                if next[0] != prev[0] or next[1] != prev[1]:
                    j = next[1]
                else:
                    j = next[1] + 2
                
                prev = nextPrev
            case 'L':
                nextPrev = (i,j)
                next = (i, j + 1)
                if next[0] != prev[0] or next[1] != prev[1]:
                    i = next[0]
                    j = next[1]
                else:
                    i = next[0] - 1
                    j = next[1] - 1
                
                prev = nextPrev
            case 'J':
                nextPrev = (i,j)
                next = (i, j - 1)
                if next[0] != prev[0] or next[1] != prev[1]:
                    i = next[0]
                    j = next[1]
                else:
                    i = next[0] - 1
                    j = next[1] + 1
                
                prev = nextPrev
            case '7':
                nextPrev = (i,j)
                next = (i, j - 1)
                if next[0] != prev[0] or next[1] != prev[1]:
                    i = next[0]
                    j = next[1]
                else:
                    i = next[0] + 1
                    j = next[1] + 1
                
                prev = nextPrev
            case 'F':
                nextPrev = (i,j)
                next = (i, j + 1)
                if next[0] != prev[0] or next[1] != prev[1]:
                    i = next[0]
                    j = next[1]
                else:
                    i = next[0] + 1
                    j = next[1] - 1
                
                prev = nextPrev
            case 'S':
                if prev is not None:
                    return int(dist / 2 + dist % 2)
                
                right = '.' if j == len(grid[i]) else grid[i][j + 1]

                if right in ["7", "J", "-"]:
                    prev = (i,j)
                    j += 1
                    sTowards = 1
                
                left = '.' if j == 0 else grid[i][j - 1]

                if left in ["-", "F", "L"] and prev is None:
                    prev = (i,j)
                    j -= 1
                    sTowards = 2
                
                up = '.' if i == 0 else grid[i - 1][j]

                if up in ["|", "F", "7"] and prev is None:
                    prev = (i,j)
                    i -= 1
                    sTowards = 3
                
                if prev is None:
                    prev = (i,j)
                    i += 1
                    sTowards = 4
            
        tile = grid[i][j]
        if tile != "S": 
            pathTiles.add((i, j, tile))

    sIncoming = 0

    xDiff = i - prev[0]
    yDiff = j - prev[1]

    if xDiff == -1:
        sIncoming = 4
    elif xDiff == 1:
        sIncoming = 3
    elif yDiff == -1:
        sIncoming = 1
    else:
        sIncoming = 2

    match ((sIncoming, sTowards)):
        case (1, 2):
            tile = "-"
        case (2, 1):
            tile = "-"
        case (1, 3):
            tile = "L"
        case (3, 1):
            tile = "L"
        case (1, 4):
            tile = "F"
        case (4, 1):
            tile = "F"
        case (2, 3):
            tile = "J"
        case (3, 2):
            tile = "J"
        case (2, 4):
            tile = "7"
        case (4, 2):
            tile = "7"
        case (3, 4):
            tile = "|"
        case (4, 3):
            tile = "|"

    pathTiles.add((i, j, tile))
    grid[i][j] = tile

    return pathTiles

def resetGrid(grid, tilesInPath):
    tileMap = {
        ".": [[".", ".", "."], [".", ".", "."], [".", ".", "."]],
        "|": [["X", "#", "X"], ["X", "#", "X"], ["X", "#", "X"]],
        "-": [["X", "X", "X"], ["#", "#", "#"], ["X", "X", "X"]],
        "L": [["X", "#", "X"], ["X", "#", "#"], ["X", "X", "X"]],
        "7": [["X", "X", "X"], ["#", "#", "X"], ["X", "#", "X"]],
        "F": [["X", "X", "X"], ["X", "#", "#"], ["X", "#", "X"]],
        "J": [["X", "#", "X"], ["#", "#", "X"], ["X", "X", "X"]]
    }

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (i, j, grid[i][j]) not in tilesInPath:
                grid[i][j] = "."
            
            grid[i][j] = tileMap[grid[i][j]]

    return grid

def processGrid(grid):
    changes = 1

    while changes != 0:
        print(changes)
        changes = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                tile = grid[i][j]

                if tile == "." or tile == "X":
                    iBef = i - 1 if i > 0 else i
                    iAft = i + 2 if i < len(grid) - 1 else i + 1
                    jBef = j - 1 if j > 0 else j
                    jAft = j + 2 if j < len(grid[i]) - 1 else j + 1

                    oAdjacent = False

                    for x in range(iBef, iAft):
                        for y in range(jBef, jAft):
                            if grid[x][y] == "O":
                                oAdjacent = True
                                break

                        if oAdjacent:
                            break
                    
                    if oAdjacent or i == 0 or i == len(grid) - 1 or j == 0 or j == len(grid[i]) - 1:
                        grid[i][j] = "O"
                        changes += 1

def flatten(grid):
    newGrid = []
    for line in grid:
        currentInLine = 0

        while currentInLine < 3:
            currLine = []
            for tile in line:
                inLine = tile[currentInLine]

                for inTile in inLine:
                    currLine.append(inTile)

            newGrid.append(currLine)
            currentInLine += 1
    
    return newGrid

            

if __name__ == "__main__":
    grid = baseFunct.readFile("Day10\\input.txt")

    tilesInPath = None

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'S':
                tilesInPath = findPath(grid, i, j)
                break

        if tilesInPath != None:
            break

    grid = resetGrid(grid, tilesInPath)

    grid = flatten(grid)

    processGrid(grid)

    area = len(grid) * len(grid[0])

    outputFile = open("Day10\\gridOutput.txt", "w")

    for line in grid:
        for tile in line:
            outputFile.write(tile)
            if(tile != "."):
                area -= 1
        outputFile.write("\n")
    
    outputFile.close

    print(area/9)