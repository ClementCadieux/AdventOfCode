import sys
import math

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

def circuitFrequency(buttons):
    freq = {}

    for button in buttons:
        for circuit in button:
            if circuit not in freq:
                freq[circuit] = 0
            freq[circuit] += 1

    return freq

def processJoltage(currState, buttons, targetState, cache):
    if currState in cache:
        return cache[currState]
    
    cache[currState] = sys.maxsize

    for button in buttons:
        validButton = True
        for light in button:
            if currState[light] == targetState[light]:
                validButton = False

        if validButton:
            stateWithButtonList = [currState[i] for i in range(len(currState))]
            for light in button:
                stateWithButtonList[light] += 1

            stateWithButton = tuple(stateWithButtonList)

            steps = processJoltage(stateWithButton, buttons, targetState, cache) + 1

            if steps < cache[currState]:
                cache[currState] = steps

    return cache[currState]

def sortButtons(currState, buttons):
    frequency = circuitFrequency(buttons)

    return sorted(buttons, key=lambda x: (min(frequency[c] for c in x), max(currState[c] for c in x)))      