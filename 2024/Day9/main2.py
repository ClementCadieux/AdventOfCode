import main1 as base

def compact(fileMetaDatas, emptyLengths, totalLength):
    resLine = []

    leftFileIndex = 0
    rightFileIndex = len(fileMetaDatas) - 1
    emptyIndex = 0

    while leftFileIndex < rightFileIndex:
        currIndex = len(resLine)

        leftFile = fileMetaDatas[leftFileIndex]
        rightFile = fileMetaDatas[rightFileIndex]
        nextEmpty = emptyLengths[emptyIndex]

        if currIndex == leftFile[0]

    return resLine

def genLineInfo(line):
    emptyLengths = []
    fileMetaDatas = []

    currIndex = 0

    for i in range(len(line)):
        length = int(line[i])

        charId = str(int(i / 2)) if i % 2 == 0 else "."

        if charId == ".":
            emptyLengths.append((currIndex, length))
        else:
            fileMetaDatas.append((currIndex, length))

        currIndex += length
    
    return fileMetaDatas, emptyLengths, currIndex

if __name__ == "__main__":
    line = base.readFile("2024\\Day9\\test2.txt")

    fileMetaDatas, emptyLengths, totalLength = genLineInfo(line)

    resLine = compact(fileMetaDatas, emptyLengths, totalLength)

    total = base.checkSum(resLine)

    print(total)
