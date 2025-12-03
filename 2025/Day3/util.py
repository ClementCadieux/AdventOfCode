def readFile(path):
    file = open(path, "r")

    banks = []

    for line in file.readlines():
        batteries = [int(battery) for battery in line[:-1]]

        banks.append(batteries)

    return banks