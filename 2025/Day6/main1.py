from util import readFile, getProblems
import sys

if __name__ == "__main__":
    filePath = "2025\\Day6\\test.txt" if len(sys.argv) < 2 else sys.argv[1]

    lines = readFile(filePath)

    problems = getProblems(lines)

    total = 0

    for problem in problems:
        op = problem[1]

        solution = 0

        if op == "+":
            solution = sum(problem[0])
        else:
            nums = problem[0]
            solution = nums[0]*nums[1]*nums[2]

        total += solution

    print(total)