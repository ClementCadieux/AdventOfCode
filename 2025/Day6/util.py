def readFile(filePath):
    file = open(filePath, 'r')

    lines = [line.strip("\n") for line in file.readlines()]

    splitLines = [line.split(" ") for line in lines]

    outputLines = [[val for val in line if val] for line in splitLines]

    return outputLines

def getProblems(lines):
    problems = []

    ops = lines[-1]

    for i in range(len(ops)):
        nums = []

        for j in range(len(lines) - 1):
            nums.append(int(lines[j][i]))

        op = ops[i]

        problems.append([nums, op])

    return problems