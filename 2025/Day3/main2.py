from util import readFile
import sys

if __name__ == "__main__":
    filePath = "2025\\Day3\\test.txt" if len(sys.argv) == 1 else sys.argv[1]

    banks = readFile(filePath)

    total = 0

    for bank in banks:   
        val = bank[0]

        lastSeen = bank[0]

        toAdd = 11

        for i in range(1, len(bank)):
            battery = bank[i]

            if len(bank) - i == toAdd and toAdd > 0:
                toAdd -= 1
                val *= 10
                val += battery
                lastSeen = battery
            elif battery > lastSeen:
                val -= lastSeen
                val += battery
                lastSeen = battery
            elif toAdd > 0:
                toAdd -= 1
                val *= 10
                val += battery
                lastSeen = battery

        total += val
    
    print(total)
