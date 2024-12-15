def readFile(path):
    file = open(path, "r")

    lines = file.readlines()

    lines = [line[:-1] if line[-1] == "\n" else line for line in lines]

    gridTime = True

    grid = []
    instruction = ""

    for line in lines:
        if line == "":
            gridTime = False
            continue

        if gridTime:
            grid.append(list(line))
        else:
            instruction += line
        
    instruction = list(instruction)

    return grid, instruction

def findRobot(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "@":
                return i,j

def processInstructions(grid, instructions, robotI, robotJ):
    currPos = [robotI, robotJ]

    for instruction in instructions:
        direction = [0, 0]

        match instruction:
            case "^":
                direction[0] -= 1
            case "<":
                direction[1] -= 1
            case ">":
                direction[1] += 1
            case "v":
                direction[0] += 1
        
        movePossible = False

        cellToCheck = [currPos[0] + direction[0], currPos[1] + direction[1]]

        while not movePossible and grid[cellToCheck[0]][cellToCheck[1]] != "#":
            if grid[cellToCheck[0]][cellToCheck[1]] == ".":
                movePossible = True
            else:
                cellToCheck[0] += direction[0]
                cellToCheck[1] += direction[1]

        if movePossible:
            while cellToCheck[0] != currPos[0] or cellToCheck[1] != currPos[1]:
                grid[cellToCheck[0]][cellToCheck[1]] = grid[cellToCheck[0] - direction[0]][cellToCheck[1] - direction[1]]
                cellToCheck[0] -= direction[0]
                cellToCheck[1] -= direction[1]

            grid[currPos[0]][currPos[1]] = "."
            currPos[0] += direction[0]
            currPos[1] += direction[1]
        
def getCoords(grid):
    total = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "O":
                total += 100*i + j

    return total