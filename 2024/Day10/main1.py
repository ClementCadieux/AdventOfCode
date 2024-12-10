lines = []

def readFile(path):
    file = open(path, "r")

    lines = [line[:-1] if line[-1] == "\n" else line for line in file.readlines()]

    splitLines = [list(line) for line in lines]

    intLines = [[int(val) for val in line] for line in splitLines]

    return intLines

def findNines(lines):
    nines = []

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == 9:
                nines.append(i, j)

    return nines

def getHikeTrails(lines):
    hikeTrails = [[0 for tile in line] for line in lines]

    

if __name__ == "__main__":
    lines = readFile("2024\\Day10\\test.txt")

    