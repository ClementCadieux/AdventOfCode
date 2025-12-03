def readFile(path):
    file = open(path, "r")

    banks = []

    lines = file.readlines()

    for i in range(len(lines)):
        line = lines[i]

        if i != len(lines) - 1:
            line = line[:-1]
        
        batteries = [int(battery) for battery in line]

        banks.append(batteries)

    return banks