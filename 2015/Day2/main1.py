import sys
import util

filePath = sys.argv[1]

lines = util.readFile(filePath)

areasPerGift = [util.getAreas(present) for present in lines]

costPerGift = [util.getCost(present) for present in areasPerGift]

totalCost = sum(costPerGift)

print(totalCost)