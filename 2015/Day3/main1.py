import util
import sys

def move(xPos, yPos, seen, dir):
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
    return seen, xPos, yPos


if __name__ == "__main__":
    filePath = sys.argv[1]

    line = util.readFile(filePath)

    xPos = 0
    yPos = 0

    seen = set()
    seen.add((xPos, yPos))

    for dir in line:
        seen, xPos, yPos = move(xPos, yPos, seen, dir)    

    print(len(seen))