def readFile(filePath):
    file = open(filePath, 'r')

    lines = [line.strip("\n") for line in file.readlines()]

    splitLines = [line.split(",") for line in lines]

    numsSplit = [[int(val) for val in line] for line in splitLines]

    return numsSplit