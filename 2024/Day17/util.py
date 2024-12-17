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

def op0(a, b, c, operand):
    match operand:
        case 0:
            return a
        case 1:
            return a
        case 2:
            return int(a/4)
        case 3:
            return int(a/9)
        case 4:
            return int(a/(a**2))
        case 5:
            if b == 0:
                return a
            return int(a/(b**2))
        case 6:
            if c == 0:
                return a
            return int(a/(c**2))
    return a