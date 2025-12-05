from util import readFile
import sys

if __name__ == "__main__":
    filePath = "2015\\Day9\\test.txt" if len(sys.argv) < 2 else sys.argv[1]

    distances, city = readFile(filePath)

    seenCities = set()
    seenCities.add(city)

    totalDistance = 0

    while len(seenCities) < len(distances):
        nextCities = distances[city]

        nextCity = city

        nextIdx = -1

        while nextCity in seenCities:
            nextIdx += 1
            nextCity = nextCities[nextIdx][0]

        seenCities.add(nextCity)
        city = nextCity

        totalDistance += nextCities[nextIdx][1]

    print(totalDistance)
    
    