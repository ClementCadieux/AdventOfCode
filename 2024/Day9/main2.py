import main1 as base

def compact(fileMetaDatas, emptyLengths):
    fileIndex = len(fileMetaDatas) - 1

    while fileIndex >= 0:
        file = fileMetaDatas[fileIndex]

        emptyIdx = 0

        while emptyIdx < len(emptyLengths) and emptyLengths[emptyIdx][0] < file[0]:
            empty = emptyLengths[emptyIdx]

            if empty[1] >= file[1]:
                fileMetaDatas[fileIndex] = (empty[0], file[1], file[2])
                emptyLengths[emptyIdx] = (empty[0] + file[1], empty[1] - file[1])
                if empty[1] == 0:
                    del emptyLengths[emptyIdx]
                break
            else:
                emptyIdx += 1

        fileIndex -= 1
    
    return fileMetaDatas, emptyLengths

def genLineInfo(line):
    emptyLengths = []
    fileMetaDatas = []

    currIndex = 0

    for i in range(len(line)):
        length = int(line[i])

        charId = int(i / 2) if i % 2 == 0 else "."

        if charId == ".":
            emptyLengths.append((currIndex, length))
        else:
            fileMetaDatas.append((currIndex, length, charId))

        currIndex += length
    
    return fileMetaDatas, emptyLengths

def genLine(lineMetadatas, emptyLengths):
    return None

if __name__ == "__main__":
    line = base.readFile("2024\\Day9\\test.txt")

    fileMetaDatas, emptyLengths = genLineInfo(line)

    fileMetaDatas, emptyLengths = compact(fileMetaDatas, emptyLengths)

    fileMetaDatas.sort(key=lambda x : x[0])

    print(fileMetaDatas)

    # resLine = genLine(fileMetaDatas, emptyLengths)

    # total = base.checkSum(resLine)

    # print(total)
