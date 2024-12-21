def readFile(path):
    file = open(path, "r")

    lines = file.readlines()

    lines = [line[:-1] if line[-1] == "\n" else line for line in lines]

    return lines

def codeScore(code, sequenceLength):
    numCode = int(code[:-1])

    return numCode*sequenceLength

def arrowIndex(arrow):
    match arrow:
        case ">":
            return 0
        case "<":
            return 1
        case "^":
            return 2
        case "v":
            return 3
        case "A":
            return -1

def buildSequenceDict():
    sequencePerTile = {}    

    sequencePerTile["0"] = []

    sequencePerTile["0"].append("A")
    sequencePerTile["0"].append("^<A")
    sequencePerTile["0"].append("^A")
    sequencePerTile["0"].append("^>A")
    sequencePerTile["0"].append("^^<A")
    sequencePerTile["0"].append("^^A")
    sequencePerTile["0"].append("^^>A")
    sequencePerTile["0"].append("^^^<A")
    sequencePerTile["0"].append("^^^A")
    sequencePerTile["0"].append("^^^>A")
    sequencePerTile["0"].append(">A")

    sequencePerTile["1"] = []

    sequencePerTile["1"].append(">vA")
    sequencePerTile["1"].append("A")
    sequencePerTile["1"].append(">A")
    sequencePerTile["1"].append(">>A")
    sequencePerTile["1"].append("^A")
    sequencePerTile["1"].append("^>A")
    sequencePerTile["1"].append("^>>A")
    sequencePerTile["1"].append("^^A")
    sequencePerTile["1"].append("^^>A")
    sequencePerTile["1"].append("^^>>A")
    sequencePerTile["1"].append(">>vA")

    sequencePerTile["2"] = []

    sequencePerTile["2"].append("vA")
    sequencePerTile["2"].append("<A")
    sequencePerTile["2"].append("A")
    sequencePerTile["2"].append(">A")
    sequencePerTile["2"].append("<^A")
    sequencePerTile["2"].append("^A")
    sequencePerTile["2"].append("^>A")
    sequencePerTile["2"].append("<^^A")
    sequencePerTile["2"].append("^^A")
    sequencePerTile["2"].append("^^>A")
    sequencePerTile["2"].append("v>A")   

    sequencePerTile["3"] = []

    sequencePerTile["3"].append("<vA")
    sequencePerTile["3"].append("<<A")
    sequencePerTile["3"].append("<A")
    sequencePerTile["3"].append("A")
    sequencePerTile["3"].append("<<^A")
    sequencePerTile["3"].append("<^A")
    sequencePerTile["3"].append("^A")
    sequencePerTile["3"].append("<<^^A")
    sequencePerTile["3"].append("<^^A")
    sequencePerTile["3"].append("^^A")
    sequencePerTile["3"].append("vA")   

    sequencePerTile["4"] = []

    sequencePerTile["4"].append(">vvA")
    sequencePerTile["4"].append("vA")
    sequencePerTile["4"].append("v>A")
    sequencePerTile["4"].append("v>>A")
    sequencePerTile["4"].append("A")
    sequencePerTile["4"].append(">A")
    sequencePerTile["4"].append(">>A")
    sequencePerTile["4"].append("^A")
    sequencePerTile["4"].append("^>A")
    sequencePerTile["4"].append("^>>A")
    sequencePerTile["4"].append(">>vvA") 

    sequencePerTile["5"] = []

    sequencePerTile["5"].append("vvA")
    sequencePerTile["5"].append("<vA")
    sequencePerTile["5"].append("vA")
    sequencePerTile["5"].append("v>A")
    sequencePerTile["5"].append("<A")
    sequencePerTile["5"].append("A")
    sequencePerTile["5"].append(">A")
    sequencePerTile["5"].append("<^A")
    sequencePerTile["5"].append("^A")
    sequencePerTile["5"].append("^>A")
    sequencePerTile["5"].append("vv>A") 

    sequencePerTile["6"] = []

    sequencePerTile["6"].append("<vvA")
    sequencePerTile["6"].append("<<vA")
    sequencePerTile["6"].append("<vA")
    sequencePerTile["6"].append("vA")
    sequencePerTile["6"].append("<<A")
    sequencePerTile["6"].append("<A")
    sequencePerTile["6"].append("A")
    sequencePerTile["6"].append("<<^A")
    sequencePerTile["6"].append("<^A")
    sequencePerTile["6"].append("^A")
    sequencePerTile["6"].append("vvA")  

    sequencePerTile["7"] = []

    sequencePerTile["7"].append(">vvvA")
    sequencePerTile["7"].append("vvA")
    sequencePerTile["7"].append("vv>A")
    sequencePerTile["7"].append("vv>>A")
    sequencePerTile["7"].append("vA")
    sequencePerTile["7"].append("v>A")
    sequencePerTile["7"].append("v>>A")
    sequencePerTile["7"].append("A")
    sequencePerTile["7"].append(">A")
    sequencePerTile["7"].append(">>A")
    sequencePerTile["7"].append(">>vvvA") 

    sequencePerTile["8"] = []

    sequencePerTile["8"].append("vvvA")
    sequencePerTile["8"].append("<vvA")
    sequencePerTile["8"].append("vvA")
    sequencePerTile["8"].append("vv>A")
    sequencePerTile["8"].append("<vA")
    sequencePerTile["8"].append("vA")
    sequencePerTile["8"].append("v>A")
    sequencePerTile["8"].append("<A")
    sequencePerTile["8"].append("A")
    sequencePerTile["8"].append(">A")
    sequencePerTile["8"].append("vvv>A") 

    sequencePerTile["9"] = []

    sequencePerTile["9"].append("<vvvA")
    sequencePerTile["9"].append("<<vvA")
    sequencePerTile["9"].append("<vvA")
    sequencePerTile["9"].append("vvA")
    sequencePerTile["9"].append("<<vA")
    sequencePerTile["9"].append("<vA")
    sequencePerTile["9"].append("vA")
    sequencePerTile["9"].append("<<A")
    sequencePerTile["9"].append("<A")
    sequencePerTile["9"].append("A")
    sequencePerTile["9"].append("vvvA")

    sequencePerTile[">"] = []

    sequencePerTile[">"].append("A")
    sequencePerTile[">"].append("<<A")
    sequencePerTile[">"].append("<^A")
    sequencePerTile[">"].append("<A")
    sequencePerTile[">"].append("^A")

    sequencePerTile["<"] = []

    sequencePerTile["<"].append(">>A")
    sequencePerTile["<"].append("A")
    sequencePerTile["<"].append(">^A")
    sequencePerTile["<"].append(">A")
    sequencePerTile["<"].append(">>^A")

    sequencePerTile["^"] = []

    sequencePerTile["^"].append("v>A")
    sequencePerTile["^"].append("v<A")
    sequencePerTile["^"].append("A")
    sequencePerTile["^"].append("vA")
    sequencePerTile["^"].append(">A")

    sequencePerTile["v"] = []

    sequencePerTile["v"].append(">A")
    sequencePerTile["v"].append("<A")
    sequencePerTile["v"].append("^A")
    sequencePerTile["v"].append("A")
    sequencePerTile["v"].append("^>A")

    sequencePerTile["A"] = []

    sequencePerTile["A"].append("<A")
    sequencePerTile["A"].append("^<<A")
    sequencePerTile["A"].append("<^A")
    sequencePerTile["A"].append("^A")
    sequencePerTile["A"].append("^^<<A")
    sequencePerTile["A"].append("<^^A")
    sequencePerTile["A"].append("^^A")
    sequencePerTile["A"].append("^<<^^A")
    sequencePerTile["A"].append("<^^^A")
    sequencePerTile["A"].append("^^^A")
    
    sequencePerTile["A"].append("vA")
    sequencePerTile["A"].append("v<<A")
    sequencePerTile["A"].append("<A")
    sequencePerTile["A"].append("<vA")
    sequencePerTile["A"].append("A")
    
    return sequencePerTile

def buildNextSequence(sequence, sequenceDict, start):
    currChar = start

    result = ""

    for i in range(len(sequence)):
        nextChar = sequence[i]

        charIndex = arrowIndex(nextChar) if not nextChar.isdigit() else int(nextChar)

        if currChar == "A" and not nextChar.isdigit() and nextChar != "A":
            charIndex += 10

        result += sequenceDict[currChar][charIndex]

        currChar = nextChar
    
    return result

def buildLengthsByPairs(keyboards, sequenceDict):
    lengthsByPair = {}

    arrows = ["<", ">", "^", "v", "A"]

    for leftArrow in arrows:
        for rightArrow in arrows:
            pair = leftArrow + rightArrow
            sequence = pair

            for i in range(keyboards):
                sequence = buildNextSequence(sequence, sequenceDict, sequence[0])

            lengthsByPair[pair] = len(sequence) - 1
    
    return lengthsByPair


def main(filePath, keyboards):
    codes = readFile(filePath)

    score = 0

    sequenceDict = buildSequenceDict()
    lengthsByPair = buildLengthsByPairs(min(15, keyboards), sequenceDict)
    
    sequence = ""

    for code in codes:
        sequence = buildNextSequence(code, sequenceDict, "A")

        if keyboards > 15:
            for i in range(keyboards - 15):
                sequence = buildNextSequence(sequence, sequenceDict, "A")

        length = 0

        for i in range(len(sequence)):
            pair = ("A" if i == 0 else sequence[i - 1]) + sequence[i]

            length += lengthsByPair[pair]

        score += codeScore(code, length)
    return score