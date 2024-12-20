def readFile(path):
    file = open(path,"r")

    lines = file.readlines()

    lines = [line[:-1] if line[-1] == "\n" else line for line in lines]

    grid = [list(line) for line in lines]

    return grid

def findStart(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "S":
                return (i,j)

def scorePath(grid, start):
    score = 0

    i = start[0]
    j = start[1]

    direction = 0

    down = (i + 1, j)
    left = (i, j - 1)
    right = (i, j + 1)

    downTile = grid[down[0]][down[1]]
    leftTile = grid[left[0]][left[1]]
    rightTile = grid[right[0]][right[1]]

    if downTile == ".":
        direction = 2
    elif leftTile == ".":
        direction = 3
    elif rightTile == ".":
        direction = 1
        
    while grid[i][j] != "E":
        grid[i][j] = score

        forward = (i - 1, j)
        left = (i, j - 1)
        right = (i, j + 1)

        match direction:
            case 1:
                forward = (i, j + 1)
                left = (i - 1, j)
                right = (i + 1, j)
            case 2:
                forward = (i + 1, j)
                left = (i, j + 1)
                right = (i, j - 1)
            case 3:
                forward = (i, j - 1)
                left = (i + 1, j)
                right = (i - 1, j)

        leftTile = grid[left[0]][left[1]]
        rightTile = grid[right[0]][right[1]]

        if leftTile == ".":
            i = left[0]
            j = left[1]
            direction -= 1
            if direction == -1:
                direction = 3
        elif rightTile == ".":
            i = right[0]
            j = right[1]
            direction += 1
            direction %= 4
        else:
            i = forward[0]
            j = forward[1]
        
        score += 1

    grid[i][j] = score