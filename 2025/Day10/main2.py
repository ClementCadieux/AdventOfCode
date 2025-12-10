from util import readFile, processJoltage
import sys

if __name__ == "__main__":
    filePath = "2025\\Day10\\test.txt" if len(sys.argv) < 2 else sys.argv[1]

    lines = readFile(filePath)

    total = 0

    for machine in lines:
        currState = tuple(machine[2])

        buttons = machine[1]

        for i in range(len(buttons)):
            buttons[i] = sorted(buttons[i], key=lambda x : currState[x])

        buttons = sorted(buttons, key=lambda x : (currState[x[-1]], -len(x)))

        cache = {}
        
        cache[tuple([0 for _ in currState])] = 0

        total += processJoltage(currState, buttons, cache, 0)

    print(total)