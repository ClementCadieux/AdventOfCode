import sys
import util

args = sys.argv

filePath = "2024\\Day18\\test.txt" if len(args) == 1 else args[1]

coordsList = util.readFile(filePath)