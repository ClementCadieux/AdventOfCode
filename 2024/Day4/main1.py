import re

def readFile(path):
    file = open(path, "r")

    lines = file.readlines()

    lines = [line[:-1] if line[-1] == "\n" else line for line in lines]

    return lines

xmas = "XMAS"
samx = "SAMX"

if __name__ == "__main__":
    lines = readFile("2024\\Day4\\test.txt")
