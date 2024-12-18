import sys

def readFile(filePath):
    file = open(filePath, "r")

    lines = file.readlines()

    lines = [line[:-1] if line[-1] == "\n" else line for line in lines]

    splitLines = [line.split(",") for line in lines]

    intSplitLines = [[int(coord) for coord in line] for line in splitLines]

    return intSplitLines

def genGrid(coords, bound, sim):
    grid = [["." for j in range(bound)] for i in range(bound)]

    for i in range(sim):
        coord = coords[i]
        grid[coord[1]][coord[0]] = "#"

    return grid

sys.setrecursionlimit(5000)
def dijkstra(scoreGrid, grid, i, j, unvisited, nonInfinityNodes):
    if (i, j) not in unvisited:
        return

    unvisited.remove((i, j))
    nonInfinityNodes.pop(0)

    if grid[i][j] == "#":
        return

    score = scoreGrid[i][j]

    up = (i - 1, j)
    down = (i + 1, j)
    left = (i, j - 1)
    right = (i, j + 1)

    upPossible = i != 0 and grid[up[0]][up[1]] != "#" and up in unvisited and up not in nonInfinityNodes
    downPossible = i != len(grid) - 1 and grid[down[0]][down[1]] != "#" and down in unvisited and down not in nonInfinityNodes
    leftPossible = j != 0 and grid[left[0]][left[1]] != "#" and left in unvisited and left not in nonInfinityNodes
    rightPossible = j != len(grid[i]) - 1 and grid[right[0]][right[1]] != "#" and right in unvisited and right not in nonInfinityNodes

    if upPossible:
        scoreGrid[up[0]][up[1]] = score + 1
        nonInfinityNodes.append(up)
    if downPossible:
        scoreGrid[down[0]][down[1]] = score + 1
        nonInfinityNodes.append(down)
    if leftPossible:
        scoreGrid[left[0]][left[1]] = score + 1
        nonInfinityNodes.append(left)
    if rightPossible:
        scoreGrid[right[0]][right[1]] = score + 1
        nonInfinityNodes.append(right)

    if len(nonInfinityNodes) == 0:
        return
    
    minNode = nonInfinityNodes[0]

    dijkstra(scoreGrid, grid, minNode[0], minNode[1], unvisited, nonInfinityNodes)