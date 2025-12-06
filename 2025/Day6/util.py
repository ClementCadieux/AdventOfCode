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

def readFile2(filePath):
    file = open(filePath, 'r')

    lines = [line.strip("\n") for line in file.readlines()]

    outputLines = []

    rawOpsLine = lines[-1]

    inOps = False
    vals = ["" for _ in range(len(lines) - 1)]
    currOp = ""

    for i in range(len(rawOpsLine)):
        if rawOpsLine[i] in {"*", "+"}:
            inOps = True
            currOp = rawOpsLine[i]
        elif inOps and i != len(rawOpsLine) - 1 and rawOpsLine[i + 1] in {"*", "+"}:
            inOps = False
            outputLines.append([vals, currOp])
            vals = ["" for _ in range(len(lines) - 1)]
        
        if inOps:
            for j in range(len(vals)):
                vals[j] += lines[j][i]
    
    outputLines.append([vals, currOp])

    return outputLines

def getProblems2(lines):
    
    problems = []

    for problem in lines:
        op = problem[-1]

        nums = []

        vals = problem[0]

        for i in range(len(vals[0])):
            strNum = ""

            for j in range(len(vals)):
                strNum += vals[j][i]
            
            strNum = strNum.strip()
            num = int(strNum)

            nums.append(num)

        problems.append([nums, op])

    return problems