import main1 as base

if __name__ == "__main__":
    lines = base.readFile("2024\\Day4\\input.txt")

    total = 0

    for i in range(1, len(lines) - 1):
        line = lines[i]
        prevLine = lines[i - 1]
        nextLine = lines[i + 1]
        for j in range(1, len(line) - 1):
            if line[j] == "A":
                topLeft = prevLine[j - 1]
                topRight = prevLine[j + 1]
                bottomLeft = nextLine[j - 1]
                bottomRight = nextLine[j + 1]

                posDiag = (topLeft == "M" and bottomRight == "S") or (topLeft == "S" and bottomRight == "M")
                negDiag = (topRight == "M" and bottomLeft == "S") or (topRight == "S" and bottomLeft == "M")

                if posDiag and negDiag:
                    total += 1

    print(total)