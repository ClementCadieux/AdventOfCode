import sys
import util
import time

args = sys.argv

filePath = "2024\\Day21\\test.txt" if len(args) == 1 else args[1]

startTime = time.time()

codes = util.readFile(filePath)

sequenceDict = util.buildSequenceDict()

score = 0

sequence = ""

for code in codes:
    sequence = code
    for i in range(3):
        sequence = util.buildNextSequence(sequence, sequenceDict)

    score += util.codeScore(code, len(sequence))

print(score)