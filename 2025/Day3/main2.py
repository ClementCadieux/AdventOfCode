from util import readFile
import sys

if __name__ == "__main__":
    filePath = "2025\\Day3\\test.txt" if len(sys.argv) == 1 else sys.argv[1]

    banks = readFile(filePath)

    total = 0

    for bank in banks:   
        val = bank[0]

        toAdd = 11

        for i in range(1, len(bank)):
            battery = bank[i]
            
            while val > 0 and battery > val % 10 and toAdd < len(bank) - i:
                val = int(val/10)
                toAdd += 1
            
            if toAdd > 0:
                val *= 10
                val += battery
                toAdd -= 1
        
        total += val
    
    print(total)
