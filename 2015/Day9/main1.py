from util import readFile
import sys

if __name__ == "__main__":
    filePath = "2015\\Day9\\test.txt" if len(sys.argv) < 2 else sys.argv[1]

    lines = readFile(filePath)

    
    