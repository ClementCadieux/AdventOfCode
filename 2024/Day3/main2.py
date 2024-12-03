import main1 as base
import re

if __name__ == "__main__":
    line = base.readFile("2024\\Day3\\input.txt")

    doExpr = "do\(\)"
    dontExpr = "don't\(\)"

    total = 0

    lineSplit = re.split(doExpr, line)

    for subLine in lineSplit:
        dontMatch = re.search(dontExpr, subLine)

        doLine = subLine if dontMatch is None else subLine[:dontMatch.start()]

        total += base.getTotal(doLine)
    
    print(total)





    