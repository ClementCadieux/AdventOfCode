def readFile(filePath):
    file = open(filePath, 'r')

    lines = file.readlines()

    outputLines = [line[:-1] if line[-1] == "\\n" else line for line in lines]

    return outputLines