import sys
from util import readFile
from main1 import sumGrid

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
                        grid[y][x] += 1
                    case "turn off":
                        if grid[y][x] > 0:
                            grid[y][x] -= 1
                    case "toggle":
                        grid[y][x] += 2
        
    gridSum = sumGrid(grid)

    print(gridSum)
        
    