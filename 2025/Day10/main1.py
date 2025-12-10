from util import readFile, processMachineState
import sys

if __name__ == "__main__":
    filePath = "2025\\Day10\\test.txt" if len(sys.argv) < 2 else sys.argv[1]

    lines = readFile(filePath)

    total = 0

    for machine in lines:
        print(machine)
        cache = {}
        currState = "".join(["." for _ in range(len(machine[0]))])

        total += processMachineState(machine, cache, currState, -1)

    print(total)