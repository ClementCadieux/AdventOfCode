from util import readFile, processButtons
import sys

if __name__ == "__main__":
    filePath = "2025\\Day10\\test.txt" if len(sys.argv) < 2 else sys.argv[1]

    lines = readFile(filePath)

    total = 0

    for machine in lines:
        machine[1] = processButtons(machine[1], len(machine[0]))

        print(machine)