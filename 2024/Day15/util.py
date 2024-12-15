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

