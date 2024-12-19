def readFile(path):
    file = open(path, "r")

    lines = file.readlines()

    lines = [line[:-1] if line[:-1] == "\n" else line for line in lines]

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