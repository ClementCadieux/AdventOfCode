from util import readFile
import sys

if __name__ == "__main__":
    filePath = "2025\\Day4\\test.txt" if len(sys.argv) < 2 else sys.argv[1]

    grid = readFile(filePath)

    print(grid)