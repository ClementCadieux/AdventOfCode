import sys
import util

args = sys.argv

filePath = "2024\\Day15\\test3.txt" if len(args) == 1 else args[1]

grid, instructions = util.readFile(filePath)

grid = util.doubleGrid(grid)

robotI, robotJ = util.findRobot(grid)

util.processInstructionsDoubleWidth(grid, instructions, robotI, robotJ)

total = util.getCoords(grid)

print(total)