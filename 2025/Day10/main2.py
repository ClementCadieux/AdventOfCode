from util import readFile, processJoltage, circuitFrequency
import sys

if __name__ == "__main__":
    filePath = "2025\\Day10\\test.txt" if len(sys.argv) < 2 else sys.argv[1]

    lines = readFile(filePath)

    total = 0

    for machine in lines:
        currState = machine[2]

        buttons = machine[1]

        circuitFreq = circuitFrequency(buttons)

        total += processJoltage(currState, buttons, circuitFreq)
        print(total)

    print(total)