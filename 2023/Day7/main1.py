file = open("Day7\\input.txt", 'r')

cardValues = {
    "A": 12,
    "K": 11,
    "Q": 10,
    "J": 9,
    "T": 8,
    "9": 7,
    "8": 6,
    "7": 5,
    "6": 4,
    "5": 3,
    "4": 2,
    "3": 1,
    "2": 0
}

def getCardFreq(hand):
    cardFreq = {}
    for char in hand:
        if char in cardFreq:
            cardFreq[char] += 1
        else:
            cardFreq[char] = 1
    
    return cardFreq

def getHandType(cardFreq):
    freqLength = len(cardFreq)
    handType = 0

    match freqLength:
        case 1:
            handType = 7
        case 2:
            for card in cardFreq:
                if cardFreq[card] == 1 or cardFreq[card] == 4:
                    handType = 6
                    break
                else:
                    handType = 5
                    break
        case 3:
            for card in cardFreq:
                if cardFreq[card] == 3:
                    handType = 4
                    break
                elif cardFreq[card] == 2:
                    handType = 3
                    break
        case 4:
            handType = 2
        case 5:
            handType = 1
    
    return handType
        
def handCardValues(hand, cardValues):

    # hand = sorted(hand, reverse=True, key=lambda x : (cardFreq[x], cardValues[x]))

    values = []
    for card in hand:
        values.append(cardValues[card])

    return values

def analyseHands(hands):
    handsAnalysed = []

    for handBetPair in hands:
        hand = handBetPair[0]
        cardFreq = getCardFreq(hand)
        handType = getHandType(cardFreq)
        values = handCardValues(hand, cardValues)
        bet = handBetPair[1]

        handsAnalysed.append([hand, (handType, values), bet])

    handsAnalysed.sort(key=lambda x: x[1])
    return handsAnalysed

def readFromFile(file):
    hands = []

    line = file.readline()

    while(line != ""):
        handLine = line.split(" ")
        handLine[1] = int(handLine[1])
        hands.append(handLine)

        line = file.readline()
    return hands

if(__name__ == "__main__"):
    hands = readFromFile(file)

    handsAnalysed = analyseHands(hands)

    sum = 0

    for i in range(len(handsAnalysed)):
        sum += (i+1) * handsAnalysed[i][2]

    print(sum)


