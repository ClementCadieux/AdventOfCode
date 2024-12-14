import sys
import util

filePath = sys.argv[1]

line = util.readFile(filePath)

floor = 0
for i in range(len(line)):
    if line[i]  == '(':
        floor += 1
    else:
        floor -= 1

    if floor < 0:
        print(i + 1)
        break

print(floor)