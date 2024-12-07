import functools

def readFile(path):
    file = open(path, "r")

    line = file.readline()

    lines = {}

    while line != "":
        splitLine = line.split(":")

        key = splitLine[0]

        vals = splitLine[1][:-1] if splitLine[1][-1] == "\n" else splitLine[1]

        valsList = vals.split(" ")
        valsList = [x for x in valsList if x != ""]
        valsNumList = [int(val) for val in valsList]

        valsTup = tuple(valsNumList)

        lines[key] = valsTup

        line = file.readline()

    return lines

@functools.lru_cache(maxsize=None)
def isValid(total, curr, currInd, vals):
    if currInd == len(vals):
        return total == curr
    
    if curr > total:
        return False
    
    if curr == total:
        return False
    
    mulRes = isValid(total, curr * vals[currInd], currInd + 1, vals)

    if mulRes:
        return True
    
    return isValid(total, curr + vals[currInd], currInd + 1, vals)

if __name__ == "__main__":
    lines = readFile("2024\\Day7\\test.txt")

    total = 0

    for key in lines.keys():
        vals = lines[key]
        intKey = int(key)

        if isValid(intKey, vals[0], 1, vals):
            print(intKey)
            total += intKey

    print(total)