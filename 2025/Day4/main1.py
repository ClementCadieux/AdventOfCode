from util import readFile
import sys

def countAround(grid, i, j):
    surounds = 0

    for x in range(i - 1, i + 2):
        if x >= 0 and x < len(grid):
            for y in range(j - 1, j + 2):
                if y >= 0 and y < len(grid[i]):
                    if grid[x][y] == "@":
                        surounds += 1

    return surounds - 1

if __name__ == "__main__":
    filePath = "2025\\Day4\\test.txt" if len(sys.argv) < 2 else sys.argv[1]

    grid = readFile(filePath)

    total = 0

    for i in range(len(grid)):

        for j in range(len(grid[i])):
            if grid[i][j] == "@":
                if countAround(grid, i, j) < 4:
                    total += 1

    print(total)

            
