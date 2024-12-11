import main1 as base

if __name__ == "__main__":
    line = base.readFile("2024\\Day11\\input.txt")

    total = 0

    for num in line:
        total += base.processNum(num, 75)
    
    print(total)