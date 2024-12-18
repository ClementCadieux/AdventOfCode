import main1 as base1
import time

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
            
            for j in range(len(emptysByLength[newEmptyLength])):
                if emptysByLength[newEmptyLength][j] > newEmptyIndex:
                    emptysByLength[newEmptyLength].insert(j, newEmptyIndex)
                    break
                if j == len(emptysByLength[newEmptyLength]) - 1:
                    emptysByLength[newEmptyLength].append(newEmptyIndex)
        
    return filesMetaData

def checkSum(filesMetaData):
    score = 0
    for file in filesMetaData:
        startIndex = file[2]
        length = file[0]
        val = file[1]

        mul = (length * startIndex) + (length * int((length - 1)/2))

        score += val * mul

    return score

if __name__ == "__main__":
    begin = time.time()
    line = base1.readFile("2024\\Day9\\input.txt")

    emptysByLength, filesMetaData = getLineInfo(line)

    filesMetaData = compact(emptysByLength, filesMetaData)

    score = checkSum(filesMetaData)

    print(score)

    end = time.time()

    print(end - begin)