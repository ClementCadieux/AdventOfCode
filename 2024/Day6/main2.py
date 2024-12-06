import main1 as base
import copy

def processGuard(lines, i, j):
    total = 0

    inMap = True

    dir = 0

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

    return total
        

if __name__ == "__main__":
    lines = base.readFile("2024\\Day6\\test.txt")

    i, j = base.findGuard(lines)

    total = processGuard(lines, i, j)

    print(total)