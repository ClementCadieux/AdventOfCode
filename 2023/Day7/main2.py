import main1 as baseMethods

file = open("Day7\\input.txt", 'r')

cardValues = {
    "A": 12,
    "K": 11,
    "Q": 10,
    "T": 9,
    "9": 8,
    "8": 7,
    "7": 6,
    "6": 5,
    "5": 4,
    "4": 3,
    "3": 2,
    "2": 1,
    "J": 0
}

def handleJokers(cardFreq):
    highestFreq = 0
    highestFreqCard = ""

    for card in cardFreq:
        if (highestFreq == 0 or cardFreq[card] > highestFreq) and card != "J":
            highestFreqCard = card
            highestFreq = cardFreq[card]

    if highestFreqCard != "":
        cardFreq[highestFreqCard] += cardFreq["J"]
        del cardFreq["J"]

def analyseHands(hands):
    handsAnalysed = []

    for handBetPair in hands:
        hand = handBetPair[0]
        cardFreq = baseMethods.getCardFreq(hand)
        if "J" in cardFreq:
            handleJokers(cardFreq)

        handType = baseMethods.getHandType(cardFreq)
        values = baseMethods.handCardValues(hand, cardValues)
        bet = handBetPair[1]

        handsAnalysed.append([hand, (handType, values), bet])

    handsAnalysed.sort(key=lambda x: x[1])
    return handsAnalysed

if(__name__ == "__main__"):
    hands = baseMethods.readFromFile(file)

    handsAnalysed = analyseHands(hands)

    sum = 0

    for i in range(len(handsAnalysed)):
        sum += (i+1) * handsAnalysed[i][2]

    print(sum)
