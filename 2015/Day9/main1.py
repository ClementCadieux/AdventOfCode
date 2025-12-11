from util import readFile, sortCities
import sys

if __name__ == "__main__":
    filePath = "2015\\Day9\\test.txt" if len(sys.argv) < 2 else sys.argv[1]

    distances = readFile(filePath)

    sortedCities = sortCities(distances)

    total = 0

    for i in range(len(sortedCities) - 1):
        city = sortedCities[i]
        print(city)
        nextCity = sortedCities[i + 1]

        total += distances[city][nextCity]

    print(total)