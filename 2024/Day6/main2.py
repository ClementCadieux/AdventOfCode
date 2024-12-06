import main1 as base

def getDirToLook(lines, corner):
    i,j = corner

    dirAtCorner = lines[i][j]

    dirToLook = ""

    match dirAtCorner:
        case "v":
            dirToLook = ">"
        case ">":
            dirToLook = "^"
        case "^":
            dirToLook = "<"
        case "<":
            dirToLook = "v"

    return dirToLook

if __name__ == "__main__":
    lines = base.readFile("2024\\Day6\\test.txt")

    i, j = base.findGuard(lines)

    lines = base.processGuard(lines, i, j)

    corners = base.corners

    for corner in corners:
        dirToLook = getDirToLook(lines, corner)



    

