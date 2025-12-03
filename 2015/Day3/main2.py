import util
import sys
from main1 import move

if __name__ == "__main__":
    filePath = sys.argv[1]

    line = util.readFile(filePath)

    santaX = 0
    santaY = 0
    robotX = 0
    robotY = 0

    seen = set()
    seen.add((0, 0))

    for i in range(len(line)):
        if i % 2 == 0:
            seen, santaX, santaY = move(santaX, santaY, seen, line[i])
        else:
            seen, robotX, robotY = move(robotX, robotY, seen, line[i])

    print(len(seen))