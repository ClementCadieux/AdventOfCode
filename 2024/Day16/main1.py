import sys
import util
import time

args = sys.argv

filePath = "2024\\Day16\\test.txt" if len(args) == 1 else args[1]

start = time.time()

lines = util.readFile(filePath)

scores = util.scoreTiles(lines)

score = scores[1][-2]

print(score)

end = time.time()

print(end - start)