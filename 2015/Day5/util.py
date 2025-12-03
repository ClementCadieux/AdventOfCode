def readFile(filePath):
    file = open(filePath, 'r')

    lines = file.readlines()

    for i in range(len(lines)):
        if lines[i][-1] == "\\n":
            lines[i] = lines[i][:-1]

    return lines