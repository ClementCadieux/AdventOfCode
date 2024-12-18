import sys
import util
import time

start = time.time()

args = sys.argv

filePath = "2024\\Day18\\test.txt" if len(args) == 1 else args[1]
bound = 7 if len(args) == 1 else int(args[2])

coordsList = util.readFile(filePath)

left = 0
right = len(coordsList)

while left < right - 1:    
    mid = int((left + right)/2)

    res = util.main(bound, mid, coordsList)



    if res == bound**2 + 1:
        right = mid
    else:
        left = mid

if left == right - 1:
    res = util.main(bound, left, coordsList)

    if res != bound**2 + 1:
        left = right

print(coordsList[left])    

end = time.time()

print(end - start)