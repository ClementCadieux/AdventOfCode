import sys
import util
import time

start = time.time()

args = sys.argv

filePath = "2024\\Day16\\test3.txt" if len(args) == 1 else args[1]

lines = util.readFile(filePath)

scores = [[0 for tile in line] for line in lines]



finalScore = scores[-2][1]
total = 0

for line in scores:
    for tile in line:
        if tile == finalScore:
            total += 1

print(total + 1)

end = time.time()

print(end - start)