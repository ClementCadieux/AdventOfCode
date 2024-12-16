import sys

def readFile(path):
    file = open(path, "r")

    lines = file.readlines()

    lines = [line[:-1] if line[-1] == "\n" else line for line in lines]

    return lines

sys.setrecursionlimit(5000)
def scoreTile(scores, maze, i, j, score, direction):
    if scores[i][j] != 0 and scores[i][j] < score:
        return
    
    if maze[i][j] == "S":
        if direction in [0, 1]:
            scores[i][j] = score
        if direction == 0:
            scores[i][j] += 1000
        return
    
    scores[i][j] = score


    upScore = score + 1 if direction == 0 else score + 1001 if direction in [1, 3] else -1
    downScore = score + 1 if direction == 2 else score + 1001 if direction in [1, 3] else -1
    leftScore = score + 1 if direction == 3 else score + 1001 if direction in [0, 2] else -1
    rightScore = score + 1 if direction == 1 else score + 1001 if direction in [0, 2] else -1

    if maze[i + 1][j] != "#" and upScore != -1:
        scoreTile(scores, maze, i + 1, j, upScore, 0)
    if maze[i - 1][j] != "#" and downScore != -1:
        scoreTile(scores, maze, i - 1, j, downScore, 2)
    if maze[i][j + 1] != "#" and leftScore != -1:
        scoreTile(scores, maze, i, j + 1, leftScore, 3)
    if maze[i][j - 1] != "#" and rightScore != -1:
        scoreTile(scores, maze, i, j - 1, rightScore, 1)

    