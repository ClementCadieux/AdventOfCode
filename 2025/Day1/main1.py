import sys
from util import readFile

if __name__ == "__main__":
    filePath = "2025\\Day1\\test.txt" if len(sys.argv) == 1 else sys.argv[1]
    
    rotations = readFile(filePath)

    pointer = 50

    count = 0

    for rotation in rotations:
        pointer += rotation

        if pointer % 100 == 0:
            count += 1

    print(count)