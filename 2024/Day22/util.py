def readFile(path):
    file = open(path, "r")

    lines = file.readlines()

    lines = [int(line) for line in lines]

    return lines

def calcNumPart1(num):
    mixVal = num*64
    num = num^mixVal
    num %= 16777216

    mixVal = int(num/32)
    num = num^mixVal
    num %= 16777216

    mixVal = num*2048
    num = num^mixVal
    num %= 16777216

    return num

def getChangeSequence(priceSequence):
    changeSequence = []
    
    for i in range(1, len(priceSequence)):
        change = priceSequence[i] % 10 - priceSequence[i - 1] % 10

        changeSequence.append(change)

    strChangeSequence = str(changeSequence)

    return strChangeSequence[1:-1]

def keepChangeSequence(num, priceSequence, changeSequenceDict):
    num = calcNumPart1(num)

    priceSequence.append(num)

    if len(priceSequence) > 5:
        priceSequence.pop(0)

    changeSequence = getChangeSequence(priceSequence)

    if changeSequence not in changeSequenceDict and len(changeSequence.split(",")) == 4:
        changeSequenceDict[changeSequence] = priceSequence[-1]%10

    return (num,priceSequence,changeSequenceDict)
