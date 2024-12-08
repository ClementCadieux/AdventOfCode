def readFile(path):
    file = open(path, "r")

    lines = file.readlines()

    lines = [line[:-1] if line[-1] == "\n" else line for line in lines]

    return lines

def getAntennaLocations(lines):
    antennaLocations = {}

    for i in range(len(lines)):
        line = lines[i]
        for j in range(len(line)):
            tile = line[j]

            if tile != ".":
                if tile not in antennaLocations:
                    antennaLocations[tile] = []

                antennaLocations[tile].append((i, j))
    
    return antennaLocations