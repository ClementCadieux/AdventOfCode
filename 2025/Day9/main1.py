from util import readFile
import sys

if __name__ == "__main__":
    filePath = "2025\\Day9\\test.txt" if len(sys.argv) < 2 else sys.argv[1]

    redTiles = readFile(filePath)

    maxArea = 0

    for i in range(len(redTiles) - 1):
        point1 = redTiles[i]
        for j in range(i + 1, len(redTiles)):
            point2 = redTiles[j]

            xDiff = abs(point1[0] - point2[0]) + 1
            yDiff = abs(point1[1] - point2[1]) + 1

            area = xDiff * yDiff

            if area > maxArea:
                maxArea = area

    print(maxArea)