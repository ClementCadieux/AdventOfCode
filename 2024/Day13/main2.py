import main1 as base
import time

if __name__ == "__main__":
    start = time.time()

    machines = base.readFile("2024\\Day13\\input.txt")

    total = 0

    for machine in machines:
        machine[2] = (machine[2][0] + (10 ** 13), machine[2][1] + (10 ** 13))
        price = base.calcOptPrice(machine)
        total += price
    
    print(total)

    end = time.time()

    print(end - start)