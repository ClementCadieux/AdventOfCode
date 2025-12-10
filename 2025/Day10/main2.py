from util import readFile, processJoltage, sortButtons, circuitFrequency
import sys

if __name__ == "__main__":
    filePath = "2025\\Day10\\test.txt" if len(sys.argv) < 2 else sys.argv[1]

    lines = readFile(filePath)

    total = 0

    for machine in lines:
        currState = tuple(machine[2])

        buttons = machine[1]

        frequency = circuitFrequency(buttons)

        buttons = sortButtons(buttons, frequency)

        cache = {}

        total += processJoltage(currState, buttons, cache, 0)

    print(total)