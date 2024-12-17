import sys
import util

args = sys.argv

filePath = "2024\\Day17\\test2.txt" if len(args) == 1 else args[1]

a, b, c, instructions = util.readFile(filePath)

splitCommands = util.splitInstructions(instructions)

currOutputIndex = len(instructions) - 1

aDivideFactor = util.aDivideFactor(splitCommands)

result = util.reverseEngineer(instructions, splitCommands, currOutputIndex, 0, aDivideFactor)

print(result)