def readFile(path):
    file = open(path, "r")

    lines = file.readlines()

    lines = [line[:-1] if line[-1] == "\n" else line for line in lines]

    return lines

# make each tile a tuple with two values:
# (region tt belongs to, number of fences)

def makeRegionsNumbers(lines):
    newGrid = [[-1 for tile in line] for line in lines]

    currRegionNumber = 0

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if newGrid[i][j] == -1:
                propagateRegion(lines, newGrid, currRegionNumber, lines[i][j], i, j)
                currRegionNumber += 1
    
    return newGrid

def propagateRegion(lines, newGrid, regionNumber, regionLetter, i, j):
    if i == len(lines) - 1 or i == -1 or j == len(lines[i]) - 1 or j == -1:
        return

    if lines[i][j] != regionLetter or newGrid[i][j] != -1:
        return
    
    newGrid[i][j] = regionNumber

    propagateRegion(lines, newGrid, regionNumber, regionLetter, i - 1, j)
    propagateRegion(lines, newGrid, regionNumber, regionLetter, i + 1, j)
    propagateRegion(lines, newGrid, regionNumber, regionLetter, i, j - 1)
    propagateRegion(lines, newGrid, regionNumber, regionLetter, i, j + 1)
    
