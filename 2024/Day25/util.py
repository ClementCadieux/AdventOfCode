def readFile(path):
    file = open(path, "r")

    keys = []
    locks = []

    lines = file.readlines()

    lines = [line[:-1] if line[-1] == "\n" else line for line in lines]

    lines = [list(line) for line in lines]

    currentGroup = []

    for line in lines:
        if line == []:
            currentGroup = processGroup(keys, locks, currentGroup)
        else:
            currentGroup.append(line)
    
    processGroup(keys, locks, currentGroup)

    return (keys, locks)

def processGroup(keys, locks, currentGroup):
    isLock = currentGroup[0][0] == "#"

    group = [0, 0, 0, 0, 0]

    iRange = range(1, len(currentGroup)) if isLock else range(len(currentGroup) - 2, -1, -1)

    for i in iRange:
        for j in range(len(currentGroup[i])):
            if currentGroup[i][j] == "#":
                group[j] += 1

    if isLock:
        locks.append(group)
    else:
        keys.append(group)
            
    currentGroup = []
    return currentGroup
            