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

def getTotal(getDirToLook, lines, corners):
    total = 0

    for corner in corners:
        dirToLook = getDirToLook(lines, corner)

        i,j = corner

        match dirToLook:
            case ">":
                if i != 0:
                    for idx in range(j, -1, -1):
                        if lines[i][idx] == "^" and lines[i - 1][idx] != "#":
                            total += 1
                        elif lines[i][idx] == "#":
                            break
            
            case "^":
                if j != 0:
                    for idx in range(i, len(lines)):
                        if lines[idx][j] == "<" and lines[idx][j - 1] != "#":
                            total += 1
                        elif lines[idx][j] == "#":
                            break

            case "<":
                if i != len(lines) - 1:
                    for idx in range(j, len(lines[i])):
                        if lines[i][idx] == "v" and lines[i + 1][idx] != "#":
                            total += 1
                        elif lines[i][idx] == "#":
                            break

            case "v":
                if j != len(lines[i]) - 1:
                    for idx in range(i, -1, -1):
                        if lines[idx][j] == ">" and lines[idx][j + 1] != "#":
                            total += 1
                        elif lines[idx][j] == "#":
                            break

if __name__ == "__main__":
    lines = base.readFile("2024\\Day6\\test.txt")

    i, j = base.findGuard(lines)

    lines = base.processGuard(lines, i, j)

    corners = base.corners

    total = getTotal(getDirToLook, lines, corners)
    



    

