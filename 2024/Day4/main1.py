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

def buildVertical(lines):
    verticalLines = []

    for i in range(len(lines)):
        line = lines[i]

        for j in range(len(line)):
            if i == 0:
                verticalLines.append(line[j])
            else:
                verticalLines[j] += line[j]
            
    return verticalLines

def buildPosDiag(lines):
    diagGrid = []

    startIdx = 0

    for line in lines:
        for i in range(len(line)):
            if startIdx + i == len(diagGrid):
                diagGrid.append(line[i])
            else:
                diagGrid[startIdx + i] += line[i]
        
        startIdx += 1
    
    return diagGrid

if __name__ == "__main__":
    lines = readFile("2024\\Day4\\test.txt")

    horizontalTotal = findInLines(lines)

    vertical = buildVertical(lines)

    verticalTotal = findInLines(vertical)

    posDiag = buildPosDiag(lines)
    