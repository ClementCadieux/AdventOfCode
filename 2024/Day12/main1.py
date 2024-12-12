def readFile(path):
    file = open(path, "r")

    lines = file.readlines()

    lines = [line[:-1] if line[-1] == "\n" else line for line in lines]

    return lines

# make each tile a tuple with two values:
# (region tt belongs to, number of fences)

