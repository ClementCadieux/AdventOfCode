from util import readFile, pathsToOut
import sys

if __name__ == "__main__":
    args = sys.argv
    filePath = "2025\\Day11\\test2.txt" if len(args) < 2 else args[1]

    circuit = readFile(filePath)

