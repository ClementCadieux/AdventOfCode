import sys
import util

args = sys.argv

filePath = "2024\\Day17\\test.txt" if len(args) == 1 else args[1]

a, b, c, instructions = util.readFile(filePath)

