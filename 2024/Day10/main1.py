lines = []

def readFile(path):
    file = open(path, "r")

    lines = [line[:-1] if line[-1] == "\n" else line for line in file.readlines()]

    splitLines = [list(line) for line in lines]

    intLines = [[int(val) for val in line] for line in splitLines]

    return intLines

def findZeroes(lines):
    zeroSpots = []

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == 0:
                zeroSpots.append((i, j))

    return zeroSpots

def hikingScore(i, j):
    global lines
    
    val = lines[i][j]
    lines[i][j] = -1

    if val == 9:
        return 1

    up = -1 if i == 0 else lines[i - 1][j]
    down = -1 if i == len(lines) - 1 else lines[i + 1][j]
    left = -1 if j == 0 else lines[i][j - 1]
    right = -1 if j == len(lines[i]) - 1 else lines[i][j + 1]

    score = 0

    if up == val + 1:
        score += hikingScore(i - 1, j)

    if down == val + 1:
        score += hikingScore(i + 1, j)

    if left == val + 1:
        score += hikingScore(i, j - 1)

    if right == val + 1:
        score += hikingScore(i, j + 1)

    lines[i][j] = val

    return score

if __name__ == "__main__":
    lines = readFile("2024\\Day10\\test2.txt")

    zeroSpots = findZeroes(lines)

    total = 0

    for spot in zeroSpots:
        total += hikingScore(spot[0], spot[1])

    print(total)