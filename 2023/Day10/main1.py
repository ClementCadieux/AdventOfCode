def readFile(path):
    file = open(path, "r")

    grid = []

    lineStr = file.readline()

    while(lineStr != ""):
        if lineStr[-1] == "\n":
            lineStr = lineStr[0:-1]

        line = list(lineStr)
        
        grid.append(line)

        lineStr = file.readline()

    return grid

def processTile(grid, i, j):
    prev = None

    dist = 0

    tile = grid[i][j]

    while prev is None or tile != "S":
        match tile:
            case '|':
                nextPrev = (i,j)
                next = (i - 1, j)
                j = next[1]
                if next[0] != prev[0] or next[1] != prev[1]:
                    i = next[0]
                else:
                    i = next[0] + 2
                
                prev = nextPrev    
            case '-':
                nextPrev = (i,j)
                next = (i, j - 1)
                i = next[0]
                if next[0] != prev[0] or next[1] != prev[1]:
                    j = next[1]
                else:
                    j = next[1] + 2
                
                prev = nextPrev
            case 'L':
                nextPrev = (i,j)
                next = (i, j + 1)
                if next[0] != prev[0] or next[1] != prev[1]:
                    i = next[0]
                    j = next[1]
                else:
                    i = next[0] - 1
                    j = next[1] - 1
                
                prev = nextPrev
            case 'J':
                nextPrev = (i,j)
                next = (i, j - 1)
                if next[0] != prev[0] or next[1] != prev[1]:
                    i = next[0]
                    j = next[1]
                else:
                    i = next[0] - 1
                    j = next[1] + 1
                
                prev = nextPrev
            case '7':
                nextPrev = (i,j)
                next = (i, j - 1)
                if next[0] != prev[0] or next[1] != prev[1]:
                    i = next[0]
                    j = next[1]
                else:
                    i = next[0] + 1
                    j = next[1] + 1
                
                prev = nextPrev
            case 'F':
                nextPrev = (i,j)
                next = (i, j + 1)
                if next[0] != prev[0] or next[1] != prev[1]:
                    i = next[0]
                    j = next[1]
                else:
                    i = next[0] + 1
                    j = next[1] - 1
                
                prev = nextPrev
            case 'S':
                if prev is not None:
                    return int(dist / 2 + dist % 2)
                
                right = '.' if j == len(grid[i]) else grid[i][j + 1]

                if right in ["7", "J", "-"]:
                    prev = (i,j)
                    j += 1
                
                left = '.' if j == 0 else grid[i][j - 1]

                if left in ["-", "F", "L"] and prev is None:
                    prev = (i,j)
                    j -= 1
                
                up = '.' if i == 0 else grid[i - 1][j]

                if up in ["|", "F", "7"] and prev is None:
                    prev = (i,j)
                    i -= 1
                
                if prev is None:
                    prev = (i,j)
                    i += 1
            
        tile = grid[i][j]
        dist += 1

    return int(dist / 2 + dist % 2)


if __name__ == "__main__":
    grid = readFile("Day10\\input.txt")

    gridDist = [[-1 for x in grid[y]] for y in range(len(grid))]

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'S':
                print(processTile(grid, i, j))
                break
    
