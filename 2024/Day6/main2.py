import main1 as base
import copy

total = set()

def processGuard(lines, i, j, dir, obstacle, tilesByDir, seen):
    inMap = True

    while inMap:

        changed = True

        while changed:
            inMap, newDir = base.getDir(lines, inMap, i, j, dir)
            if dir != newDir:
                dir = newDir
            else:
                changed = False      

        if (i,j) in tilesByDir[dir] and obstacle:
            return lines, True

        dirChar = "^" if dir == 0 else ">" if dir == 1 else "v" if dir == 2 else "<"

        lines[i] = lines[i][:j] + dirChar + lines[i][j + 1:]
        
        tilesByDir[dir].append((i, j))
        seen.add((i,j))

        if not obstacle:
            obstacleInFront(lines, i, j, dir, tilesByDir, seen) 

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

    return lines, False
        
def obstacleInFront(lines, i, j, dir, tilesByDir, seen):
    global total
    linesCopy = copy.deepcopy(lines)
    tilesByDirCopy = copy.deepcopy(tilesByDir)
    seenCopy = copy.deepcopy(seen)

    trap = ()

    match dir:
        case 0:
            if i != 0:
                linesCopy[i - 1] = linesCopy[i - 1][:j] + "#" + linesCopy[i - 1][j + 1:]

                trap = (i - 1, j)
        
        case 1:
            if j != len(lines[i]) - 1:                
                linesCopy[i] = linesCopy[i][:j + 1] + "#" + linesCopy[i][j + 2:]

                trap = (i, j + 1)
        
        case 2:
            if i != len(lines) - 1:
                linesCopy[i + 1] = linesCopy[i + 1][:j] + "#" + linesCopy[i + 1][j + 1:]

                trap = (i + 1, j)

        case 3:
            if j != 0:            
                linesCopy[i] = linesCopy[i][:j - 1] + "#" + linesCopy[i][j:]

                trap = (i, j - 1)
    
    foundLoop = False
    if trap != () and trap not in seen:
        lines, foundLoop = processGuard(linesCopy, i, j, dir, True, tilesByDirCopy, seenCopy)

    if foundLoop and trap != ():
        total.add(trap)
        print(len(total))
            
    

if __name__ == "__main__":
    lines = base.readFile("2024\\Day6\\input.txt")

    orig = base.findGuard(lines)

    tilesByDir = [[] for x in range(4)]

    lines = processGuard(lines, orig[0], orig[1], 0, False, tilesByDir, set())

    print(total)
    print(len(total))