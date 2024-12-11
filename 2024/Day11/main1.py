def readFile(path):
    file = open(path, "r")

    line = file.readline()

    splitLine = line.split(" ")

    intLine = [int(val) for val in splitLine]

    return intLine

