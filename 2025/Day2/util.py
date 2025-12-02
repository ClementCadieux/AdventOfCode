def readFile(path):
    file = open(path, "r")

    ranges = []

    inputRanges = file.readline().split(",")

    for idRange in inputRanges:
        splitRange = idRange.split("-")

        start = splitRange[0]
        end = splitRange[1]

        rangeOutput = [start, end]

        ranges.append(rangeOutput)
    
    return ranges