import main1 as base

def getAntinodes(lines, locations):
    for i in range(len(locations) - 1):
        currLocation = locations[i]

        for j in range(i + 1, len(locations)):
            nextLocation = locations[j]

            xDiff = currLocation[0] - nextLocation[0]
            yDiff = currLocation[1] - nextLocation[1]

            dir1X = nextLocation[0] + xDiff
            dir1Y = nextLocation[1] + yDiff

            while dir1X >= 0 and dir1X < len(lines) and dir1Y >= 0 and dir1Y < len(lines[0]):
                lines[dir1X] = lines[dir1X][:dir1Y] + "#" + lines[dir1X][dir1Y + 1:]

                dir1X += xDiff
                dir1Y += yDiff
            

            dir2X = nextLocation[0] + xDiff
            dir2Y = nextLocation[1] + yDiff

            while dir2X >= 0 and dir2X < len(lines) and dir2Y >= 0 and dir2Y < len(lines[0]):
                lines[dir2X] = lines[dir2X][:dir2Y] + "#" + lines[dir2X][dir2Y + 1:]

                dir2X -= xDiff
                dir2Y -= yDiff
    
    return lines
            
            

    
    return lines

if __name__ == "__main__":
    lines = base.readFile("2024\\Day8\\input.txt")

    antennaLocations = base.getAntennaLocations(lines)

    for antenna in antennaLocations:
        lines = getAntinodes(lines, antennaLocations[antenna])

    total = base.countAntinodes(lines)

    print(total)