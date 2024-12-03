file = open("Day5\\input1.txt", 'r')

def mapFromLine(mapStr):
    if(mapStr == "\n" or mapStr == ""):
        return -1

    vals = mapStr.split(" ")
    start = int(vals[1])
    end = int(vals[1]) + int(vals[2]) - 1
    delta = int(vals[0]) - int(vals[1])

    return [start, end, delta]


seedsLine = file.readline()
seedsStr = seedsLine[7:]
seeds = seedsStr.split(" ")

for i in range(len(seeds)):
    seeds[i] = int(seeds[i])

def convert_step(file):
    line = file.readline()
    while(line == "\n" or line[0].isalpha()):
        line = file.readline()

    currLine = mapFromLine(line)
    currMap = []

    while(currLine != -1):
        currMap.append(currLine)
        currLine = mapFromLine(file.readline())
    
    for i in range(len(seeds)):
        for map in currMap:
            if seeds[i] >= map[0] and seeds[i] <= map[1]:
                seeds[i] += map[2]
                break

    
while (file.readline() != ""):
    convert_step(file)

print(min(seeds))

