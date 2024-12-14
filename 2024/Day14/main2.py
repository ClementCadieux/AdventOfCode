import main1 as base

def moveRobots(robots, xBounds, yBounds):
    for robot in robots:
        robot[0][0] += robot[1][0]
        robot[0][1] += robot[1][1]

        robot[0][0] %= xBounds
        robot[0][1] %= yBounds

if __name__ == "__main__":
    robots = base.readFile("2024\\Day14\\input.txt")

    xBounds = 101
    yBounds = 103