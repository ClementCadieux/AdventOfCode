import main1 as base
import time

def moveRobots(robots, xBounds, yBounds):
    for robot in robots:
        robot[0][0] += robot[1][0]
        robot[0][1] += robot[1][1]

        robot[0][0] %= xBounds
        robot[0][1] %= yBounds

def writeRobots(robots):
    grid = [['.' for i in range(101)] for j in range(103)]

    for robot in robots:
        grid[robot[0][1]][robot[0][0]] = "#"
    
    file = open("2024\\Day14\\currentState.txt", "w")

    for line in grid:
        file.write(str(line))
        file.write("\n")

    file.close()

if __name__ == "__main__":
    robots = base.readFile("2024\\Day14\\input.txt")

    xBounds = 101
    yBounds = 103

    base.moveRobots(6355, robots, xBounds, yBounds)
    writeRobots(robots)     
