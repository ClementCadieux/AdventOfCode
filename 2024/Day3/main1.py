import re

def readFile(path):
    file = open(path, "r")

    return file.readline()

def getTotal(line):
    muls = re.findall(mulExpr, line)

    total = 0

    for mul in muls:
        nums = mul[4:-1]

        numsList = nums.split(",")

        num1 = int(numsList[0])
        num2 = int(numsList[1])

        prod = num1 * num2

        total += prod
    
    return total

mulExpr = "mul\([0-9]{1,3},[0-9]{1,3}\)"

if __name__ == "__main__":
    line = readFile("2024\\Day3\\input.txt")
            
    total = getTotal(line)

    print(total)
