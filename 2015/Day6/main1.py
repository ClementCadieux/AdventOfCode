import sys
from util import readFile

def sumGrid(grid):
    total = 0

    for line in grid:
        total += sum(line)

    return total

if __name__ == "__main__":
    filePath = "2015\\Day6\\test.txt" if len(sys.argv) < 2 else sys.argv[1]

    instructions = readFile(filePath)

    grid = [[0 for i in range(1000)] for i in range(1000)]

    for instruction in instructions:
        mode = instruction[0]

        startX = instruction[1][0]
        startY = instruction[2][0]
        
        endX = instruction[1][1]
        endY = instruction[2][1]
        
        for x in range(startX, endX + 1):
            for y in range(startY, endY + 1):
                match mode:
                    case "turn on":
                        grid[y][x] = 1
                    case "turn off":
                        grid[y][x] = 0
                    case "toggle":
                        if grid[y][x] == 1:
                            grid[y][x] = 0
                        else:
                            grid[y][x] = 1

        
    gridSum = sumGrid(grid)

    print(gridSum)
        
    