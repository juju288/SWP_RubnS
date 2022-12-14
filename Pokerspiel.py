import numpy
import numpy as np
import random

runden = 100000


def drawHand():
    start = 1
    end = 52
    ziehung = 5

    a = np.arange(start, end + 1)
    mk = []

    for i in range(0, ziehung):
        r = int(random.random() * end)
        a1 = a[r]
        a[r] = a[(end - 1) - i]
        a[(end - 1) - i] = a1

    for i in range(end - ziehung, end):
        mk.append(a[i])

    return mk


def cardColor(arr):
    if (arr // 13 == 0):
        return "Herz";
    elif (arr // 13 == 1):
        return "Karo";
    elif (arr // 13 == 2):
        return "Pik";
    elif (arr // 13 == 3):
        return "Kreuz";


def cardColors(arr):
    out = []
    for c in arr:
        out.append(cardColor(c))
    return out


def cardNumbers(arr):
    out = []
    for c in arr:
        out.append(cardNumber(c))
    return out


def cardNumber(arr):
    if ((arr % 13) == 0):
        return 2;
    elif ((arr % 13) == 1):
        return 3;
    elif ((arr % 13) == 2):
        return 4;
    elif ((arr % 13) == 3):
        return 5;
    elif ((arr % 13) == 4):
        return 6;
    elif ((arr % 13) == 5):
        return 7;
    elif ((arr % 13) == 6):
        return 8;
    elif ((arr % 13) == 7):
        return 9;
    elif ((arr % 13) == 8):
        return 10;
    elif ((arr % 13) == 9):
        return 11;  # J
    elif ((arr % 13) == 10):
        return 12;  # Q
    elif ((arr % 13) == 11):
        return 13;  # K
    elif ((arr % 13) == 12):
        return 14;  # A


def highCard(hand):
    return numpy.sort(cardNumbers(hand)).max()


'''
def nOfAKind2(hand):
    ranks = numpy.zeros(14)
    for card in hand:
        ranks[cardNumber(card)-1] += 1
    return ranks.max()
'''


def nOfAKind(hand):
    n = 1
    rank = None
    for i in range(0, len(hand)):
        if cardNumber(hand[i]) in cardNumbers(hand[i + 1:]):
            if rank is None:
                rank = cardNumber(hand[i])
            if rank is cardNumber(hand[i]):
                n += 1
    return n


def twoPair(hand):
    rankFirstPair = None
    for i in range(0, len(hand)):
        if cardNumber(hand[i]) in cardNumbers(hand[i + 1:]):
            if rankFirstPair is not None and cardNumber(hand[i]) != rankFirstPair:
                return True
            rankFirstPair = cardNumber(hand[i])
    return False


def fullHouse(hand):
    if (nOfAKind(numpy.sort(hand)) == 2 and nOfAKind(numpy.sort(hand)[::-1]) == 3) \
            or (nOfAKind(numpy.sort(hand)) == 3 and nOfAKind(numpy.sort(hand)[::-1]) == 2):
        return True
    return False


def straight(hand):
    cards = numpy.sort(hand)
    rank = 1
    for i in range(0, len(hand) - 1):
        if cardNumber(cards[i]) == (cardNumber(cards[i + 1]) - 1):
            rank += 1
        if rank == 5:
            return True
    return False


def flush(hand):
    sameColor = 1
    for i in range(0, len(hand)):
        if cardColor(hand[i]) in cardColors(hand[i + 1:]):
            sameColor += 1
        if sameColor == 5:
            return True
    return False


def straightFlush(hand):
    if straight(hand) and flush(hand):
        return True
    return False


def royalFlush(hand):
    if straight(hand) and flush(hand) and (highCard(hand) == 14):
        return True
    return False


dic = {"Royal Flush": 0,
       "Straight Flush": 0,
       "Quads": 0,
       "Full House": 0,
       "Flush": 0,
       "Straight": 0,
       "Three of Kind": 0,
       "Two Pair": 0,
       "One Pair": 0,
       "High Card": 0
       }


def getHand(hand):
    if royalFlush(hand):
        dic["Royal Flush"] = dic["Royal Flush"] + 1
        return "Royal Flush"
    elif straightFlush(hand):
        dic["Straight Flush"] = dic["Straight Flush"] + 1
        return "Straight Flush"
    elif nOfAKind(hand) == 4:
        dic["Quads"] = dic["Quads"] + 1
        return "Quads"
    elif fullHouse(hand):
        dic["Full House"] = dic["Full House"] + 1
        return "Full House"
    elif flush(hand):
        dic["Flush"] = dic["Flush"] + 1
        return "Flush"
    elif straight(hand):
        dic["Straight"] = dic["Straight"] + 1
        return "Straight"
    elif nOfAKind(hand) == 3:
        dic["Three of Kind"] = dic["Three of Kind"] + 1
        return "Three of Kind"
    elif twoPair(hand):
        dic["Two Pair"] = dic["Two Pair"] + 1
        return "Two Pair"
    elif nOfAKind(hand) == 2:
        dic["One Pair"] = dic["One Pair"] + 1
        return "One Pair"
    else:
        '''
        if highCard(hand) == 11:
            print('J')
        elif highCard(hand) == 12:
            print('Q')
        elif highCard(hand) == 13:
            print('K')
        elif highCard(hand) == 14:
            print('A')
        else: print(highCard(hand))'''
        dic["High Card"] = dic["High Card"] + 1
        return "High Card"



def main():
    for i in range(0, runden):
        hand = drawHand()
        getHand(hand)

    for i in dic:
        dic[i] = round(dic[i] / runden * 100, 2)
    print(dic)


if __name__ == "__main__":
    main()

