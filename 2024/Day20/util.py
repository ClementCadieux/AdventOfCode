def readFile(path):
    file = open(path,"r")

    lines = file.readlines()

    lines = [line[:-1] if line[-1] == "\n" else line for line in lines]

    grid = [list(line) for line in lines]

    return grid

def findStartAndEnd(grid):
    startI = -1
    startJ = -1

    endI = -1
    endJ = -1

    foundStart = False
    foundEnd = False

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "S":
                foundStart = True
                startI = i
                startJ = j
            elif grid[i][j] == "E":
                foundEnd = True
                endI = i
                endJ = j
            
            if foundStart and foundEnd:
                break
        if foundStart and foundEnd:
            break
    
    return ((startI, startJ), (endI, endJ))