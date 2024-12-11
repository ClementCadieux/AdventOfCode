import functools

def readFile(path):
    file = open(path, "r")

    line = file.readline()

    splitLine = line.split(" ")

    intLine = [int(val) for val in splitLine]

    return intLine

@functools.lru_cache(maxsize=None)
def processNum(num, remaining):
    if remaining == 0:
        return 1
    
    if num == 0:
        return processNum(1, remaining - 1)
    
    strNum = str(num)
    length = len(strNum)

    if length % 2 != 0:
        return processNum(num * 2024, remaining - 1)
    
    return processNum(int(strNum[:int(length/2)]), remaining - 1) + processNum(int(strNum[int(length/2):]), remaining - 1)

if __name__ == "__main__":
    line = readFile("2024\\Day11\\input.txt")

    total = 0

    for num in line:
        total += processNum(num, 25)

    print(total)

