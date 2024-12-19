import sys
import util
import time

args = sys.argv

filePath = "2024\\Day19\\test.txt" if len(args) == 1 else args[1]

start = time.time()

towelsByFirst, designs = util.readFile(filePath)

count = 0

for design in designs:
    cache = [-1 for i in range(len(design))]
    count += util.countAllDesigns(design, 0, towelsByFirst, cache)

print(count)

end = time.time()

print(end - start)