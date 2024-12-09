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

if __name__ == "__main__":
    print("")