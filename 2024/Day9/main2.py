def compact(lineMap):
    return None

def genLineInfo(line):
    emptyLengths = {}
    fileMetaDatas = {}

    currIndex = 0

    for i in range(len(line)):
        length = int(line[i])

        charId = str(int(i / 2)) if i % 2 == 0 else "."

        if charId == ".":
            emptyLengths[str(currIndex)] = length
        else:
            fileMetaDatas[charId] = (length, currIndex)

        currIndex += length
    
    return fileMetaDatas, emptyLengths
