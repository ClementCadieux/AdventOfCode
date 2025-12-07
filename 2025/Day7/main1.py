from util import readFile
import sys

seen = set()

def processBeam(grid, startI, startJ):
    i = startI + 1
    j = startJ

    if j == -1 or j == len(grid[i]):
        return 0

    while i < len(grid) and grid[i][j] != '^':
        i += 1
    
    if (i, j) in seen:
        return 0

    seen.add((i, j))

    if i == len(grid):
        return 0
    
    leftSplit = processBeam(grid, i, j - 1)
    rightSplit = processBeam(grid, i, j + 1)

    return leftSplit + rightSplit + 1

if __name__ == "__main__":
    filePath = "2025\\Day7\\test.txt" if len(sys.argv) < 2 else sys.argv[1]

    beamPoint, grid = readFile(filePath)

    total = processBeam(grid, beamPoint[0], beamPoint[1])

    print(total)