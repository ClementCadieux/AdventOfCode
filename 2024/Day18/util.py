def readFile(filePath):
    file = open(filePath, "r")

    lines = file.readlines()

    lines = [line[:-1] if line[-1] == "\n" else line for line in lines]

    splitLines = [line.split(",") for line in lines]

    intSplitLines = [[int(coord) for coord in line] for line in splitLines]

    return intSplitLines

def genGrid(coords, bound, sim):
    grid = [["." for j in range(bound)] for i in range(bound)]

    for i in range(sim):
        coord = coords[i]
        grid[coord[1]][coord[0]] = "#"

    return grid

def scoreTile(grid, scoreGrid, i, j, score):
    if scoreGrid[i][j] <= score or grid[i][j] == "#":
        return
    
    scoreGrid[i][j] = score

    up = (i - 1, j)
    down = (i + 1, j)
    left = (i, j - 1)
    right = (i, j + 1)

    upPossible = i != 0 and grid[up[0]][up[1]] != "#" and scoreGrid[up[0]][up[1]] > score + 1
    downPossible = i != len(grid) - 1 and grid[down[0]][down[1]] != "#" and scoreGrid[down[0]][down[1]] > score + 1
    leftPossible = j != 0 and grid[left[0]][left[1]] != "#" and scoreGrid[left[0]][left[1]] > score + 1
    rightPossible = j != len(grid[i]) - 1 and grid[right[0]][right[1]] != "#" and scoreGrid[right[0]][right[1]] > score + 1

    if upPossible:
        scoreTile(grid, scoreGrid, up[0], up[1], score + 1)
    if downPossible:
        scoreTile(grid, scoreGrid, down[0], down[1], score + 1)
    if leftPossible:
        scoreTile(grid, scoreGrid, left[0], left[1], score + 1)
    if rightPossible:
        scoreTile(grid, scoreGrid, right[0], right[1], score + 1)