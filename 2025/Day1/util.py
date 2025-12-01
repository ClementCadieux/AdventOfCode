def readFile(path):
    file = open(path, "r")

    rotations = []

    for line in file.readlines():
        dir = line[0]
        num = int(line[1:])

        polarity = -1 if dir == 'L' else 1

        val = num * polarity

        rotations.append(val)
    
    return rotations