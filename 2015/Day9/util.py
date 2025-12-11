def readFile(filePath):
    file = open(filePath, 'r')

    lines = file.readlines()

    splitLines = [line.strip("\n").split(" = ") for line in lines]

    processSplitLines = [[line[0].split(" to "), int(line[1])] for line in splitLines]

    resultDistance = {}

    for line in processSplitLines:
        city1 = line[0][0]
        city2 = line[0][1]
        distance = line[1]

        city1Distances = [] if city1 not in resultDistance else resultDistance[city1]
        city2Distances = [] if city2 not in resultDistance else resultDistance[city2]

        city1Distances.append([city2, distance])
        city2Distances.append([city1, distance])

        resultDistance[city1] = city1Distances
        resultDistance[city2] = city2Distances

    return resultDistance