import sys
import util
import time

args = sys.argv

filePath = "2024\\Day19\\test.txt" if len(args) == 1 else args[1]

start = time.time()

towelsByFirst, designs = util.readFile(filePath)

count = 0

for design in designs:
    cache = [True for i in range(len(design))]
    valid = util.possibleDesign(design, 0, towelsByFirst, cache)
    if valid:
        count += 1

print(count)

end = time.time()

print(end - start)