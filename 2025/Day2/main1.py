import sys
from util import readFile

if __name__ == "__main__":
    filePath = "2025\\Day2\\test.txt" if len(sys.argv) == 1 else sys.argv[1]

    ranges = readFile(filePath)
    
    invalids = []

    for idRange in ranges:
        start = int(idRange[0])
        end = int(idRange[1])

        for i in range(start, end + 1):
            iStr = str(i)

            firstHalf = iStr[:int(len(iStr)/2)]
            secondHalf = iStr[int(len(iStr)/2):]

            if firstHalf == secondHalf:
                invalids.append(i)

    total = sum(invalids)
    
    print(total)
    
    