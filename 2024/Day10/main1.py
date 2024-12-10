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

if __name__ == "__main__":
    lines = readFile("2024\\Day10\\test2.txt")

    