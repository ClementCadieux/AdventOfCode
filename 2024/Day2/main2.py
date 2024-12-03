import main1 as baseFunc
import functools

@functools.lru_cache(maxsize=None)
def evalLine(line, prev, curr, dir, removed):
    if curr == len(line):
        return True

    if dir == None:
        dir = 1 if line[curr] > line[prev] else -1 if line[curr] < line[prev] else 0
        
        if dir == 0:
            if removed:
                return False

            removePrev = evalLine(line, prev + 1, curr + 1, None, True)

            if removePrev:
                return True

            return evalLine(line, prev, curr + 1, None, True)

    if line[curr] < line[prev] and dir == 1:
        return mistakeCheck(line, prev, curr, dir, removed)

    if line[curr] > line[prev] and dir == -1:
        return mistakeCheck(line, prev, curr, dir, removed)
      
    diffCheck = (line[curr] - line[prev]) * dir

    if diffCheck > 3 or diffCheck == 0:
        return mistakeCheck(line, prev, curr, dir, removed)

    prev = curr
    curr += 1
    return evalLine(line, prev, curr, dir, removed)

def mistakeCheck(line, prev, curr, dir, removed):
    if removed:
            return False
        
    removePrev = False

    if prev == 0:
        removePrev = evalLine(line, prev + 1, curr + 1, None, True)
    else:
        if prev == 1:
            removePrev = evalLine(line, prev, curr, None, True)
        if not removePrev:
            removePrev = evalLine(line, prev - 1, curr, dir if prev > 1 else None, True)
    
    if removePrev:
        return True

    return evalLine(line, prev, curr + 1, dir, True)

def getValidLines(reports):
    total = 0

    for line in reports:
        valid = evalLine(line, 0, 1, None, False)

        if valid:
            total += 1

    return total

if __name__ == "__main__":
    reports = baseFunc.readFile("2024\\Day2\\input.txt")

    reports = [tuple(report) for report in reports]

    total = getValidLines(reports)

    print(total)