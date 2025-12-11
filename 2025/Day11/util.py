from copy import deepcopy

def readFile(filePath):
    file = open(filePath, 'r')

    lines = [line.strip("\n") for line in file.readlines()]

    splitLines = [line.split(":") for line in lines]

    splitLinesTarget = [[line[0], line[1].strip().split(" ")] for line in splitLines]

    circuitDict = {}

    for line in splitLinesTarget:
        circuitDict[line[0]] = line[1]

    return circuitDict

def pathsToOut(circuit, cache, machine):
    if machine not in cache:
        cache[machine] = 0

        outputs = circuit[machine]

        for output in outputs:
            cache[machine] += pathsToOut(circuit, cache, output)
    
    return cache[machine]

def pathsToOut2(circuit, cache, machine):
    if machine not in cache:
        cache[machine] = []

        outputs = circuit[machine]

        for output in outputs:
            pathsFromOutput = deepcopy(pathsToOut2(circuit, cache, output))

            for path in pathsFromOutput:
                path.add(output)
            
            cache[machine].extend(pathsFromOutput)
    
    return cache[machine]