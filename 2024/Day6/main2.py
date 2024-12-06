import main1 as base
def processGuard(lines, i, j):
    inMap = True

    dir = 0

    while inMap:

        inMap, dir = getDir(lines, inMap, i, j, dir)
        
        dirChar = "^" if dir == 0 else ">" if dir == 1 else "v" if dir == 2 else "<"
        lines[i] = lines[i][:j] + dirChar + lines[i][j + 1:]

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

    return lines
        
def getDir(lines, inMap, i, j, dir):
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

if __name__ == "__main__":
    lines = base.readFile("2024\\Day6\\test.txt")

    i, j = base.findGuard(lines)

    