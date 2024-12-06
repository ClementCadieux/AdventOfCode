import main1 as base
import copy

total = set()

def processGuard(lines, i, j, dir, obstacle, tilesByDir):
    global total

    inMap = True

    while inMap:

        inMap, dir = base.getDir(lines, inMap, i, j, dir)

        if (i,j) in tilesByDir[dir]:
            total.add((i, j))
            return

        dirChar = "^" if dir == 0 else ">" if dir == 1 else "v" if dir == 2 else "<"

        lines[i] = lines[i][:j] + dirChar + lines[i][j + 1:]
        
        tilesByDir[dir].append((i, j))

        if not obstacle and (i, j) not in total:
            obstacleInFront(lines, i, j, dir, tilesByDir) 

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
        
def obstacleInFront(lines, i, j, dir, tilesByDir):
    linesCopy = copy.deepcopy(lines)
    tilesByDirCopy = copy.deepcopy(tilesByDir)

    match dir:
        case 0:
            if i != 0:
                linesCopy[i - 1] = linesCopy[i - 1][:j] + "#" + linesCopy[i - 1][j + 1:]
        
        case 1:
            if j != len(lines[i]) - 1:                
                linesCopy[i] = linesCopy[i][:j + 1] + "#" + linesCopy[i][j + 2:]
        
        case 2:
            if i != len(lines) - 1:
                linesCopy[i + 1] = linesCopy[i + 1][:j] + "#" + linesCopy[i + 1][j + 1:]

        case 3:
            if j != 0:            
                linesCopy[i] = linesCopy[i][:j - 1] + "#" + linesCopy[i][j:]
    
    
    processGuard(linesCopy, i, j, dir, True, tilesByDirCopy)
            
    

if __name__ == "__main__":
    lines = base.readFile("2024\\Day6\\test.txt")

    i, j = base.findGuard(lines)

    tilesByDir = [[] for x in range(4)]

    lines = processGuard(lines, i, j, 0, False, tilesByDir)

    print(len(total))