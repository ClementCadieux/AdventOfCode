import main1 as base
import functools

@functools.lru_cache(maxsize=None)
def isValid(total, curr, currInd, vals):
    if currInd == len(vals):
        return total == curr
    
    if curr > total:
        return False
    
    mulRes = isValid(total, curr * vals[currInd], currInd + 1, vals)

    if mulRes:
        return True
    
    addRes = isValid(total, curr + vals[currInd], currInd + 1, vals)

    if addRes:
        return True
    
    currStr = str(curr)
    nxtStr = str(vals[currInd])

    return isValid(total, int(currStr + nxtStr), currInd + 1, vals)

if __name__ == "__main__":
    lines = base.readFile("2024\\Day7\\input.txt")
    
    total = 0

    for key in lines.keys():
        vals = lines[key]
        intKey = int(key)

        if isValid(intKey, vals[0], 1, vals):
            total += intKey

    print(total)