import main1 as base1
import main2 as base2

def getLineInfo(line):
    emptysByLength = []
    filesMetaData = []
    currLength = 0

    for i in range(len(line)):
        length = int(line[i])

        if length == 0:
            continue

        if i % 2 == 0:
            filesMetaData.append([length, int(i / 2), currLength])
        else:
            while len(emptysByLength) <= length:
                emptysByLength.append([])
            
            emptysByLength[length].append(currLength)
        
        currLength += length

    
    return emptysByLength, filesMetaData

def compact(emptysByLength, filesMetaData):
    for i in range(len(filesMetaData) - 1, -1, -1):
        file = filesMetaData[i]
        fileLength = file[0]
        fileIdx = file[2]

        minIdx = fileIdx
        emptysIdx = -1

        for j in range(fileLength, len(emptysByLength)):
            if len(emptysByLength[j]) > 0 and emptysByLength[j][0] < minIdx:
                emptysIdx = j
                minIdx = emptysByLength[j][0]
        
        if emptysIdx != -1:
            file[2] = minIdx

            newEmptyLength = emptysIdx - fileLength
            newEmptyIndex = minIdx + fileLength

            del emptysByLength[emptysIdx][0]
            emptysByLength[newEmptyLength].append(newEmptyIndex)

            emptysByLength[newEmptyLength].sort()
        
    return filesMetaData


if __name__ == "__main__":
    line = base1.readFile("2024\\Day9\\test.txt")

    emptysByLength, filesMetaData = getLineInfo(line)

    filesMetaData = compact(emptysByLength, filesMetaData)

    print(filesMetaData)