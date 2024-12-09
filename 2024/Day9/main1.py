def readFile(path):
    file = open(path, "r")

    line = file.readline()

    return line

def genMap(line):
    lineMap = []
    for i in range(len(line)):
        charToAdd = str(int(i / 2)) if i % 2 == 0 else "."

        length = int(line[i])

        for j in range(length):
            lineMap.append(charToAdd)

    return lineMap

def compact(lineMap):
    right = len(lineMap) - 1
    left = 0

    while left < right:
        while left < right and lineMap[left] != ".":
            left += 1
        
        while right > left and lineMap[right] == ".":
            right -= 1

        if left != right:
            lineMap[left] = lineMap[right]
            lineMap[right] = "."

    return lineMap    

def checkSum(lineMap):
    total = 0

    for i in range(len(lineMap)):
        if lineMap[i] == ".":
            break

        val = int(lineMap[i])

        total += val * i

    return total

if __name__ == "__main__":
    line = readFile("2024\\Day9\\test2.txt")

    lineMap = genMap(line)

    lineMap = compact(lineMap)

    total = checkSum(lineMap)

    print(total)