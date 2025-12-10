import sys
from functools import cmp_to_key

def readFile(filePath):
    file = open(filePath, 'r')

    lines = [line.strip("\n") for line in file.readlines()]

    splitLines = [line.split(" ") for line in lines]

    sepLines = [[line[0], line[1:-1], line[-1]] for line in splitLines]

    processedLines = [[line[0].strip("[]"), [val.strip("()").split(",") for val in line[1]], line[2].strip("{}").split(",")] for line in sepLines]

    intMiddleLines = [[[1 if light == "#" else 0 for light in list(line[0])], [[int(val) for val in button] for button in line[1]], [int(val) for val in line[2]]] for line in processedLines]

    return intMiddleLines

def processButtonsBin(buttons, lightsLen):
    output = [0 for _ in buttons]

    for i in range(len(buttons)):
        button = buttons[i]
        buttonBitList = [0 for _ in range(lightsLen)]
        for light in button:
            buttonBitList[light] = 1

        binary_string = "".join(str(bit) for bit in buttonBitList)
        output[i] = int(binary_string, 2)

    return output

def processState(currState, targetState, buttons, currButtonIdx):
    if targetState == currState:
        return 0
    
    if currButtonIdx == len(buttons):
        return sys.maxsize

    currButton = buttons[currButtonIdx]
    
    valWithNext = currState ^ currButton
    
    buttonsWithNext = processState(valWithNext, targetState, buttons, currButtonIdx + 1) + 1
    buttonsWithoutNext = processState(currState, targetState, buttons, currButtonIdx + 1)

    return min(buttonsWithNext, buttonsWithoutNext)

def processJoltage(currState, buttons):
    stateSum = sum(currState)

    presses = 0

    while stateSum > 0:
        buttons = sortButtons(currState, buttons)

        nextButton = buttons[0]

        for circuit in nextButton:
            currState[circuit] -= 1

        presses += 1

        stateSum = sum(currState)

    return presses

def sortButtons(currState, buttons):
    def compare_buttons(btn1, btn2):
        vals1 = tuple(-currState[circuit] for circuit in btn1)
        vals2 = tuple(-currState[circuit] for circuit in btn2)
        
        # Compare element by element (values are negated, so lower negative = higher value)
        for v1, v2 in zip(vals1, vals2):
            if v1 != v2:
                return -1 if v1 < v2 else 1
        
        # If all compared elements are equal, prefer longer button
        if len(vals1) != len(vals2):
            return -1 if len(vals1) > len(vals2) else 1
        
        return 0

    buttons = sorted(buttons, key=cmp_to_key(compare_buttons))

    return buttons