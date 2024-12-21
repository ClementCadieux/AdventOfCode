import sys
import util
import time

args = sys.argv

filePath = "2024\\Day21\\test.txt" if len(args) == 1 else args[1]

startTime = time.time()

score = util.main(filePath, 25)

print(score)

endTime = time.time()

print(endTime - startTime)