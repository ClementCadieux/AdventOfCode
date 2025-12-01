import sys

def readFile(path):
    file = open(path, "r")

    rotations = []

    for line in file.readlines():
        dir = line[0]
        num = int(line[1:])

        polarity = -1 if dir == 'L' else 1

        val = num * polarity

        rotations.append(val)
    
    return rotations


if __name__ == "__main__":
    filePath = sys.argv[1]
    
    rotations = readFile(filePath)

    pointer = 50

    count = 0

    for rotation in rotations:
        pointer += rotation

        if pointer % 100 == 0:
            count += 1

    print(count)