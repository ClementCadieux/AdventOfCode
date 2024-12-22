import sys
import time
import util

args = sys.argv

filePath = "2024\\Day22\\test2.txt" if len(args) == 1 else args[1]

startTime = time.time()

nums = util.readFile(filePath)

changeSequences = []

allSequences = set()

for val in nums:
    num = val
    priceSequence = [num]
    changeSequenceDict = {}

    for i in range(2000):
        num, priceSequence, changeSequenceDict, allSequences = util.keepChangeSequence(num, priceSequence, changeSequenceDict, allSequences)

    changeSequences.append(changeSequenceDict)

maxTotal = 0

for sequence in allSequences:
    total = 0

    for changeSequenceDict in changeSequences:
        total += 0 if sequence not in changeSequenceDict else changeSequenceDict[sequence]

    if total > maxTotal:
        maxTotal = total

print(maxTotal)

endTime = time.time()

print(endTime - startTime)