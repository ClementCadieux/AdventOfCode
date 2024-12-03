import main1 as basefunc
import math

def gcd(nums):
    curr = nums[0]

    for i in range(1, len(nums)):
        curr = abs(curr * nums[i]) // math.gcd(curr, nums[i])

    return curr

if __name__ == "__main__":
    fileRead = basefunc.readFile("Day8\\input.txt")

    network = fileRead[1]

    startingNodes = [node for node in network if node[2] == "A"]

    steps = []

    for node in startingNodes:
        currSteps = 0
        currNode = node

        while(currNode[2] != "Z"):
            currNode = basefunc.nextNode(currNode, fileRead[0], currSteps, network)
            currSteps += 1

        steps.append(currSteps)

    allDone = gcd(steps)

    print(allDone)