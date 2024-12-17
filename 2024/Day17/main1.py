import sys
import util

args = sys.argv

filePath = "2024\\Day17\\test.txt" if len(args) == 1 else args[1]

a, b, c, instructions = util.readFile(filePath)

pointer = 0

while pointer < len(instructions) - 1:
    print(pointer)
    operation = instructions[pointer]
    operand = instructions[pointer + 1]

    match operation:
        case 0:
            a = util.op067(a, b, c, operand)
            pointer += 2
        case 1:
            b = util.op1(b, operand)
            pointer += 2
        case 2:
            b = util.op2(a, b, c, operand)
            pointer += 2
        case 3:
            pointer, jumped = util.op3(a, operand, pointer)
            if not jumped:
                pointer += 2
        case 4:
            b = util.op4(b, c)
            pointer += 2
        case 5:
            util.op5(a, b, c, operand)
            pointer += 2
        case 6:
            b = util.op067(a, b, c, operand)
            pointer += 2
        case 7:
            c = util.op067(a, b, c, operand)
            pointer += 2

print(util.outputLine)