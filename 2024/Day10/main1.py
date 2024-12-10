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
    hikeTrails = [[0 for tile in line] for line in lines]

    

if __name__ == "__main__":
    lines = readFile("2024\\Day10\\test.txt")

    nines, zeroes = findNinesAndZeroes(lines)

    hikeTrails = getHikeTrails(lines, nines)

    score = 0

    for zero in zeroes:
        score += hikeTrails[zero[0]][zero[1]]

    print(score)
    