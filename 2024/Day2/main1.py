def readFile(path):
    file = open(path, "r")

    reports = []

    line = file.readline()

    while line != "":
        lineSplit = line[:-1].split(" ") if line[-1] == "\n" else line.split(" ")

        intLine = [int(x) for x in lineSplit]

        reports.append(intLine)

        line = file.readline()

    return reports

def evalLine(line):
    dir = 1 if line[1] > line[0]  else -1 if line[1] < line[0] else 0

    if dir == 0:
        return False
    
    for i in range(1, len(line)):
        diffCheck = (line[i] - line[i - 1]) * dir

        if (diffCheck) > 3:
            return False
        
        if line[i] == line[i - 1]:
            return False
        
        if line[i] < line[i - 1] and dir == 1:
            return False
        
        if line[i] > line[i - 1] and dir == -1:
            return False
        
    return True

def getValidLines(reports):
    total = 0

    for line in reports:
        if evalLine(line):
            total += 1

    return total

if __name__ == "__main__":
    reports = readFile("2024\\Day2\\input.txt")

    total = getValidLines(reports)

    print(total)