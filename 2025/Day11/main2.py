from util import readFile, pathsToTarget
import sys

if __name__ == "__main__":
    args = sys.argv
    filePath = "2025\\Day11\\test2.txt" if len(args) < 2 else args[1]

    circuit = readFile(filePath)

    cache = {}

    fromSvrToFFT = pathsToTarget(circuit, "svr", "fft")
    fromSvrToDAC = pathsToTarget(circuit, "svr", "dac")
    fromFFTToDAC = pathsToTarget(circuit, "fft", "dac")
    fromDACToFFT = pathsToTarget(circuit, "dac", "fft")
    fromFFTToOut = pathsToTarget(circuit, "fft", "out")
    fromDACToOut = pathsToTarget(circuit, "dac", "out")

    total = (fromSvrToFFT + fromFFTToDAC + fromDACToOut)

    print(total)