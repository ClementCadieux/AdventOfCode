def readFile(filePath):
    file = open(filePath, 'r')

    lines = file.readlines()

    splitLines = [line.strip("\n").split(" = ") for line in lines]

    processSplitLines = [[line[0].split(" to "), int(line[1])] for line in splitLines]

    return processSplitLines