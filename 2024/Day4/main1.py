import re

def readFile(path):
    file = open(path, "r")

    lines = file.readlines()

    lines = [line[:-1] if line[-1] == "\n" else line for line in lines]

    return lines

xmas = "XMAS"
samx = "SAMX"

def findInLines(lines):
    total = 0
    for line in lines:
        total += len(re.findall(xmas, line))
        total += len(re.findall(samx, line))
    
    return total

if __name__ == "__main__":
    lines = readFile("2024\\Day4\\test.txt")

    