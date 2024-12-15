import sys
import util

filePath = sys.argv[1]

grid, instruction = util.readFile(filePath)

print(grid)
print(instruction)