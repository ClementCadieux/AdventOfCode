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