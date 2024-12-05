import main1 as base

def reorderLine(line, rules):
    befInLine = getBefInLine(line, rules)

    line.sort(key=lambda x : befInLine[x])

    return line

def getBefInLine(line, rules):
    befInLine = {}

    inLine = set(line)

    for num in line:
        rule = rules[num]

        befInLine[num] = set()

        for n in rule:
            if n in inLine:
                befInLine[num].add(n)

    return befInLine

if __name__ == "__main__":
    rules, prints = base.readFile("2024\\Day5\\input.txt")

    invalidLines = [line for line in prints if not base.validatePrint(line, rules)]

    total = 0

    for line in invalidLines:
        orderedLine = reorderLine(line, rules)
        total += base.getMiddle(orderedLine)

    print(total)
