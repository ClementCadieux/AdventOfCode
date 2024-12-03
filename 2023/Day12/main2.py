import main1 as baseFuncts

def unfold(records, groups):
    for i in range(len(records)):
        baseRecord = records[i]
        baseGroup = groups[i]
        
        newRecord = ""
        newGroup = []

        for j in range(5):
            newRecord += baseRecord

            if j != 4:
                newRecord += "?"
            
            for x in baseGroup:
                newGroup.append(x)
            
        records[i] = newRecord
        groups[i] = newGroup
    
    return (records, groups)

if __name__ == "__main__":
    grid = baseFuncts.readFile("Day12\\input.txt")

    records, groups = baseFuncts.separateGroupList(grid)

    records, groups = unfold(records, groups)
    
    groups = [tuple(group) for group in groups]

    output = 0

    for i in range(len(records)):
        output += baseFuncts.process(records[i], groups[i])

    print(output)
    