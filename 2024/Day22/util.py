def readFile(path):
    file = open(path, "r")

    lines = file.readlines()

    lines = [int(line) for line in lines]

    return lines