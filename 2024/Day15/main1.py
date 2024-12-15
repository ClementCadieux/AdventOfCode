import sys
import util

args = sys.argv

filePath = "2024\\Day15\\test1.txt" if len(args) == 1 else args[1]

grid, instructions = util.readFile(filePath)

robotI, robotJ = util.findRobot(grid)

util.processInstructionsSingleWidth(grid, instructions, robotI, robotJ)

total = util.getCoordsSingleWidth(grid)

print(total)