import sys
import time
import util

args = sys.argv

filePath = "2024\\Day22\\test2.txt" if len(args) == 1 else args[1]

startTime = time.time()

nums = util.readFile(filePath)

num = 123
priceSequence = [num]
changeSequenceDict = {}

for i in range(11):
    num, priceSequence, changeSequenceDict = util.keepChangeSequence(num, priceSequence, changeSequenceDict)


for sequence in changeSequenceDict:
    print(sequence, changeSequenceDict[sequence])

endTime = time.time()

print(endTime - startTime)