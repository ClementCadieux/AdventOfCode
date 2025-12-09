from util import readFile
import sys

def getDirections(redTiles):
    pointDirections = [[False, False, False, False] for _ in redTiles]

    for i in range(len(redTiles)):
        currPoint = redTiles[i]
        pointBefore = redTiles[i - 1]
        pointAfter = redTiles[(i + 1) % len(redTiles)]

        if currPoint[0] == pointAfter[0]:
            if currPoint[1] > pointAfter[1]:
                pointDirections[i][3] = True
            else:
                pointDirections[i][1] = True
        else:
            if currPoint[0] > pointAfter[0]:
                pointDirections[i][2] = True
            else:
                pointDirections[i][0] = True

        if currPoint[0] == pointBefore[0]:
            if currPoint[1] > pointBefore[1]:
                pointDirections[i][3] = True
            else:
                pointDirections[i][1] = True
        else:
            if currPoint[0] > pointBefore[0]:
                pointDirections[i][2] = True
            else:
                pointDirections[i][0] = True

    return pointDirections

if __name__ == "__main__":
    filePath = "2025\\Day9\\test.txt" if len(sys.argv) < 2 else sys.argv[1]

    redTiles = readFile(filePath)

    maxLine = -1
    maxCol = -1

    for tile in redTiles:
        if tile[0] > maxLine:
            maxLine = tile[0]

        if tile[1] > maxCol:
            maxCol = tile[1]

    maxArea = 0

    for i in range(len(redTiles) - 1):
        point1 = redTiles[i]
        for j in range(i + 1, len(redTiles)):
            point2 = redTiles[j]

            valid = True

            if valid:
                xDiff = abs(point1[0] - point2[0]) + 1
                yDiff = abs(point1[1] - point2[1]) + 1

                area = xDiff * yDiff

                if area > maxArea:
                    maxArea = area

    print(maxArea)