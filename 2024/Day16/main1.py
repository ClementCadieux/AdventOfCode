import sys
import util

args = sys.argv

filePath = "2024\\Day16\\test3.txt" if len(args) == 1 else args[1]

lines = util.readFile(filePath)

scores = [[0 for tile in line] for line in lines]
seen = set()

if lines[2][-2] != "#":
    util.scoreTile(scores, lines, 2, len(lines[1]) - 2, 1, 0, seen)
if lines[1][-3] != "#":
    util.scoreTile(scores, lines, 1, len(lines[1]) - 2, 0, 1, seen)

score = scores[-2][1]

print(score)