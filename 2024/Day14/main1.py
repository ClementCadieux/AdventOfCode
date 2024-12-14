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

def quadrantCalc(robots, xBounds, yBounds):
    quadrantTotals = [0, 0, 0, 0]

    for robot in robots:
        robotX = robot[0][0]
        robotY = robot[0][1]

        quandrantX = 0 if robotX < int(xBounds/2) else 1 if robotX > int(xBounds/2) else -1
        quandrantY = 0 if robotY < int(yBounds/2) else 1 if robotY > int(yBounds/2) else -1

        quandrantIndex = -1

        if quandrantX == 0:
            if quandrantY == 0:
                quandrantIndex = 0
            elif quandrantY == 1:
                quandrantIndex = 2
        elif quandrantX == 1:
            if quandrantY == 0:
                quandrantIndex = 1
            elif quandrantY == 1:
                quandrantIndex = 3

        if quandrantIndex != -1:
            quadrantTotals[quandrantIndex] += 1

    return quadrantTotals

if __name__ == "__main__":
    robots = readFile("2024\\Day14\\test.txt")

    moveRobots(100, robots, 11, 7)

    quadrantTotals = quadrantCalc(robots, 11, 7)

    print(quadrantTotals)