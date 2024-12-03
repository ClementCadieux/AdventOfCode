def readFile(path):
    file = open(path, "r")

    line = file.readline().strip()

    res = []

    while line != "":
        lineArr = line.split(" ")

        for i in range(len(lineArr)):
            lineArr[i] = int(lineArr[i])

        res.append(lineArr)

        line = file.readline().strip()

    return res

def genSubSequence(sequence):
    newSequence = []

    for i in range(1, len(sequence)):
        diff = sequence[i] - sequence[i - 1]
        newSequence.append(diff)

    return newSequence

def isAllZeroes(sequence):
    for i in sequence:
        if i != 0:
            return False
    
    return True
        
def genNextEntry(sequence, subSequence):
    lastSubVal = subSequence[-1]

    sequence.append(sequence[-1] + lastSubVal)

    return sequence

def handleSequence(sequence):
    sequenceList = [sequence]

    while not isAllZeroes(sequenceList[-1]):
        newSequence = genSubSequence(sequenceList[-1])
        sequenceList.append(newSequence)

    for i in range(len(sequenceList) - 2, -1, -1):
        sequenceList[i] = genNextEntry(sequenceList[i], sequenceList[i + 1])

    return sequenceList[0][-1]

if __name__ == "__main__":
    lines = readFile("Day9\\input.txt")

    sum = 0

    for sequence in lines:
        sum += handleSequence(sequence)

    print(sum)