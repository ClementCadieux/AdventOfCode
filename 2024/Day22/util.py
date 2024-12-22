def readFile(path):
    file = open(path, "r")

    lines = file.readlines()

    lines = [int(line) for line in lines]

    return lines

def calcNum(num):
    mixVal = num*64
    num = num^mixVal
    num %= 16777216

    mixVal = int(num/32)
    num = num^mixVal
    num %= 16777216

    mixVal = num*2048
    num = num^mixVal
    num %= 16777216

    return num

