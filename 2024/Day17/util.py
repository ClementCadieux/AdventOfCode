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

outputLine = []

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
    power = comboOperand(a, b, c, operand)

    return int(a/(2**power))

def op1(b, operand):
    return b ^ operand

def op2(a, b, c, operand):
    numerator = comboOperand(a, b, c, operand)

    return numerator % 8

def op3(a, operand, pointer):
    if a == 0:
        return pointer, False
    
    return operand, True

def op4(b, c):
    return b ^ c

def op5(a, b, c, operand):
    global outputLine
    output = op2(a, b, c, operand)

    outputLine.append(output)

def processIntrusctions(a, b, c, instructions):
    pointer = 0

    while pointer < len(instructions) - 1:
        operation = instructions[pointer]
        operand = instructions[pointer + 1]

        a, b, c, pointer = processOp(a, b, c, pointer, operation, operand)

def processOp(a, b, c, pointer, operation, operand):
    match operation:
        case 0:
            a = op067(a, b, c, operand)
            pointer += 2
        case 1:
            b = op1(b, operand)
            pointer += 2
        case 2:
            b = op2(a, b, c, operand)
            pointer += 2
        case 3:
            pointer, jumped = op3(a, operand, pointer)
            if not jumped:
                pointer += 2
        case 4:
            b = op4(b, c)
            pointer += 2
        case 5:
            op5(a, b, c, operand)
            pointer += 2
        case 6:
            b = op067(a, b, c, operand)
            pointer += 2
        case 7:
            c = op067(a, b, c, operand)
            pointer += 2
    
    return (a, b, c, pointer)

def splitInstructions(instructions):
    instructionsList = []
    
    for i in range(len(instructions) - 1):
        instruction = [instructions[i], instructions[i + 1]]

        instructionsList.append(instruction)
        i += 1
    
    return instructionsList

def processSequence(a, splitCommands):
    a = a
    b = 0
    c = 0

    for command in splitCommands:
        a, b, c, pointer = processOp(a, b, c, 0, command[0], command[1])
    
    return outputLine[-1], a