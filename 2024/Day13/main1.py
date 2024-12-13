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

if __name__ == "__main__":
    machines = readFile("2024\\Day13\\test.txt")

    