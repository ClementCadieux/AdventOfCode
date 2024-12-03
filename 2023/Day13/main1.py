def readFile(path):
    file = open(path, "r")

    allGrids = []

    currGrid = []

    for line in file.readlines():
        if line == "\n":
            allGrids.append(currGrid)
            currGrid = []
        else:
            currGrid.append(line[:-1] if line[-1] == "\n" else line)
    
    allGrids.append(currGrid)

    return allGrids

def gridToNums(allGrids):
    numGrids = []

    for grid in allGrids:
        numLines = []
        numCols = []
        for line in grid:
            numLines.append(lineToNum(line))
        
        for i in range(len(grid[0])):
            numCols.append(colToNum(grid, i))
        
        numGrids.append((numLines, numCols))

    return numGrids

def lineToNum(line):
    val = 0

    for i in range(len(line)):
        if line[i] == "#":
            val += 2**i
    
    return val

def colToNum(grid, i):
    val = 0

    for rowI in range(len(grid)):
        if grid[rowI][i] == "#":
            val += 2**rowI

    return val

def evalNumGrid(nums):
    stack = []
    revStack = []

    for i in range(len(nums)):
        val = nums[i]
        currInd = i

        while len(stack) != 0 and val == stack[-1]:
            revStack.append(stack.pop())
            currInd += 1

            if len(stack) == 0 or currInd == len(nums):
                return i

            val = nums[currInd]
        
        while len(revStack) > 0:
            stack.append(revStack.pop())
        
        stack.append(nums[i])

    return -1

if __name__ == "__main__":
    allGrids = readFile("Day13\\input.txt")

    numGrids = gridToNums(allGrids)

    val = 0

    for numGrid in numGrids:
        num = 100 * evalNumGrid(numGrid[0])

        if num == -100:
            num = evalNumGrid(numGrid[1])
        
        val += num
    
    print(val)

    