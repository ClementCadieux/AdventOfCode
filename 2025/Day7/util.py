def readFile(filePath):
    file = open(filePath, 'r')

    lines = [line.strip("\n") for line in file.readlines()]

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            curr = lines[i][j]

            if curr == 'S':
                return (i, j), lines 