def compact(lineMap, filesByLength):
    for length in filesByLength:
        filesByLength[length].sort()
