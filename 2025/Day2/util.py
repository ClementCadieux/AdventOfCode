def readFile(path):
    file = open(path, "r")

    ranges = []

    inputRanges = file.readline().split(",")

    for range in inputRanges:
        splitRange = range.split("-")

        start = splitRange[0]
        end = splitRange[1]

        rangeOutput = [start, end]

        ranges.append(rangeOutput)
    
    return ranges