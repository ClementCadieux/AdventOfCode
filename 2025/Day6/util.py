def readFile(filePath):
    file = open(filePath, 'r')

    lines = [line.strip("\n") for line in file.readlines()]

    splitLines = [line.split(" ") for line in lines]

    outputLines = [[val for val in line if val] for line in splitLines]

    return outputLines

def getProblems(lines):
    problems = []

    line1 = lines[0]
    line2 = lines[1]
    line3 = lines[2]

    ops = lines[3]

    for i in range(len(line1)):
        val1 = int(line1[i])
        val2 = int(line2[i])
        val3 = int(line3[i])

        op = ops[i]

        problems.append([[val1, val2, val3], op])

    return problems