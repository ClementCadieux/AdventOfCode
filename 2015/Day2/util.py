def readFile(path):
    file = open(path, "r")

    lines = file.readlines()

    lines = [line[:-1] if line[-1] == "\n" else line for line in lines]

    lines = [line.split("x") for line in lines]

    lines = [[int(length) for length in line] for line in lines]

    return lines