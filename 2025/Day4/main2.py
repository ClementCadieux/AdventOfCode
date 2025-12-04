from util import readFile
import sys
from main1 import groupThree, countAround

def removePaper(newGrid, i, j):
    newGrid[i][j] -= 1
    if j > 0:
        newGrid[i][j - 1] -= 1
    if j < len(grid[i]) - 1:
        newGrid[i][j + 1] -= 1

    return newGrid

if __name__ == "__main__":
    filePath = "2025\\Day4\\test.txt" if len(sys.argv) < 2 else sys.argv[1]

    grid = readFile(filePath)

    newGrid = [[groupThree(grid, i, j) for j in range(len(grid[i]))] for i in range(len(grid))]

    passSwaps = 1

    total = 0

    while passSwaps > 0:
        passSwaps = 0
        
        for i in range(len(newGrid)):
            for j in range(len(newGrid[i])):
                if grid[i][j] == "@":
                    countRolls = countAround(newGrid, i, j)

                    if countRolls < 4:
                        grid[i] = grid[i][:j] + "x" + grid[i][j + 1:]
                        newGrid = removePaper(newGrid, i, j)
                        passSwaps += 1
                        total += 1

    print(total)