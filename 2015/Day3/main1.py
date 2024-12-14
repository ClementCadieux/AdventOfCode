import util
import sys

filePath = sys.argv[1]

line = util.readFile(filePath)

xPos = 0
yPos = 0

seen = set()
seen.add((xPos, yPos))

for dir in line:
    match dir:
        case '>':
            xPos += 1
        case '<':
            xPos -= 1
        case '^':
            yPos -= 1
        case 'v':
            yPos += 1
    seen.add((xPos, yPos))

print(len(seen))