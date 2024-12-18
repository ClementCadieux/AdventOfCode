import sys
import time

def readFile(path):
    file = open(path, "r")

    lines = file.readlines()

    lines = [line[:-1] if line[-1] == "\n" else line for line in lines]

    return lines

sys.setrecursionlimit(5000)
def scoreTile(scores, maze, i, j, score, direction):
    if scores[-2][1] != 0 and score > scores[-2][1]:
        return False
    
    if scores[i][j] != 0 and scores[i][j] < score:
        return False

    if maze[i][j] == "S":
        befScore = scores[i][j]   
        if befScore != 0 and befScore < score + 1000 if direction == 0 else 0:
            return False
        
        if direction in [0, 1]:
            scores[i][j] = score
        if direction == 0:
            scores[i][j] += 1000
        
        return True
    
    scores[i][j] = score
    
    upScore = score + 1 if direction == 0 else score + 1001 if direction in [1, 3] else -1
    downScore = score + 1 if direction == 2 else score + 1001 if direction in [1, 3] else -1
    leftScore = score + 1 if direction == 3 else score + 1001 if direction in [0, 2] else -1
    rightScore = score + 1 if direction == 1 else score + 1001 if direction in [0, 2] else -1

    up = False
    down = False
    right = False
    left = False

    if maze[i][j - 1] != "#" and rightScore != -1:
        right = scoreTile(scores, maze, i, j - 1, rightScore, 1)
    if maze[i + 1][j] != "#" and upScore != -1:
        up = scoreTile(scores, maze, i + 1, j, upScore, 0)
    if maze[i][j + 1] != "#" and leftScore != -1:
        left = scoreTile(scores, maze, i, j + 1, leftScore, 3)
    if maze[i - 1][j] != "#" and downScore != -1:
        down = scoreTile(scores, maze, i - 1, j, downScore, 2)

    # if up or right or down or left:
    #     scores[i][j] = scores[-2][1]
    
    # seen.remove((i, j))

    return up or right or down or left

sys.setrecursionlimit(5000)
def dijkstra(scoreGrid, grid, i, j, unvisited, nonInfinityNodes, direction):
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

    upPossible = i != 0 and grid[up[0]][up[1]] != "#" and up in unvisited and up not in nonInfinityNodes and direction in [0, 1, 3]
    downPossible = i != len(grid) - 1 and grid[down[0]][down[1]] != "#" and down in unvisited and down not in nonInfinityNodes and direction in [1, 2, 3]
    leftPossible = j != 0 and grid[left[0]][left[1]] != "#" and left in unvisited and left not in nonInfinityNodes and direction in [0, 2, 3]
    rightPossible = j != len(grid[i]) - 1 and grid[right[0]][right[1]] != "#" and right in unvisited and right not in nonInfinityNodes and direction in [0, 1, 2]

    if upPossible:
        scoreGrid[up[0]][up[1]] = score + 1
        if direction != 0:
            scoreGrid[up[0]][up[1]] += 1000
        nonInfinityNodes.append((up, 0))
    if downPossible:
        scoreGrid[down[0]][down[1]] = score + 1
        if direction != 2:
            scoreGrid[down[0]][down[1]] += 1000
        nonInfinityNodes.append((down, 2))
    if leftPossible:
        scoreGrid[left[0]][left[1]] = score + 1
        if direction != 3:
            scoreGrid[left[0]][left[1]] += 1000
        nonInfinityNodes.append((left, 3))
    if rightPossible:
        scoreGrid[right[0]][right[1]] = score + 1
        if direction != 1:
            scoreGrid[right[0]][right[1]] += 1000
        nonInfinityNodes.append((right, 1))

    if len(nonInfinityNodes) == 0:
        return
    
    minNode, newDirection = nonInfinityNodes[0]

    dijkstra(scoreGrid, grid, minNode[0], minNode[1], unvisited, nonInfinityNodes, newDirection)