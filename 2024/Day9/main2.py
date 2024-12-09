import main1 as base

def compact(fileMetaDatas, emptyLengths):
    
    
    return fileMetaDatas

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

    fileMetaDatas = compact(fileMetaDatas, emptyLengths)

    fileMetaDatas.sort(lambda x : x[0])

    resLine = genLine(fileMetaDatas, emptyLengths)

    total = base.checkSum(resLine)

    print(total)
