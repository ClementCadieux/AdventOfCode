from util import readFile, pathsToOut
import sys

if __name__ == "__main__":
    args = sys.argv
    filePath = "2025\\Day11\\test.txt" if len(args) < 2 else args[1]

    circuit = readFile(filePath)

    cache = {}

    cache["out"] = 1

    totalPaths = pathsToOut(circuit, cache, "you")

    print(totalPaths)