from util import readFile2
import sys

if __name__ == "__main__":
    filePath = "2025\\Day6\\test.txt" if len(sys.argv) < 2 else sys.argv[1]

    lines = readFile2(filePath)

    print(lines)