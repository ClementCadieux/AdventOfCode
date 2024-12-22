import sys
import time
import util

args = sys.argv

filePath = "2024\\Day22\\test.txt" if len(args) == 1 else args[1]

nums = util.readFile(filePath)

print(nums)