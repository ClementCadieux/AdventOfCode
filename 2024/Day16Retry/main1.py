import sys
import time
import util

args = sys.argv

filePath = "2024\\Day16Retry\\test.txt" if len(args) == 1 else args[1]

startTime = time.time()

grid = util.readFile(filePath)
