import pygame
from pygame.locals import *
import time
import statistics as st

def readFile(path):
    file = open(path, "r")

    lines = file.readlines()

    lines = [line[:-1] if line[-1] == "\n" else line for line in lines]

    nodeIndex = {}
    nodes = []

    inWires = True

    for line in lines:
        if inWires:
            if line == "":
                inWires = False
            else:
                splitLine = line.split(":")

                node = splitLine[0]
                value = True if splitLine[1].strip() == "1" else False

                nodeIndex[node] = len(nodes)
                nodes.append(value)
        else:
            splitLine = line.split("->")

            leftSplit = splitLine[0].split(" ")

            targetNode = splitLine[1].strip()

            opLeftNode = leftSplit[0]
            opRightNode = leftSplit[2]

            op = leftSplit[1]

            if opLeftNode not in nodeIndex:
                nodeIndex[opLeftNode] = len(nodes)
                nodes.append(-1)

            if opRightNode not in nodeIndex:
                nodeIndex[opRightNode] = len(nodes)
                nodes.append(-1)

            if targetNode not in nodeIndex:
                nodeIndex[targetNode] = len(nodes)
                nodes.append(-1)

            nodes[nodeIndex[targetNode]] = [opLeftNode, op, opRightNode]

    return (nodes, nodeIndex)

def processOps(nodes, nodeIndex):
    changed = True

    while changed:
        changed = False

        for i in range(len(nodes)):
            node = nodes[i]
            if not isinstance(node, bool):
                leftNode = nodes[nodeIndex[node[0]]]
                rightNode = nodes[nodeIndex[node[2]]]

                validOp = isinstance(leftNode, bool) and isinstance(rightNode, bool)

                if validOp:
                    match node[1]:
                        case "AND":
                            node = leftNode and rightNode
                        case "XOR":
                            node = leftNode != rightNode
                        case "OR":
                            node = leftNode or rightNode

                    changed = True
                    nodes[i] = node

def getBinary(nodes, nodeIndex, letter):
    res = ""

    num = 0

    node = letter + ("0" if num < 10 else "") + str(num)

    while node in nodeIndex:
        value = nodes[nodeIndex[node]]

        bit = "1" if value else "0"

        res = bit + res

        num += 1

        node = letter + ("0" if num < 10 else "") + str(num)
    
    return res

def visualDisplay(nodes, nodeIndex):
    pygame.init()

    font = pygame.font.SysFont(None, 15)

    window = pygame.display.set_mode((1372.5, 850.5))

    window.fill((255, 255, 255))

    seenNodes = set()

    for node in nodeIndex:
        drawNode(node, seenNodes, window, nodeIndex, nodes, font)

    pygame.display.update()
    time.sleep(300)
        
def drawNode(node, seenNodes, window, nodeIndex, nodes, font):
    if node in seenNodes:
        return
    
    height = 0
    width = 10

    if node[0] == "x" or node[0] == "y":
        height = 121.5
        num = int(node[1:])
        width += 30*num

        if node[0] == "y":
            width += 15

        pygame.draw.circle(window, (0, 0, 0), [width, height], 5, 2)

        return (height, width)
    elif node[0] == "z":
        height = 729
        num = int(node[1:])
        width += 30*num

        value = nodes[nodeIndex[node]]

        leftNode = value[0]
        rightNode = value[2]

        if leftNode not in seenNodes:
            leftHeight, leftWidth = drawNode(leftNode, seenNodes, window, nodeIndex, nodes, font)
        if rightNode not in seenNodes:
            rightHeight, rightWidth = drawNode(rightNode, seenNodes, window, nodeIndex, nodes, font)
        
        op = value[1]

        color = None

        match op:
            case "XOR":
                color = (255, 0, 0)
            case "AND":
                color = (0, 255, 0)
            case "OR":
                color = (0, 0, 255)

        pygame.draw.line(window, color, [leftWidth, leftHeight], [width, height], 2)

        pygame.draw.line(window, color, [rightWidth, rightHeight], [width, height], 2)

        pygame.draw.circle(window, (0, 0, 0), [width, height], 10, 2)
    
        text = font.render(node, True, (0, 0, 0))

        window.blit(text, text.get_rect(center = (width, height + 15)))        

        return (height, width)
    else:
        height = 425.25

        value = nodes[nodeIndex[node]]

        leftNode = value[0]
        rightNode = value[2]

        if leftNode not in seenNodes:
            leftHeight, leftWidth = drawNode(leftNode, seenNodes, window, nodeIndex, nodes, font)
        if rightNode not in seenNodes:
            rightHeight, rightWidth = drawNode(rightNode, seenNodes, window, nodeIndex, nodes, font)
        
        op = value[1]

        color = None

        match op:
            case "XOR":
                color = (255, 0, 0)
            case "AND":
                color = (0, 255, 0)
            case "OR":
                color = (0, 0, 255)
        
        width = st.mean([leftWidth, rightWidth])

        pygame.draw.line(window, color, [leftWidth, leftHeight], [width, height], 2)

        pygame.draw.line(window, color, [rightWidth, rightHeight], [width, height], 2)

        pygame.draw.circle(window, (0, 0, 0), [width, height], 3, 2)

        return height,width
