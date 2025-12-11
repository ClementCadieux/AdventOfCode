from util import readFile, pathsToTarget
import sys

if __name__ == "__main__":
    args = sys.argv
    filePath = "2025\\Day11\\test2.txt" if len(args) < 2 else args[1]

    circuit = readFile(filePath)

    cache = {}

    fromSvrToFFT = pathsToTarget(circuit, "svr", "fft", ["dac", "out"])
    fromSvrToDAC = pathsToTarget(circuit, "svr", "dac", ["fft", "out"])
    fromFFTToDAC = pathsToTarget(circuit, "fft", "dac", ["out"])
    fromDACToFFT = pathsToTarget(circuit, "dac", "fft", ["out"])
    fromFFTToOut = pathsToTarget(circuit, "fft", "out", ["dac"])
    fromDACToOut = pathsToTarget(circuit, "dac", "out", ["fft"])

    total = (fromSvrToFFT * fromFFTToDAC * fromDACToOut) + (fromSvrToDAC  * fromDACToFFT * fromFFTToOut)

    print(total)