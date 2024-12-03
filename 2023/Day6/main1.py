def readFile(path):
    file = open(path, "r")

    timesLine = file.readline()
    distancesLine = file.readline()

    file.close()

    for i, char in enumerate(timesLine):
        if char.isdigit():
            timesLine = timesLine[i:]
            break

    for i, char in enumerate(distancesLine):
        if char.isdigit():
            distancesLine = distancesLine[i:]
            break

    return (timesLine, distancesLine)

def linesToArrs(lines):
    times = lines[0].split(" ")
    newTimes = []
    
    for i in range(len(times)):
        if(times[i] != ""):
            newTimes.append(int(times[i]))

    distances = lines[1].split(" ")
    newDistances = []

    for i in range(len(distances)):
        if(distances[i] != ""):
            newDistances.append(int(distances[i]))

    return (newTimes, newDistances)

def waysToWin(time, distance):
    sum = 0
    for i in range(time):
        speed = i
        length = speed * (time - speed)

        if length > distance:
            sum += 1
        elif length <= distance and sum != 0:
            break

    return sum

def allWaysToWin(arrs):
    times = arrs[0]
    distances = arrs[1]

    ways = []

    for i in range(len(times)):
        ways.append(waysToWin(times[i], distances[i]))
    
    return ways

if(__name__ == "__main__"):
    lines = readFile("Day6\\input.txt")

    arrs = linesToArrs(lines)
    
    ways = allWaysToWin(arrs)

    prod = 1

    for i in ways:
        prod *= i
    
    print(prod)

