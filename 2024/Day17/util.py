def readFile(path):
    file = open(path, "r")

    lines = file.readlines()

    lines = [line[:-1] if line[-1] == "\n" else line for line in lines]

    a = setRegister(lines[0])
    b = setRegister(lines[1])
    c = setRegister(lines[2])

    programLine = lines[4]

    programInstructions = programLine.split(":")[1].strip()

    program = programInstructions.split(",")

    program = [int(instruction) for instruction in program]

    return (a, b, c, program)

def setRegister(line):
    splitLine = line.split(":")

    numStr = splitLine[1].strip()

    num = int(numStr)

    return num