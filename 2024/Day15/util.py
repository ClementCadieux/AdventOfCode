def readFile(path):
    file = open(path, "r")

    lines = file.readlines()

    lines = [line[:-1] if line[-1] == "\n" else line for line in lines]

    gridTime = True

    grid = []
    instruction = ""

    for line in lines:
        if line == "":
            gridTime == False
            continue

        if gridTime:
            grid.append(list(line))
        else:
            instruction += line
        
    instruction = list(instruction)

    return grid, instruction