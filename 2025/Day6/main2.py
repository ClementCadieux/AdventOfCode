from util import readFile2, getProblems2
import sys
from main1 import computeProblem

if __name__ == "__main__":
    filePath = "2025\\Day6\\test.txt" if len(sys.argv) < 2 else sys.argv[1]

    lines = readFile2(filePath)

    problems = getProblems2(lines)

    total = 0

    for problem in problems:
        solution = computeProblem(problem)

        total += solution

    print(total)