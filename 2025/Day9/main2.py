from util import readFile
import sys

def getGrid(redTiles):
    grid = [[0 for _ in range(maxCol + 1)] for _ in range(maxLine + 1)]

    for i in range(len(redTiles)):
        currPoint = redTiles[i]
        pointAfter = redTiles[(i + 1) % len(redTiles)]

        if currPoint[0] == pointAfter[0]:
            if currPoint[1] > pointAfter[1]:
                x = currPoint[0]
                for y in range(pointAfter[1], currPoint[1] + 1):
                    grid[x][y] = 1
            else:
                x = currPoint[0]
                for y in range(currPoint[1], pointAfter[1] + 1):
                    grid[x][y] = 1
        else:
            if currPoint[0] > pointAfter[0]:
                y = currPoint[1]
                for x in range(pointAfter[0], currPoint[0] + 1):
                    grid[x][y] = 1
            else:
                y = currPoint[1]
                for x in range(currPoint[0], pointAfter[0] + 1):
                    grid[x][y] = 1

    return grid

def checkValid(grid, point1, point2):
    return False

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

    grid = getGrid(redTiles)

    maxArea = 0

    for i in range(len(redTiles) - 1):
        point1 = redTiles[i]
        for j in range(i + 1, len(redTiles)):
            point2 = redTiles[j]
            
            xDiff = abs(point1[0] - point2[0]) + 1
            yDiff = abs(point1[1] - point2[1]) + 1

            area = xDiff * yDiff

            if area > maxArea:
                if checkValid(grid, point1, point2):
                    maxArea = area

    print(maxArea)