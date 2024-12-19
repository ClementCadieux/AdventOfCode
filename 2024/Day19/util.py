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

def possibleDesign(design, index, towelsByFirst, cache):
    if index == len(design):
        return True

    if not cache[index]:
        return False
    
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
                validDesign = possibleDesign(design, index + len(towel), towelsByFirst, cache)
        if validDesign:
            break
    
    cache[index] = validDesign

    return validDesign

def countAllDesigns(design, index, towelsByFirst, cache):
    if index == len(design):
        return 1
    
    if cache[index] != -1:
        return cache[index]
    
    cache[index] = 0

    currChar = design[index]

    lengthToEnd = len(design) - index

    towels = [] if currChar not in towelsByFirst else towelsByFirst[currChar]

    for towel in towels:
        if len(towel) <= lengthToEnd:
            valid = True
            for i in range(len(towel)):
                if towel[i] != design[index + i]:
                    valid = False
                    break
            if valid:
                cache[index] += countAllDesigns(design, index + len(towel), towelsByFirst, cache)
    
    return cache[index]