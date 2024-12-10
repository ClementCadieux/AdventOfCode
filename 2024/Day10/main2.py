import functools
import main1 as base

lines = []

@functools.lru_cache(maxsize=None)
def hikingScore(i, j):
    global lines
    
    val = lines[i][j]

    if val == 9:
        return 1

    lines[i][j] = -1

    up = -1 if i == 0 else lines[i - 1][j]
    down = -1 if i == len(lines) - 1 else lines[i + 1][j]
    left = -1 if j == 0 else lines[i][j - 1]
    right = -1 if j == len(lines[i]) - 1 else lines[i][j + 1]

    score = 0

    if up == val + 1:
        score += hikingScore(i - 1, j)

    if down == val + 1:
        score += hikingScore(i + 1, j)

    if left == val + 1:
        score += hikingScore(i, j - 1)

    if right == val + 1:
        score += hikingScore(i, j + 1)

    lines[i][j] = val

    return score

if __name__ == "__main__":
    lines = base.readFile("2024\\Day10\\input.txt")

    nines, zeroSpots = base.findNinesAndZeroes(lines)

    total = 0

    for spot in zeroSpots:
        total += hikingScore(spot[0], spot[1])

    print(total)