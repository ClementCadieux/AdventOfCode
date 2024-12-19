def readFile(path):
    file = open(path, "r")

    lines = file.readlines()

    lines = [line[:-1] if line[-1] == "\n" else line for line in lines]

    towelsLine = lines[0]

    splitTowelsLine = towelsLine.split(",")

    splitTowelsLine = [towel.strip() for towel in splitTowelsLine]

    towelsByFirst = {}

    for towel in splitTowelsLine:
        first = towel[0]

        if first not in towelsByFirst:
            towelsByFirst[first] = []

        towelsByFirst[first].append(towel)
    
    designs = []

    for i in range(2, len(lines)):
        designs.append(lines[i])

    return towelsByFirst, designs

def possibleDesign(design, index, towelsByFirst):
    if index == len(design):
        return True
    
    currChar = design[index]

    lengthToEnd = len(design) - index

    towels = [] if currChar not in towelsByFirst else towelsByFirst[currChar]

    validDesign = False

    for towel in towels:
        if len(towel) <= lengthToEnd:
            valid = True
            for i in range(len(towel)):
                if towel[i] != design[index + i]:
                    valid = False
                    break
            if valid:
                validDesign = possibleDesign(design, index + len(towel), towelsByFirst)
        if validDesign:
            break

    return validDesign