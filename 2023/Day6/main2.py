import main1 as baseFuncs

def removeWhitespace(lines):
    newTime = ""

    for char in lines[0]:
        if char.isdigit():
            newTime += char
    
    newDist = ""

    for char in lines[1]:
        if char.isdigit():
            newDist += char

    return (int(newTime), int(newDist))

if(__name__ == "__main__"):
    lines = baseFuncs.readFile("Day6\\input.txt")

    vals = removeWhitespace(lines)

    total = baseFuncs.waysToWin(vals[0], vals[1])

    print(total)