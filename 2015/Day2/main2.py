import sys
import util

filePath = sys.argv[1]

lines = util.readFile(filePath)

ribbonPerimeterPerGift = [util.getRibbonPerimeter(present) for present in lines]

totalCost = sum(ribbonPerimeterPerGift)

print(totalCost)