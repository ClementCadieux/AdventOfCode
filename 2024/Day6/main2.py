import main1 as base

def getDirToLook(lines, corner):
    i,j = corner

    dirAtCorner = lines[i][j]

    iBef = i - 1 if dirAtCorner == "<" else i + 1 if dirAtCorner == ">" else i
    jBef = j - 1 if dirAtCorner == "v" else j + 1 if dirAtCorner == "^" else j

    dirToLook = lines[iBef][jBef]

    return dirToLook

if __name__ == "__main__":
    lines = base.readFile("2024\\Day6\\test.txt")

    i, j = base.findGuard(lines)

    lines = base.processGuard(lines, i, j)

    corners = base.corners

    for corner in corners:
        getDirToLook(lines, corner)

    

