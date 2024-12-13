import main1 as base

if __name__ == "__main__":
    machines = base.readFile("2024\\Day13\\test.txt")

    for machine in machines:
        machine[2] = (machine[2][0] * 10000000000000, machine[2][1] * 10000000000000)

    