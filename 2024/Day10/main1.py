lines = []

def readFile(path):
    file = open(path, "r")

    lines = [line[:-1] if line[-1] == "\n" else line for line in file.readlines()]

    splitLines = [list(line) for line in lines]

    intLines = [[int(val) for val in line] for line in splitLines]

    return intLines

def findNinesAndZeroes(lines):
    nines = []
    zeroes = []

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == 9:
                nines.append((i, j))
            elif lines[i][j] == 0:
                zeroes.append((i, j))

    return nines, zeroes

def getHikeTrails(lines, nines):
    hikeTrails = [[[] for tile in line] for line in lines]

    for i in range(len(nines)):
        nine = nines[i]
        hikeTrails[nine[0]][nine[1]].append(2 ** i)

def propagate(lines, hikeTrails, i, j, val):
    if height == 0:
        return hikeTrails

    height = lines[i][j]

    upHeight = -1 if i == 0 else lines[i - 1][j]
    upVals = [val] if i == 0 else hikeTrails[i - 1][j]

    if upHeight == height - 1 and val not in upVals:
        hikeTrails[i - 1][j].append(val)
        propagate(lines, hikeTrails, i - 1, j, val)

    downHeight = -1 if i == len(lines) - 1 else lines[i + 1][j]
    downVals = [val] if i == len(lines) - 1 else hikeTrails[i + 1][j]

    if downHeight == height - 1 and val not in downVals:
        hikeTrails[i + 1][j].append(val)
        propagate(lines, hikeTrails, i + 1, j, val)

    leftHeight = -1 if j == 0 else lines[i][j - 1]
    leftVals = [val] if j == 0 else hikeTrails[i][j - 1]

    if leftHeight == height - 1 and val not in leftVals:
        hikeTrails[i][j - 1].append(val)
        propagate(lines, hikeTrails, i, j - 1, val)

    rightHeight = -1 if j == len(lines[i]) - 1 else lines[i][j + 1]
    rightVals = [val] if j == len(lines[i]) - 1 else hikeTrails[i][j + 1]

    if rightHeight == height - 1 and val not in rightVals:
        hikeTrails[i][j + 1].append(val)
        propagate(lines, hikeTrails, i, j + 1, val)

    return hikeTrails

if __name__ == "__main__":
    lines = readFile("2024\\Day10\\test.txt")

    nines, zeroes = findNinesAndZeroes(lines)

    hikeTrails = getHikeTrails(lines, nines)

    score = 0

    for zero in zeroes:
        score += hikeTrails[zero[0]][zero[1]]

    print(score)
    