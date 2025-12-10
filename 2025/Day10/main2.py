from util import readFile, processJoltage, sortButtons
import sys

if __name__ == "__main__":
    filePath = "2025\\Day10\\test.txt" if len(sys.argv) < 2 else sys.argv[1]

    lines = readFile(filePath)

    total = 0

    for machine in lines:
        print("machine")
        targetState = tuple(machine[2])

        buttons = machine[1]

        buttons = sortButtons(targetState, buttons)

        cache = {}

        currState = tuple([0 for _ in targetState])

        cache[targetState] = 0

        total += processJoltage(currState, buttons, targetState,cache)

    print(total)