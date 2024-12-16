import sys
import util

args = sys.argv

filePath = "2024\\Day16\\test.txt" if len(args) == 1 else args[1]

lines = util.readFile(filePath)

scores = [[-1 for tile in line] for line in lines]

util.scoreTile(scores, lines, len(lines) - 2, 1, -1, -1, 1)

score = scores[-1][1]

print(score)