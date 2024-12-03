import main1 as baseFuncts

def genFirstValue(sequence, subSequence):
    firstVal = subSequence[0]

    newVal = sequence[0] - firstVal

    sequence.insert(0, newVal)

    return sequence

def handleSequence(sequence):
    sequenceList = [sequence]

    while not baseFuncts.isAllZeroes(sequenceList[-1]):
        newSequence = baseFuncts.genSubSequence(sequenceList[-1])
        sequenceList.append(newSequence)

    for i in range(len(sequenceList) - 2, -1, -1):
        sequenceList[i] = genFirstValue(sequenceList[i], sequenceList[i + 1])

    return sequenceList[0][0]


if __name__ == "__main__":
    lines = baseFuncts.readFile("Day9\\input.txt")

    sum = 0

    for line in lines:
        sum += handleSequence(line)

    print(sum)
