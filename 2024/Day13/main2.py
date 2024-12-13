import main1 as base

def calcOptPrice(machine):
    left = machine[1]
    right = machine[0]
    prize = machine[2]

    aCoef = right[0] - right[1]
    bCoef = left[0] - left[1]
    prizeSub = prize[0] - prize[1]

    prizeStep = prizeSub/aCoef
    bCoef /= aCoef

    bPress = (prize[0] - (right[0] * prizeStep)) / (left[0] - (right[0] * bCoef))
    aPress = prizeStep - (bCoef * bPress)

    if bPress % 1 != 0 or aPress % 1 != 0:
        return 0
    
    return 3*aPress + bPress

if __name__ == "__main__":
    machines = base.readFile("2024\\Day13\\test.txt")

    total = 0

    for machine in machines:
        machine[2] = (machine[2][0] + (10 ** 13), machine[2][1] + (10 ** 13))
        price = calcOptPrice(machine)
        print(price)
        total += price
    
    print(total)