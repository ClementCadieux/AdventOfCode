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

