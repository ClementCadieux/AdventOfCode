import sys
from util import readFile

if __name__ == "__main__":
    filePath = sys.argv[1]
    
    rotations = readFile(filePath)

    pointer = 50

    count = 0

    for rotation in rotations:
        pointer += rotation

        while pointer < 0:
            pointer += 100
            count += 1
        
        while pointer >= 100:
            pointer -= 100
            count += 1
    
    print(count)