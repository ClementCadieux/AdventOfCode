def readFile(path):
    file = open(path, "r")

    lines = file.readlines()

    lines = [line[:-1] if line[-1] == "\n" else line for line in lines]

    return lines

def codeScore(code, sequenceLength):
    numCode = int(code[:-1])

    return numCode*sequenceLength

def arrowAIndex(coord):
    match coord:
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
    sequencePerTile["2"].append("^<A")
    sequencePerTile["2"].append("^A")
    sequencePerTile["2"].append("^>A")
    sequencePerTile["2"].append("^^<A")
    sequencePerTile["2"].append("^^A")
    sequencePerTile["2"].append("^^>A")
    sequencePerTile["2"].append(">vA")   

    sequencePerTile["3"] = []

    sequencePerTile["3"].append("<vA")
    sequencePerTile["3"].append("<<A")
    sequencePerTile["3"].append("<A")
    sequencePerTile["3"].append("A")
    sequencePerTile["3"].append("^<<A")
    sequencePerTile["3"].append("^<A")
    sequencePerTile["3"].append("^A")
    sequencePerTile["3"].append("^^<<A")
    sequencePerTile["3"].append("^^<A")
    sequencePerTile["3"].append("^^A")
    sequencePerTile["3"].append("vA")   

    sequencePerTile["4"] = []

    sequencePerTile["4"].append(">vvA")
    sequencePerTile["4"].append("vA")
    sequencePerTile["4"].append(">vA")
    sequencePerTile["4"].append(">>vA")
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
    sequencePerTile["5"].append(">vA")
    sequencePerTile["5"].append("<A")
    sequencePerTile["5"].append("A")
    sequencePerTile["5"].append(">A")
    sequencePerTile["5"].append("^<A")
    sequencePerTile["5"].append("^A")
    sequencePerTile["5"].append("^>A")
    sequencePerTile["5"].append(">vvA") 

    sequencePerTile["6"] = []

    sequencePerTile["6"].append("vv<A")
    sequencePerTile["6"].append("<<vA")
    sequencePerTile["6"].append("<vA")
    sequencePerTile["6"].append("vA")
    sequencePerTile["6"].append("<<A")
    sequencePerTile["6"].append("<A")
    sequencePerTile["6"].append("A")
    sequencePerTile["6"].append("^<<A")
    sequencePerTile["6"].append("^<A")
    sequencePerTile["6"].append("^A")
    sequencePerTile["6"].append("vvA")  

    sequencePerTile["7"] = []

    sequencePerTile["7"].append(">vvvA")
    sequencePerTile["7"].append("vvA")
    sequencePerTile["7"].append(">vvA")
    sequencePerTile["7"].append(">>vvA")
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
    sequencePerTile["8"].append(">vvA")
    sequencePerTile["8"].append("<vA")
    sequencePerTile["8"].append("vA")
    sequencePerTile["8"].append("v>A")
    sequencePerTile["8"].append("<A")
    sequencePerTile["8"].append("A")
    sequencePerTile["8"].append(">A")
    sequencePerTile["8"].append(">vvvA") 

    sequencePerTile["9"] = []

    sequencePerTile["9"].append("vvv<A")
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

    sequencePerTile[">"].append["A"]
    sequencePerTile[">"].append["<<A"]
    sequencePerTile[">"].append["<^A"]
    sequencePerTile[">"].append["<A"]
    sequencePerTile[">"].append["^A"]

    sequencePerTile["<"] = []

    sequencePerTile["<"].append[">>A"]
    sequencePerTile["<"].append["A"]
    sequencePerTile["<"].append[">^A"]
    sequencePerTile["<"].append[">A"]
    sequencePerTile["<"].append[">>^A"]

    sequencePerTile["^"] = []

    sequencePerTile["^"].append["v>A"]
    sequencePerTile["^"].append["v<A"]
    sequencePerTile["^"].append["A"]
    sequencePerTile["^"].append["vA"]
    sequencePerTile["^"].append[">A"]

    sequencePerTile["v"] = []

    sequencePerTile["v"].append[">A"]
    sequencePerTile["v"].append["<A"]
    sequencePerTile["v"].append["^A"]
    sequencePerTile["v"].append["A"]
    sequencePerTile["v"].append["^>A"]

    sequencePerTile["A"] = []

    sequencePerTile["A"].append("<A")
    sequencePerTile["A"].append("^<<A")
    sequencePerTile["A"].append("^<A")
    sequencePerTile["A"].append("^A")
    sequencePerTile["A"].append("^^<<A")
    sequencePerTile["A"].append("^^<A")
    sequencePerTile["A"].append("^^A")
    sequencePerTile["A"].append("^^^<<A")
    sequencePerTile["A"].append("^^^<A")
    sequencePerTile["A"].append("^^^A")
    sequencePerTile["A"].append["vA"]
    sequencePerTile["A"].append["v<<A"]
    sequencePerTile["A"].append["<A"]
    sequencePerTile["A"].append["<vA"]
    sequencePerTile["A"].append["A"]
    
    return sequencePerTile