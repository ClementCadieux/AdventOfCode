import sys
import util
import time

start = time.time()

args = sys.argv

filePath = "2024\\Day18\\test.txt" if len(args) == 1 else args[1]
bound = 7 if len(args) == 1 else int(args[2])
sim = 12 if len(args) == 1 else int(args[3])

coordsList = util.readFile(filePath)

result = util.main(bound, sim, coordsList)

print(result)

end = time.time()

print(end - start)