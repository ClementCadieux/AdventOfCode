from util import readFile, getProblems
import sys

def computeProblem(problem):
    op = problem[1]

    solution = 0

    if op == "+":
        solution = sum(problem[0])
    else:
        nums = problem[0]
        solution = 1

        for num in nums:
            solution *= num

    return solution

if __name__ == "__main__":
    filePath = "2025\\Day6\\test.txt" if len(sys.argv) < 2 else sys.argv[1]

    lines = readFile(filePath)

    problems = getProblems(lines)

    total = 0

    for problem in problems:
        solution = computeProblem(problem)

        total += solution

    print(total)