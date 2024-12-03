import functools

def readFile(path):
    file = open(path, "r")

    grid = []

    line = file.readline()

    while line != "":
        if line[-1] == "\n":
            line = line[:-1]

        grid.append(line)

        line = file.readline()

    return grid

def separateGroupList(grid):
    records = []
    groups = []

    for line in grid:
        splitGroups = line.split(" ")

        record = splitGroups[0]

        group = splitGroups[1]

        groupsArr = [int(i) for i in group.split(",")]

        records.append(record)
        groups.append(groupsArr)


    return records, groups

@functools.lru_cache(maxsize=None)
def process(record, groups):

    if not groups:
        return 1 if "#" not in record else 0
    
    if len(record) == 0:
        return 0

    nextCharacter = record[0]
    nextGroup = groups[0]

    if nextCharacter == "#":
        return pound(record, groups, nextGroup)
    elif nextCharacter == ".":
        return dot(record, groups)
    
    return dot(record, groups) + pound(record, groups, nextGroup)

def pound(record, groups, nextGroup):
    thisGroup = record[:nextGroup]
    thisGroup = thisGroup.replace("?", "#")

    if thisGroup != nextGroup * "#":
        return 0
    
    if len(record) == nextGroup:
        return 1 if len(groups) == 1 else 0
    
    if record[nextGroup] in "?.":
        return process(record[nextGroup + 1:], groups[1:])
    
    return 0


def dot(record, groups):
    return process(record[1:], groups)

if __name__ == "__main__":
    grid = readFile("Day12\\input.txt")

    records, groups = separateGroupList(grid)
    
    groups = [tuple(group) for group in groups]

    output = 0

    for i in range(len(records)):
        output += process(records[i], groups[i])

    print(output)
    