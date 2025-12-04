def readFile(filePath):
    file = open(filePath, 'r')

    circuit = {}

    for line in file.readlines():
        splitLine = line.split("->")

        input = splitLine[0].strip()
        output = splitLine[1].strip()

        splitInput = input.split(" ")

        circuit[output] = splitInput
        
    return circuit