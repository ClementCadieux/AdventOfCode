from util import readFile
import sys

if __name__ == "__main__":
    filePath = "2025\\Day8\\test.txt" if len(sys.argv) < 2 else sys.argv[1]
    iteration = 10 if len(sys.argv) < 3 else sys.argv[2]

    boxes = readFile(filePath)

    print(boxes)