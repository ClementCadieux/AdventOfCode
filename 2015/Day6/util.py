def readFile(path):
    file = open(path, 'r')

    outputLines = []

    for line in file.readlines():
        words = line.split(" ")

        instruction = words[0]

        idxDelay = 0

        if instruction == "turn":
            instruction += " " + words[1]
            idxDelay = 1

        startPos = words[1 + idxDelay]

        splitStart = startPos.split(",")
        startX = int(splitStart[0])
        startY = int(splitStart[1])

        endPos = words[3 + idxDelay]

        splitEnd = endPos.split(",")
        endX = int(splitEnd[0])
        endY = int(splitEnd[1])

        insLine = (instruction, [startX, endX], [startY, endY])

        outputLines.append(insLine)
    
    return outputLines
