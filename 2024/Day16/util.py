def readFile(path):
    file = open(path, "r")

    lines = file.readlines()

    lines = [line[:-1] if line[-1] == "\n" else line for line in lines]

    return lines

def scoreTile(scores, maze, i, j, originI, originJ, direction):
    if scores[i][j] != -1:
        return scores[i][j]
    
    if maze[i][j] == "E":
        scores[i][j] = 0
        return 0
    
    up = [i - 1, j]
    down = [i + 1, j]
    left = [i, j - 1]
    right = [i, j + 1]

    upPossible = maze[up[0]][up[1]] != "#" and (up[0] != originI and up[1] != originJ) and direction in [0, 1, 3]
    downPossible = maze[down[0]][down[1]] != "#" and (down[0] != originI and down[1] != originJ) and direction in [1, 2, 3]
    leftPossible = maze[left[0]][left[1]] != "#" and (left[0] != originI and left[1] != originJ) and direction in [0, 2, 3]
    rightPossible = maze[right[0]][right[1]] != "#" and (right[0] != originI and right[1] != originJ) and direction in [0, 1, 2]

    upScore = -1 if not upPossible else (scoreTile(scores, maze, i - 1, j, i, j, 0) + 1)
    downScore = -1 if not downPossible else (scoreTile(scores, maze, i + 1, j, i, j, 2) + 1)
    leftScore = -1 if not leftPossible else (scoreTile(scores, maze, i, j - 1, i, j, 3) + 1)
    rightScore = -1 if not rightPossible else (scoreTile(scores, maze, i, j + 1, i, j, 1) + 1)

    if direction in [1, 3] and upPossible:
        upScore += 1000
    if direction in [1, 3] and downPossible:
        downScore += 1000
    if direction in [0, 2] and leftPossible:
        leftScore += 1000
    if direction in [0, 2] and rightPossible:
        rightScore += 1000
    
    score = upScore

    if score == -1 or downScore < score:
        score = downScore
    
    if score == -1 or leftScore < score:
        score = leftScore

    if score == -1 or rightScore < score:
        score = rightScore

    scores[i][j] = score

    return score