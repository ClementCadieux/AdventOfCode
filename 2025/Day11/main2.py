from util import readFile, pathsToOut2
import sys

if __name__ == "__main__":
    args = sys.argv
    filePath = "2025\\Day11\\test2.txt" if len(args) < 2 else args[1]

    circuit = readFile(filePath)

    cache = {}

    cache["out"] = [set()]

    pathsFromSvr = pathsToOut2(circuit, cache, "svr")

    total = 0

    for path in pathsFromSvr:
        if "fft" in path and "dac" in path:
            total += 1

    print(total)