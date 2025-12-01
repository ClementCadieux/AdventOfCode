import sys
from util import readFile

if __name__ == "__main__":
    filePath = "2025\\Day1\\test.txt" if len(sys.argv) == 1 else sys.argv[1]
    
    rotations = readFile(filePath)

    pointer = 50

    count = 0

    for rotation in rotations:
        if pointer == 0 and rotation < 0:
            rotation += 100
        
        pointer += rotation

        while pointer < 0:
            pointer += 100
            count += 1

        if pointer == 0:
            count += 1
        
        while pointer >= 100:
            pointer -= 100
            count += 1
            
    print(count)