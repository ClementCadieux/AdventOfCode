def readFile(path):
    file = open(path, "r")

    left = {}
    right = {}

    line = file.readline()

    while line != "":
        splitLine = line[:-1].split(" ") if line[-1] == "\n" else line.split(" ")

        if splitLine[0] not in left:
            left[splitLine[0]] = 1
        else:
            left[splitLine[0]] += 1

        if splitLine[-1] not in right:
            right[splitLine[-1]] =1
        else:
            right[splitLine[-1]] += 1

        line = file.readline()

    return left,right

if __name__ == "__main__":
    left, right = readFile("2024\\Day1\\input.txt")

    score = 0

    for num in left:
        score += left[num] * int(num) * (0 if num not in right else right[num])
    
    print(score)

