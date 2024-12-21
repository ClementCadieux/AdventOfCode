def readFile(path):
    file = open(path, "r")

    lines = file.readlines()

    lines = [line[:-1] if line[-1] == "\n" else line for line in lines]

    return lines

def codeScore(code, sequenceLength):
    numCode = int(code[:-1])

    return numCode*sequenceLength