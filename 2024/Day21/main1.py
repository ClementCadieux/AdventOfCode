import sys
import util
import time

args = sys.argv

filePath = "2024\\Day21\\test.txt" if len(args) == 1 else args[1]

startTime = time.time()

codes = util.readFile(filePath)

sequenceDict = util.buildSequenceDict()

code = codes[0]

codeSequence = util.buildNextSequence(code, sequenceDict)

print(codeSequence)