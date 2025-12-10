from util import readFile, processJoltage
import sys

if __name__ == "__main__":
    filePath = "2025\\Day10\\test.txt" if len(sys.argv) < 2 else sys.argv[1]

    lines = readFile(filePath)

    total = 0

    for machine in lines:
        targetState = tuple(machine[2])
        currStateList = [0 for _ in range(len(targetState))]
        currState = tuple(currStateList)

        buttons = machine[1]

        cache = {}

        cache[targetState] = 0

        total += processJoltage(currState, buttons, targetState, cache)

    print(total)