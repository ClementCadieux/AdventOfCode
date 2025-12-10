import sys

def readFile(filePath):
    file = open(filePath, 'r')

    lines = [line.strip("\n") for line in file.readlines()]

    splitLines = [line.split(" ") for line in lines]

    sepLines = [[line[0], line[1:-1], line[-1]] for line in splitLines]

    processedLines = [[line[0].strip("[]"), [val.strip("()").split(",") for val in line[1]], line[2].strip("{}").split(",")] for line in sepLines]

    intMiddleLines = [[line[0], [[int(val) for val in button] for button in line[1]], [int(val) for val in line[2]]] for line in processedLines]

    return intMiddleLines

def processMachineState(machine, cache, currState, lastButton):
    if currState == machine[0]:
        return 0
    
    if "#" not in currState and lastButton != -1:
        return sys.maxsize

    if currState in cache:
        return cache[currState]
    
    cache[currState] = sys.maxsize

    for i in range(len(machine[1])):
        if i != lastButton:
            button = machine[1][i]
            newState = processButton(currState, button)

            iterationsFromHere = processMachineState(machine, cache, newState, i)  + 1

            if iterationsFromHere < cache[currState]:
                cache[currState] = min  

    return cache[currState]

def processButton(currState, button):
    for light in button:
        newChar = "."
        if currState[light] == ".":
            newChar = "#"

        currState = currState[:light] + newChar + currState[light + 1:]

    return currState  