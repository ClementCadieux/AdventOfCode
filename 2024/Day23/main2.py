import sys
import util
import time

args = sys.argv

filePath = "2024\\Day23\\test.txt" if len(args) == 1 else args[1]

startTime = time.time()

connections = util.readFile(filePath)

