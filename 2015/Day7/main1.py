from util import readFile
import sys

def updateCircuit(circuit, output, seen):
    if output in seen:
        return circuit[output]

    newSegment = circuit[output]

    if len(newSegment) == 2:
        if newSegment[1].isalpha():
            updateCircuit(circuit, newSegment[1], seen)
            newSegment[1] = circuit[newSegment[1]]

        newSegment = ~int(newSegment[1])

        if newSegment < 0:
            newSegment += 65536
    elif len(newSegment) == 3:

        changedLeft = isinstance(newSegment[0], int)
        changedRight = isinstance(newSegment[2], int)

        if newSegment[0].isalpha():
            updateCircuit(circuit, newSegment[0], seen)
            newSegment[0] = circuit[newSegment[0]]
            changedLeft = isinstance(newSegment[0], int)
        else:
            changedLeft = True
            newSegment[0] = int(newSegment[0])
        
        if not changedLeft and newSegment[0].isdecimal():
            changedLeft = True
            newSegment[0] = int(newSegment[0])

        if newSegment[2].isalpha():
            updateCircuit(circuit, newSegment[2], seen)
            newSegment[2] = circuit[newSegment[2]]
            changedRight = isinstance(newSegment[2], int)
        else:
            changedRight = True
            newSegment[2] = int(newSegment[2])
        
        if not changedRight and  newSegment[2].isdecimal():
            changedRight = True
            newSegment[2] = int(newSegment[2])

        if changedRight and changedLeft:
            op = newSegment[1]

            match op:
                case "AND":
                    newSegment = newSegment[0] & newSegment[2]
                case "OR":
                    newSegment = newSegment[0] | newSegment[2]
                case "LSHIFT":
                    newSegment = newSegment[0] << newSegment[2]
                case "RSHIFT":
                    newSegment = newSegment[0] >> newSegment[2]

            if newSegment < 0:
                newSegment += 65536
    else:
        if newSegment[0].isalpha():
            newSegment[0] = updateCircuit(circuit, newSegment[0], seen)

        newSegment = int(newSegment[0])
        
        if newSegment < 0:
            newSegment += 65536
    

    circuit[output] = newSegment
    seen.add(output)

    return circuit[output]


if __name__ == "__main__":
    filePath = "2015\\Day7\\test.txt" if len(sys.argv) < 2 else sys.argv[1]

    circuit = readFile(filePath)

    seen = set()

    for output in circuit:
        updateCircuit(circuit, output, seen)

    if filePath == ".\\input.txt":
        print(circuit["a"])
    else:
        print(circuit)