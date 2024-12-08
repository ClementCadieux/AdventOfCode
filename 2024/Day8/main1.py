def readFile(path):
    file = open(path, "r")

    lines = file.readlines()

    lines = [line[:-1] if line[-1] == "\n" else line for line in lines]

    return lines

def getAntennaLocations(lines):
    antennaLocations = {}

    for i in range(len(lines)):
        line = lines[i]
        for j in range(len(line)):
            tile = line[j]

            if tile != ".":
                if tile not in antennaLocations:
                    antennaLocations[tile] = []

                antennaLocations[tile].append((i, j))
    
    return antennaLocations

def getAntinodes(lines, locations):
    for i in range(len(locations) - 1):
        currLocation = locations[i]

        for j in range(i + 1, len(locations)):
            nextLocation = locations[j]

            xDiff = currLocation[0] - nextLocation[0]
            yDiff = currLocation[1] - nextLocation[1]

            antinodeSpot1 = (currLocation[0] + xDiff, currLocation[1] + yDiff)

            antinodeSpot2 = (nextLocation[0] - xDiff, nextLocation[1] - yDiff)

            if antinodeSpot1[0] >= 0 and antinodeSpot1[0] < len(lines) and antinodeSpot1[1] >= 0 and antinodeSpot1[1] < len(lines[0]):
                lines[antinodeSpot1[0]] = lines[antinodeSpot1[0]][:antinodeSpot1[1]] + "#" + lines[antinodeSpot1[0]][antinodeSpot1[1] + 1:]
            
            if antinodeSpot2[0] >= 0 and antinodeSpot2[0] < len(lines) and antinodeSpot2[1] >= 0 and antinodeSpot2[1] < len(lines[0]):
                lines[antinodeSpot2[0]] = lines[antinodeSpot2[0]][:antinodeSpot2[1]] + "#" + lines[antinodeSpot2[0]][antinodeSpot2[1] + 1:]
        
    return lines
            
def countAntinodes(lines):
    total = 0

    for line in lines:
        for tile in line:
            if tile == "#":
                total += 1
    
    return total

if __name__ == "__main__":
    lines = readFile("2024\\Day8\\input.txt")

    antennaLocations = getAntennaLocations(lines)

    for antenna in antennaLocations:
        lines = getAntinodes(lines, antennaLocations[antenna])
    
    total = countAntinodes(lines)

    print(total)