import main1 as base

def calcRegionInfo(lines):
    return None

if __name__ == "__main__":
    lines = base.readFile("2024\\Day12\\test.txt")

    lines  = base.makeRegionsNumbers(lines)

    regionInfo = calcRegionInfo(lines)

    cost = base.calcCost(regionInfo)

    print(cost)