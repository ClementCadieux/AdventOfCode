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

def processInstructionsSingleWidth(grid, instructions, robotI, robotJ):
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
        
        moveRobot(grid, currPos, direction)

def moveRobot(grid, currPos, direction):
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
        
def getCoordsSingleWidth(grid):
    total = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "O":
                total += 100*i + j

    return total

def doubleGrid(grid):
    newGrid = []

    for line in grid:
        newLine = []

        for tile in line:
            match tile:
                case "@":
                    newLine.append("@")
                    newLine.append(".")
                case ".":
                    newLine.append(".")
                    newLine.append(".")
                case "#":
                    newLine.append("#")
                    newLine.append("#")
                case "O":
                    newLine.append("[")
                    newLine.append("]")
        
        newGrid.append(newLine)
    
    return newGrid

def isMovePossible(grid, currPos, direction):
    leftMove = (currPos[0] + direction[0], currPos[1])
    rightMove = (currPos[0] + direction[0], currPos[1] + 1)

    if grid[leftMove[0]][leftMove[1]] == "#" or grid[rightMove[0]][rightMove[1]] == "#":
        return False

    if grid[leftMove[0]][leftMove[1]] == "[":
        return isMovePossible(grid, leftMove, direction)

    rightMovePossible = True if grid[rightMove[0]][rightMove[1]] == "." else isMovePossible(grid, rightMove, direction)
            

    if grid[leftMove[0]][leftMove[1]] == "]":
        leftMovePossible = isMovePossible(grid, (leftMove[0], leftMove[1] - 1), direction)

        return leftMovePossible and rightMovePossible
    
    return True

def processInstructionsDoubleWidth(grid, instructions, robotI, robotJ):
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
        
        if instruction == "<" or instruction == ">":
            moveRobot(grid, currPos, direction)
        else:
            possible = True
            
            if grid[currPos[0] + direction[0]][currPos[1]] == "[":
                possible = isMovePossible(grid, (currPos[0] + direction[0], currPos[1]), direction)
            elif grid[currPos[0] + direction[0]][currPos[1]] == "]":
                possible = isMovePossible(grid, (currPos[0] + direction[0], currPos[1] - 1), direction)
                if possible and grid[currPos[0] + direction[0]][currPos[1] + 1] == "[":
                    possible = isMovePossible(grid, (currPos[0] + direction[0], currPos[1] + 1), direction)
            
            if possible:
                moveDoubleVert(grid, (currPos[0] + direction[0], currPos[1]), direction)
                if grid[currPos[0] + direction[0]][currPos[1] + 1] == "[":
                    moveDoubleVert(grid, (currPos[0] + direction[0], currPos[1] + 1), direction)
                grid[currPos[0] + direction[0]][currPos[1]] = grid[currPos[0]][currPos[1]]
                grid[currPos[0]][currPos[1]] = "."
                
                currPos[0] += direction[0]
                currPos[1] += direction[1]

        for line in grid:
            print(line)
        print("-------------------")

def moveDoubleVert(grid, currPos, direction):
    if grid[currPos[0]][currPos[1]] == "." or grid[currPos[0]][currPos[1]] == "#":
        return
    
    if grid[currPos[0]][currPos[1]] == "]":
        moveDoubleVert(grid, (currPos[0], currPos[1] - 1), direction)
        grid[currPos[0] + direction[0]][currPos[1]] = grid[currPos[0]][currPos[1]]
        return
    
    if grid[currPos[0] + direction[0]][currPos[1]] == "[":
        moveDoubleVert(grid, (currPos[0] + direction[0], currPos[1]), direction)
        
        grid[currPos[0] + direction[0]][currPos[1]] = grid[currPos[0]][currPos[1]]
        grid[currPos[0] + direction[0]][currPos[1] + 1] = grid[currPos[0]][currPos[1] + 1]
        grid[currPos[0]][currPos[1]] = "."
        grid[currPos[0]][currPos[1] + 1] = "."
        return
    
    
    if grid[currPos[0] + direction[0]][currPos[1]] == "]":
        moveDoubleVert(grid, (currPos[0] + direction[0], currPos[1] - 1), direction)

        if grid[currPos[0] + direction[0]][currPos[1] + 1] == "[":
            moveDoubleVert(grid, (currPos[0] + direction[0], currPos[1] + 1), direction)
        
        grid[currPos[0] + direction[0]][currPos[1]] = grid[currPos[0]][currPos[1]]
        grid[currPos[0] + direction[0]][currPos[1] + 1] = grid[currPos[0]][currPos[1] + 1]
        grid[currPos[0]][currPos[1]] = "."
        grid[currPos[0]][currPos[1] + 1] = "."
        return