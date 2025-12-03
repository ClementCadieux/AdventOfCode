from util import readFile
import sys

if __name__ == "__main__":
    filePath = "2025\\Day3\\test.txt" if len(sys.argv) == 1 else sys.argv[1]

    banks = readFile(filePath)

    total = 0

    for bank in banks:
        max = -1
        max2 = -1

        for i in range(len(bank)):
            battery = bank[i]

            if battery > max and i != len(bank) - 1:
                max = battery
                max2 = -1
            elif battery > max2:
                max2 = battery
        
        val = max*10 + max2

        total += val
    
    print(total)