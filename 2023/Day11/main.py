def readFile(path):
    file = open(path, "r")

    grid = []

    line = file.readline()

    while line != "":
        if line[-1] == "\n":
            line = line[:-1]

        grid.append(list(line))

        line = file.readline()

    return grid    

def findGalaxies(grid):
    galaxies = []
    occupiedRows = set()
    occupiedCols = set()

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "#":
                galaxies.append((i,j))

                occupiedRows.add(i)
                occupiedCols.add(j)

    return (galaxies, occupiedRows, occupiedCols)

def rollingEmpty(grid, occupiedRows, occupiedCols):
    emptyRowRollingCount = []
    emptyColRollingCount = []

    emptyRowCount = 0

    for i in range(len(grid)):
        emptyRowRollingCount.append(emptyRowCount)
        if i not in occupiedRows:
            emptyRowCount += 1

    emptyColCount = 0

    for i in range(len(grid[0])):
        emptyColRollingCount.append(emptyColCount)

        if i not in occupiedCols:
            emptyColCount += 1

    return (emptyRowRollingCount, emptyColRollingCount)

def updateGalaxies(galaxies, rollingRowsCount, rollingColsCount, factor):
    for i in range(len(galaxies)):
        galaxy = galaxies[i]

        newGal = galaxy[0] + rollingRowsCount[galaxy[0]] * (factor - 1), galaxy[1] + rollingColsCount[galaxy[1]] * (factor - 1)

        galaxies[i] = newGal

def getDistance(galaxy1, galaxy2):
    return abs(galaxy2[1] - galaxy1[1]) + abs(galaxy2[0] - galaxy1[0])

def getTotalDistance(galaxies):
    total = 0

    for i in range(len(galaxies) - 1):
        for j in range(i + 1, len(galaxies)):
            total += getDistance(galaxies[i], galaxies[j])

    return total

if __name__ == "__main__":
    grid = readFile("Day11\\input.txt")

    galaxiesAnalysis = findGalaxies(grid)

    galaxies = galaxiesAnalysis[0]
    occupiedRows = galaxiesAnalysis[1]
    occupiedCols = galaxiesAnalysis[2]

    emptyRollingCounts = rollingEmpty(grid, occupiedRows, occupiedCols)

    rollingRowsCount = emptyRollingCounts[0]
    rollingColsCount = emptyRollingCounts[1]

    updateGalaxies(galaxies, rollingRowsCount, rollingColsCount, 1000000)

    distance = getTotalDistance(galaxies)

    print(distance)


