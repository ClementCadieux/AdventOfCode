def readFile(filePath):
    file = open(filePath, 'r')

    lines = [line.strip("\n") for line in file.readlines()]

    presents = []

    linesIdx = 0

    for _ in range(6):
        linesIdx += 1

        present = []

        for i in range(linesIdx, linesIdx + 3):
            present.append(lines[i])
            linesIdx = i

        linesIdx += 2

        presents.append(present)

    return presents