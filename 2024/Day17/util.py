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

outputLine = ""

def comboOperand(a, b, c, operand):
    match operand:
        case 4:
            return a
        case 5:
            return b
        case 6:
            return c
        case _:
            return operand

def op067(a, b, c, operand):
    denominator = comboOperand(a, b, c, operand) ** 2

    if denominator != 0:
        return int(a/denominator)

    return a

def op1(b, operand):
    return b | operand

def op2(a, b, c, operand):
    numerator = comboOperand(a, b, c, operand)

    return numerator % 8

def op3(a, operand, pointer):
    if a == 0:
        return pointer, False
    
    return operand, True

def op4(b, c):
    return b % c

def op5(a, b, c, operand):
    global outputLine
    output = op2(a, b, c, operand)

    if len(outputLine) != 0:
        outputLine += ","
    outputLine += str(output)