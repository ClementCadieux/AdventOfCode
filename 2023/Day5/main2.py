def readFile(path):
    file = open(path, "r")

    lines = file.readlines()

    lines = [line.replace("\n", "") for line in lines if line != "\n"]

    seedLine = lines[0]

    seedsStr = seedLine.split(":")[1].strip()

    seeds = [int(seed) for seed in seedsStr.split(" ")]

    newSeeds = []

    for i in range(len(seeds)):
        if i % 2 == 1:
            seeds[i] += seeds[i - 1]
            newSeeds.append((seeds[i - 1], seeds[i]))

    seeds = newSeeds

    return (seeds, lines)    

if __name__ == "__main__":
    seeds, lines = readFile("Day5\\test1.txt")

    
