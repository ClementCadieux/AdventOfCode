def readFile(path):
    file = open(path, "r")

    line = file.readline()

    return line

def genMap(line):
    lineMap = ""
    for i in range(len(line)):
        charToAdd = str(int(i / 2)) if i % 2 == 0 else "."

        length = int(line[i])

        for j in range(length):
            lineMap += charToAdd

    return lineMap

if __name__ == "__main__":
    print("")