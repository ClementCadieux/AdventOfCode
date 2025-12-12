from util import readFile
import sys

if __name__ == "__main__":
    args = sys.argv

    filePath = "2025\\Day12\\test.txt" if len(args) < 2 else args[1]

    presents = readFile(filePath)

    print(presents)