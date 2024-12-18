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

def dijkstra(scoreGrid, grid, i, j, unvisited, nonInfinityNodes, direction):
    return None