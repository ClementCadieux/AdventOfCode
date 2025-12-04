from util import readFile
import sys
from main1 import updateCircuit
import copy

if __name__ == "__main__":
    filePath = "2015\\Day7\\test.txt" if len(sys.argv) < 2 else sys.argv[1]

    circuit = readFile(filePath)
    circuitCopy = copy.deepcopy(circuit)

    seen = set()

    for output in circuit:
        updateCircuit(circuit, output, seen)

    circuitCopy["b"] = circuit["a"]

    seen = set()
    seen.add("b")

    for output in circuitCopy:
        updateCircuit(circuitCopy, output, seen)

    if filePath == ".\\input.txt":
        print(circuitCopy["a"])
    else:
        print(circuit)