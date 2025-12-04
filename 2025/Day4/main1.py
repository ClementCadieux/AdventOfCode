from util import readFile
import sys

def countAround(grid, i, j):
    line = grid[i]

    total = 0

    for x in range(j - 1, j + 2):
        if x >= 0 and x < len(line):
            if line[x] == "@":
                total += 1

    return total

if __name__ == "__main__":
    filePath = "2025\\Day4\\test.txt" if len(sys.argv) < 2 else sys.argv[1]

    grid = readFile(filePath)

    newGrid = [[countAround(grid, i, j) for j in range(len(grid[i]))] for i in range(len(grid))]

    total = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "@":
                up = 0 if i == 0 else newGrid[i - 1][j]
                middle = newGrid[i][j] - 1
                down = 0 if i == len(grid) - 1 else newGrid[i + 1][j]

                countRolls = up + middle + down
                
                if countRolls < 4:
                    total += 1

    print(total)

            
