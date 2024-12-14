import sys

def readFile(path):
    file = open(path, "r")

    left = []
    right = []

    line = file.readline()

    while line != "":
        splitLine = line[:-1].split(" ") if line[-1] == "\n" else line.split(" ")

        left.append(int(splitLine[0]))

        right.append(int(splitLine[-1]))

        line = file.readline()

    return left,right

if __name__ == "__main__":
    filePath = sys.argv[1]
    left, right = readFile(filePath)

    left.sort()
    right.sort()

    sum = 0

    for i in range(len(left)):
        sum += abs(left[i] - right[i])

    print(sum)