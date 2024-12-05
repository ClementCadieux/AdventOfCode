def readFile(path):
    file = open(path, "r")

    rules = [set() for x in range(100)]

    line = file.readline()

    while line != "\n":
        lineSplit = line[:-1].split("|")

        num1 = int(lineSplit[0])
        num2 = int(lineSplit[1])

        rules[num1].add(num2)

        line = file.readline()

    prints = []
    line = file.readline()

    while line != "":
        lineSplit = line[:-1].split(",") if line[-1] == "\n" else line.split(",")

        lineArr = [int(x) for x in lineSplit]

        prints.append(lineArr)

        line = file.readline()
    
    return rules, prints

def validatePrint(printLine, rules):
    seen = set()

    for num in printLine:
        rule = rules[num]

        if len(seen) > 0:
            toLoop, toCheck = (seen, rule) if len(seen) <= len(rule) else (rule, seen)

            for n in toLoop:
                if n in toCheck:
                    return False
            
        seen.add(num)
    
    return True

if __name__ == "__main__":
    rules, prints = readFile("2024\\Day5\\input.txt")

    total = 0

    for printLine in prints:
        if validatePrint(printLine, rules):
            middle = int(len(printLine) / 2)
            total += printLine[middle]

    print(total)