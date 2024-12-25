def readFile(path):
    file = open(path, "r")

    lines = file.readlines()

    lines = [line[:-1] if line[-1] == "\n" else line for line in lines]

    return lines

def dijkstra(scoreGrid, grid, i, j, unvisited, nonInfinityNodes, direction, score, comesFrom):
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

        upPossibleIndex = i != 0
        upPossibleWall = grid[up[0]][up[1]] != "#"
        upPossibleUnvisited = up in unvisited
        upPossibleNotInfinity = up not in nonInfinityNodes
        upPossibleDirection = direction in [0, 1, 3]

        upShorter = upPossibleIndex and upPossibleWall and upPossibleUnvisited and upPossibleDirection
        upPossible = upPossibleIndex and upPossibleWall and upPossibleUnvisited and upPossibleNotInfinity and upPossibleDirection
        
        downPossibleIndex = i != len(grid) - 1
        downPossibleWall = grid[down[0]][down[1]] != "#"
        downPossibleUnvisited = down in unvisited
        downPossibleNotInfinity = down not in nonInfinityNodes
        downPossibleDirection = direction in [2, 1, 3]

        downShorter = downPossibleIndex and downPossibleWall and downPossibleUnvisited and downPossibleDirection    
        downPossible = downPossibleIndex and downPossibleWall and downPossibleUnvisited and downPossibleNotInfinity and downPossibleDirection
        
        leftPossibleIndex = j != 0
        leftPossibleWall = grid[left[0]][left[1]] != "#"
        leftPossibleUnvisited = left in unvisited
        leftPossibleNotInfinity = left not in nonInfinityNodes
        leftPossibleDirection = direction in [0, 2, 3]

        leftShorter = leftPossibleIndex and leftPossibleWall and leftPossibleUnvisited and leftPossibleDirection
        leftPossible = leftPossibleIndex and leftPossibleWall and leftPossibleUnvisited and leftPossibleNotInfinity and leftPossibleDirection
        
        rightPossibleIndex = j != len(grid[0]) - 1
        rightPossibleWall = grid[right[0]][right[1]] != "#"
        rightPossibleUnvisited = right in unvisited
        rightPossibleNotInfinity = right not in nonInfinityNodes
        rightPossibleDirection = direction in [0, 1, 2]
              
        rightShorter = rightPossibleIndex and rightPossibleWall and rightPossibleUnvisited and rightPossibleDirection
        rightPossible = rightPossibleIndex and rightPossibleWall and rightPossibleUnvisited and rightPossibleNotInfinity and rightPossibleDirection
        
        if upShorter:
            comesFrom[up].append((i,j))
        if downShorter:
            comesFrom[down].append((i,j))
        if leftShorter:
            comesFrom[left].append((i,j))
        if rightShorter:
            comesFrom[right].append((i,j))

        if upPossible:
            scoreGrid[up[0]][up[1]] = score + 1
            if direction != 0:
                scoreGrid[up[0]][up[1]] += 1000
            inserted = False
            for nonInfinityIdx in range(len(nonInfinityNodes)):
                if nonInfinityNodes[nonInfinityIdx][2] > scoreGrid[up[0]][up[1]]:
                    nonInfinityNodes.insert(nonInfinityIdx, (up, 0, scoreGrid[up[0]][up[1]]))
                    inserted = True
                    break
            if not inserted:
                nonInfinityNodes.append((up, 0, scoreGrid[up[0]][up[1]]))
        if downPossible:
            scoreGrid[down[0]][down[1]] = score + 1
            if direction != 2:
                scoreGrid[down[0]][down[1]] += 1000
            inserted = False
            for nonInfinityIdx in range(len(nonInfinityNodes)):
                if nonInfinityNodes[nonInfinityIdx][2] > scoreGrid[down[0]][down[1]]:
                    nonInfinityNodes.insert(nonInfinityIdx, (down, 2, scoreGrid[down[0]][down[1]]))
                    inserted = True
                    break
            if not inserted:
                nonInfinityNodes.append((down, 2, scoreGrid[down[0]][down[1]]))
        if leftPossible:
            scoreGrid[left[0]][left[1]] = score + 1
            if direction != 3:
                scoreGrid[left[0]][left[1]] += 1000
            inserted = False
            for nonInfinityIdx in range(len(nonInfinityNodes)):
                if nonInfinityNodes[nonInfinityIdx][2] > scoreGrid[left[0]][left[1]]:
                    nonInfinityNodes.insert(nonInfinityIdx, (left, 3, scoreGrid[left[0]][left[1]]))
                    inserted = True
                    break
            if not inserted:
                nonInfinityNodes.append((left, 3, scoreGrid[left[0]][left[1]]))
        if rightPossible:
            scoreGrid[right[0]][right[1]] = score + 1
            if direction != 1:
                scoreGrid[right[0]][right[1]] += 1000
            inserted = False
            for nonInfinityIdx in range(len(nonInfinityNodes)):
                if nonInfinityNodes[nonInfinityIdx][2] > scoreGrid[right[0]][right[1]]:
                    nonInfinityNodes.insert(nonInfinityIdx, (right, 1, scoreGrid[right[0]][right[1]]))
                    inserted = True
                    break
            if not inserted:
                nonInfinityNodes.append((right, 1, scoreGrid[right[0]][right[1]]))

        if len(nonInfinityNodes) == 0:
            return
        
        (i,j), direction, score = nonInfinityNodes[0]

def backtrackPath(comesFrom, i, j, startCoords):
    if (i,j) == startCoords:
        return (True, 1)
    
    total = 0
    isPath = False

    for tile in comesFrom[(i,j)]:
        tileProcess = backtrackPath(comesFrom, tile[0], tile[1], startCoords)

        if tileProcess[0]:
            isPath = True
            total += tileProcess[1]

    if isPath:
        total += 1
        
    return (isPath, total)