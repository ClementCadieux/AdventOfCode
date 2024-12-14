def readFile(path):
    file = open(path, "r")

    lines = [line[:-1] if line[-1] == "\n" else line for line in file.readlines()]

    robots = []

    for line in lines:
        splitLine = line.split(" ")
        
        splitLine = [subLine.split("=")[1].split(",") for subLine in splitLine]

        posX = int(splitLine[0][0])
        posY = int(splitLine[0][1])
        veloX = int(splitLine[1][0])
        veloY = int(splitLine[1][1])

        robot = [[posX, posY], (veloX, veloY)]

        robots.append(robot)
    
    return robots

def moveRobots(seconds, robots, xBounds, yBounds):
    for robot in robots:
        xMovement = robot[1][0] * seconds
        yMovement = robot[1][1] * seconds

        robot[0][0] += xMovement
        robot[0][1] += yMovement

        robot[0][0] %= xBounds
        robot[0][1] %= yBounds

if __name__ == "__main__":
    robots = readFile("2024\\Day14\\test.txt")

    moveRobots(100, robots, 11, 7)

