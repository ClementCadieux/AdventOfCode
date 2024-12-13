import time

def readFile(path):
    file = open(path, "r")

    machines = [[]]

    lines = file.readlines()

    for i in range(len(lines)):
        line = lines[i]

        if (i + 1) % 4 == 0:
            machines.append([])
        else:
            splitLine = line.split(":")

            right = splitLine[1]

            rightSplit = right.split(",")

            xVal = int(rightSplit[0].split("+" if len(machines[-1]) != 2 else "=")[1])
            yVal = int(rightSplit[1].split("+" if len(machines[-1]) != 2 else "=")[1])

            machines[-1].append((xVal, yVal))

    return machines

def calcOptPrice(machine):
    left = machine[1]
    right = machine[0]
    prize = machine[2]

    aCoef = right[0] - right[1]
    bCoef = left[0] - left[1]
    prizeSub = prize[0] - prize[1]

    prizeStep = prizeSub/aCoef
    bCoef /= aCoef

    bPress = round((prize[0] - (right[0] * prizeStep)) / (left[0] - (right[0] * bCoef)))
    aPress = round(prizeStep - (bCoef * bPress))

    if bPress * left[0] + aPress * right[0] != prize[0] or bPress * left[1] + aPress * right[1] != prize[1]:
        return 0
    
    return 3*aPress + bPress

if __name__ == "__main__":
    start = time.time()

    machines = readFile("2024\\Day13\\input.txt")

    total = 0

    for i in range(len(machines)):
        total += calcOptPrice(machines[i])
    
    print(total)

    end = time.time()

    print(end - start)