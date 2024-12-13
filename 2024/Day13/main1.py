def readFile(path):
    file = open(path, "r")

    machines = [[]]

    lines = file.readlines()

    for i in range(len(lines)):
        line = lines[i]

        if i != 0 and i % 3 == 0:
            machines.append([])
        else:
            splitLine = line.split(":")

            right = splitLine[1]

            rightSplit = right.split(",")
            xVal = int(rightSplit[0].split("+")[1])
            yVal = int(rightSplit[1].split("+")[1])

            machines[-1].append((xVal, yVal))

    return machines