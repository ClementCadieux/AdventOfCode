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

