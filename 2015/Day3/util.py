def readFile(path):
    file = open(path, "r")

    line = file.readline()

    return list(line)