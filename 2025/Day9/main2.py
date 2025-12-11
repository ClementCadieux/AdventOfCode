from util import readFile
import sys

def get_size(x1, y1, x2, y2):
    x = abs(x1 - x2) + 1
    y = abs(y1 - y2) + 1
    return x * y

def maxSize(edges, sizes):
    for size, (x1, y1), (x2, y2) in sizes:
        y1, y2 = sorted((y1, y2))
        if not any(
            (x4 > x1 and x3 < x2 and y4 > y1 and y3 < y2)
            for (x3, y3), (x4, y4) in edges
        ):
            return size

if __name__ == "__main__":
    filePath = "2025\\Day9\\test.txt" if len(sys.argv) < 2 else sys.argv[1]

    redTiles = readFile(filePath)

    edges = []
    sizes = []
    for i in range(len(redTiles)):
        edges.append(sorted((redTiles[i], redTiles[i-1])))
        for j in range(i+1, len(redTiles)):
            c1, c2 = sorted((redTiles[i], redTiles[j]))
            sizes.append((get_size(*c1, *c2), c1, c2))

    maxArea = 0

    edges.sort(reverse=True, key=lambda e: get_size(*e[0], *e[1]))
    sizes.sort(reverse=True)

    print(maxSize(edges, sizes))