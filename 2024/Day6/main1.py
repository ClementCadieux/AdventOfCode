import re

def readFile(path):
    file = open(path, "r")

    lines = file.readlines()

    lines = [line[:-1] if line[-1] == "\n" else line for line in lines]

    return lines

def findGuard(lines):
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "^":
                return (i,j)
    
    return None

def processGuard(lines, i, j):
    inMap = True

    dir = 0

    while inMap:
        lines[i][j] = "X"

        inMap, dir = getDir(lines, i, j, dir)

        if inMap:
            match dir:
                case 0:
                    i -= 1
                case 1:
                    j += 1
                case 2:
                    i += 1
                case 3:
                    j -= 1
        
def getDir(lines, i, j, dir):
    match dir:
        case 0:
            if i == 0:
                inMap = False
            elif lines[i-1][j] == "#":
                dir += 1
            
        case 1:
            if j == len(lines[0]) - 1:
                inMap = False
            elif lines[i][j + 1] == "#":
                dir += 1
                
        case 2:
            if i == len(lines) - 1:
                inMap = False
            elif lines[i + 1][j] == "#":
                dir += 1
            
        case 3:
            if j == 0:
                inMap = False
            elif lines[i][j - 1] == "#":
                dir = 0
    
    return (inMap, dir)

def countX(lines):
    total = 0

    for line in lines:
        total += re.findall("X", line)

    return total
