import sys
import time

def readFile(path):
    file = open(path, "r")

    lines = file.readlines()

    lines = [line[:-1] if line[-1] == "\n" else line for line in lines]

    return lines

def scoreTiles(lines):
    scores = [[-1 for tile in line] for line in lines]
    unvisited = set()

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            unvisited.add((i,j))

    scores[-2][1] = 0

    nonInfinityNodes = []
    nonInfinityNodes.append(((len(lines) - 2, 1), 0, 0))

    dijkstra(scores, lines, len(lines) - 2, 1, unvisited, nonInfinityNodes, 1, 0)
    
    return scores

def dijkstra(scoreGrid, grid, i, j, unvisited, nonInfinityNodes, direction, score):
    while len(nonInfinityNodes) != 0:    
        while (i, j) not in unvisited and len(nonInfinityNodes) != 1:
            nonInfinityNodes.pop(0)
            (i,j), direction, score = nonInfinityNodes[0]

        unvisited.remove((i, j))
        nonInfinityNodes.pop(0)

        if grid[i][j] == "E":
            return

        up = (i - 1, j)
        down = (i + 1, j)
        left = (i, j - 1)
        right = (i, j + 1)

        upPossible = i != 0 and grid[up[0]][up[1]] != "#" and up in unvisited and up not in nonInfinityNodes and direction in [0, 1, 3]
        downPossible = i != len(grid) - 1 and grid[down[0]][down[1]] != "#" and down in unvisited and down not in nonInfinityNodes and direction in [1, 2, 3]
        leftPossible = j != 0 and grid[left[0]][left[1]] != "#" and left in unvisited and left not in nonInfinityNodes and direction in [0, 2, 3]
        rightPossible = j != len(grid[i]) - 1 and grid[right[0]][right[1]] != "#" and right in unvisited and right not in nonInfinityNodes and direction in [0, 1, 2]

        if upPossible:
            scoreGrid[up[0]][up[1]] = score + 1
            if direction != 0:
                scoreGrid[up[0]][up[1]] += 1000
            inserted = False
            for i in range(len(nonInfinityNodes)):
                if nonInfinityNodes[i][2] > scoreGrid[up[0]][up[1]]:
                    nonInfinityNodes.insert(i, (up, 0, scoreGrid[up[0]][up[1]]))
                    inserted = True
                    break
            if not inserted:
                nonInfinityNodes.append((up, 0, scoreGrid[up[0]][up[1]]))
        if downPossible:
            scoreGrid[down[0]][down[1]] = score + 1
            if direction != 2:
                scoreGrid[down[0]][down[1]] += 1000
            inserted = False
            for i in range(len(nonInfinityNodes)):
                if nonInfinityNodes[i][2] > scoreGrid[down[0]][down[1]]:
                    nonInfinityNodes.insert(i, (down, 2, scoreGrid[down[0]][down[1]]))
                    inserted = True
                    break
            if not inserted:
                nonInfinityNodes.append((down, 2, scoreGrid[down[0]][down[1]]))
        if leftPossible:
            scoreGrid[left[0]][left[1]] = score + 1
            if direction != 3:
                scoreGrid[left[0]][left[1]] += 1000
            inserted = False
            for i in range(len(nonInfinityNodes)):
                if nonInfinityNodes[i][2] > scoreGrid[left[0]][left[1]]:
                    nonInfinityNodes.insert(i, (left, 3, scoreGrid[left[0]][left[1]]))
                    inserted = True
                    break
            if not inserted:
                nonInfinityNodes.append((left, 3, scoreGrid[left[0]][left[1]]))
        if rightPossible:
            scoreGrid[right[0]][right[1]] = score + 1
            if direction != 1:
                scoreGrid[right[0]][right[1]] += 1000
            inserted = False
            for i in range(len(nonInfinityNodes)):
                if nonInfinityNodes[i][2] > scoreGrid[right[0]][right[1]]:
                    nonInfinityNodes.insert(i, (right, 1, scoreGrid[right[0]][right[1]]))
                    inserted = True
                    break
            if not inserted:
                nonInfinityNodes.append((right, 1, scoreGrid[right[0]][right[1]]))

        if len(nonInfinityNodes) == 0:
            return
        
        (i,j), direction, score = nonInfinityNodes[0]
