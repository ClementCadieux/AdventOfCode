import sys
import util
import time

args = sys.argv

filePath = "2024\\Day16\\test3.txt" if len(args) == 1 else args[1]

start = time.time()

lines = util.readFile(filePath)

scores = util.scoreTiles(lines)

finalScore = scores[-2][1]

end = time.time()

print(end - start)