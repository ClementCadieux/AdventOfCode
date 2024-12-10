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
            filesMetaData.append((length, int(i / 2), currLength))
        else:
            while len(emptysByLength) <= length:
                emptysByLength.append([])
            
            emptysByLength[length].append(currLength)
        
        currLength += length

    
    return emptysByLength, filesMetaData


if __name__ == "__main__":
    line = base1.readFile("2024\\Day9\\test.txt")

    emptysByLength, filesMetaData = getLineInfo(line)

    print(emptysByLength)
    print(filesMetaData)