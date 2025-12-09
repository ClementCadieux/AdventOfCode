from util import readFile
import sys

def getMinMaxPoints(redTiles, maxLine, maxCol):
    minMaxRedPointLines = [[-1, -1] for _ in range(maxLine + 1)]
    minMaxRedPointCols = [[-1, -1] for _ in range(maxCol + 1)]

    for tile in redTiles:
        line = tile[0]
        col = tile[1]

        if minMaxRedPointCols[col][0] == -1 or minMaxRedPointCols[col][0] > line:
            minMaxRedPointCols[col][0] = line
        
        if minMaxRedPointCols[col][1] == -1 or minMaxRedPointCols[col][1] < line:
            minMaxRedPointCols[col][1] = line

        if minMaxRedPointLines[line][0] == -1 or minMaxRedPointLines[line][0] > col:
            minMaxRedPointLines[line][0] = col
        
        if minMaxRedPointLines[line][1] == -1 or minMaxRedPointLines[line][1] < col:
            minMaxRedPointLines[line][1] = col

    return minMaxRedPointLines, minMaxRedPointCols

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

    minMaxRedPointLines, minMaxRedPointCols = getMinMaxPoints(redTiles, maxLine, maxCol)

    maxArea = 0

    for i in range(len(redTiles) - 1):
        point1 = redTiles[i]
        for j in range(i + 1, len(redTiles)):
            point2 = redTiles[j]

            valid = True

            if point1[0] < minMaxRedPointCols[point2[1]][0] or point1[0] > minMaxRedPointCols[point2[1]][1]:
                valid = False
            elif point1[1] < minMaxRedPointLines[point2[0]][0] or point1[1] > minMaxRedPointLines[point2[0]][1]:
                valid = False
            elif point2[0] < minMaxRedPointCols[point1[1]][0] or point2[0] > minMaxRedPointCols[point1[1]][1]:
                valid = False
            elif point2[1] < minMaxRedPointLines[point1[0]][0] or point2[1] > minMaxRedPointLines[point1[0]][1]:
                valid = False

            if valid:
                xDiff = abs(point1[0] - point2[0]) + 1
                yDiff = abs(point1[1] - point2[1]) + 1

                area = xDiff * yDiff

                if area > maxArea:
                    maxArea = area

    print(maxArea)