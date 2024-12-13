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

def calcOptMachine(machine):
    right = machine[0]
    left = machine[1]
    prize = machine[2]

    optPrice = -1

    for i in range(100, -1, -1):
        startPos = (left[0] * i, left[1] * i)

        xToGo = prize[0] - startPos[0]
        yToGo = prize[1] - startPos[1]

        rightXPossible = xToGo % right[0] == 0

        if not rightXPossible:
            continue

        rightXPushes = int(xToGo / right[0])

        if rightXPushes > 100:
            continue

        yRightMove = rightXPushes * right[1]

        if yRightMove != yToGo:
            continue

        price = 3 * rightXPushes + i

        if optPrice == -1 or price < optPrice:
            optPrice = price
        elif optPrice != -1 and price > optPrice:
            break

    return optPrice if optPrice != -1 else 0

if __name__ == "__main__":
    machines = readFile("2024\\Day13\\input.txt")

    total = 0

    for i in range(len(machines)):
        total += calcOptMachine(machines[i])
    
    print(total)