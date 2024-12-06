import main1 as base
import copy

total = 0

def processGuard(lines, i, j, dir):
    inMap = True

    while inMap:

        inMap, dir = base.getDir(lines, inMap, i, j, dir)
        
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
        
def obstacleInFront(lines, i, j, dirChar):
    linesCopy = copy.deepcopy(lines)

    match dirChar:
        case "^":
            if i != 0:
                linesCopy[i - 1] = linesCopy[i - 1][:j] + "#" + linesCopy[i - 1][j + 1:]

                processGuard(linesCopy, i, j, 0)
        
        case ">":
            if j != len(lines[i]) - 1:                
                linesCopy[i] = linesCopy[i][:j + 1] + "#" + linesCopy[i][j + 2:]

                processGuard(linesCopy, i, j, 1)
        
        case "v":
            if i != len(lines) - 1:
                linesCopy[i + 1] = linesCopy[i + 1][:j] + "#" + linesCopy[i + 1][j + 1:]

                processGuard(linesCopy, i, j, 2)

        case "<":
            if j != 0:            
                linesCopy[i] = linesCopy[i][:j - 1] + "#" + linesCopy[i][j:]

                processGuard(linesCopy, i, j, 3)
            
    

if __name__ == "__main__":
    lines = base.readFile("2024\\Day6\\test.txt")

    i, j = base.findGuard(lines)

    lines = processGuard(lines, i, j)

    print(total)