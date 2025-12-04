def readFile(filePath):
    file = open(filePath, 'r')

    lines = file.readlines()

    outputLines = [line.strip("\n") for line in lines]

    return outputLines