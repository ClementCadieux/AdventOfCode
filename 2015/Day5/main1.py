import sys
from util import readFile

vowels = {"a", "e", "i", "o", "u"}
illegalStrings = {"ab", "cd", "pq", "xy"}

def isNice(line):
    vowelCount = 0
    repeat = False

    for i in range(len(line)):
        char = line[i]
        if i != 0:
            prev = line[i - 1]

            if char == prev:
                repeat = True
            else:
                match char:
                    case "b":
                        if prev == "a":
                            return False
                    case "d":
                        if prev == "c":
                            return False
                    case "q":
                        if prev == "p":
                            return False
                    case "y":
                        if prev == "x":
                            return False
        
        if vowelCount < 3 and char in vowels:
            vowelCount += 1

    return vowelCount == 3 and repeat


if __name__ == "__main__":
    filePath = "2015\\Day5\\test.txt" if len(sys.argv) < 2 else sys.argv[1]

    lines = readFile(filePath)

    count = 0

    for line in lines:
        if isNice(line):
            count += 1

    print(count)