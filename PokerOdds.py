import random
from collections import Counter

suits = ["1", "2", "3", "4"]
ranks = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]

def CreateIndex(i):
    suit = suits[i // 13]
    rank = ranks[i % 13]
    return rank, suit

def CreateHand():
    deck = list(range(52))
    random.shuffle(deck)
    hand = deck[:5]
    return [CreateIndex(i) for i in hand]

def CheckIfRoyal(hand):
    suits_in_hand = [s for r, s in hand]
    ranks_in_hand = [r for r, s in hand]

    if len(set(suits_in_hand)) != 1:
        return False 
    
    royal_ranks = {"1", "10", "11", "12", "13"}
    if set(ranks_in_hand) == royal_ranks:
        return True
    return False 

def CheckIfStraightFlush(hand):
    suits_in_hand = [s for r, s in hand]
    ranks_in_hand = [int(r) for r, s in hand]

    if len(set(suits_in_hand)) != 1:
        return False
    
    ranks_sorted = sorted(set(ranks_in_hand))

    if len(ranks_sorted) != 5:
        return False
    if ranks_sorted[-1] - ranks_sorted[0] == 4:
        return True
    if set(ranks_sorted) == {1,2,3,4,5}:
        return True
    if set(ranks_sorted) == {1,10,11,12,13}:
        return True

    return False


def CheckIfKind(hand):
    ranks_in_hand = [r for r, s in hand]
    ranks_count = Counter(ranks_in_hand)
    counts = sorted(ranks_count.values(), reverse=True)

    if counts == [4,1]:
        return "Four of a kind"
    elif counts == [3,2]:
        return "Full House"
    elif counts == [3,1,1]:
        return "Three of a kind"
    elif counts == [2,2,1]:
        return "Two pair"
    elif counts == [2,1,1,1]:
        return "One pair"
    else:
        return "High Card"
    
def CheckIfFlush(hand):
    suits_in_hand = [s for r, s in hand]
    ranks_in_hand = [int(r) for r, s in hand]
    ranks_sorted = sorted(set(ranks_in_hand))
    suits_count = Counter(suits_in_hand)
    counts = sorted(suits_count.values(), reverse=True)

    if counts[0] != 5:
        return False
    if set(ranks_sorted) == {1,2,3,4,5}:
        return False
    if set(ranks_sorted) == {1,10,11,12,13}:
        return False
    if ranks_sorted[-1] - ranks_sorted[0] == 4 and len(set(ranks_sorted)) == 5:
        return False
    return True


def CheckIfStraight(hand):
    ranks = sorted(set(int(r) for r, s in hand))
    suits = [s for r, s in hand]

    if len(ranks) != 5:
        return False
    if len(set(suits)) == 1:
        return False
    if ranks[-1] - ranks[0] == 4:
        return True
    if ranks == [1,2,3,4,5]:
        return True
    if ranks == [1,10,11,12,13]:
        return True
    else:
        return False
    
def CheckIfNothing(hand):
    if (not CheckIfRoyal(hand) and
        not CheckIfStraightFlush(hand) and
        not CheckIfFlush(hand) and 
        not CheckIfStraight(hand) and
        CheckIfKind(hand) == "High Card"):
        return True
    else:
        return False 


def main():
    total = 0
    sfc = 0
    rc = 0
    four_pair = 0
    full_house = 0
    three_pair = 0
    two_pair = 0
    one_pair = 0
    fc = 0
    sc = 0
    nc = 0

    for i in range(1000000):
        hand = CreateHand()
        kind = CheckIfKind(hand)
        if CheckIfRoyal(hand):
            rc += 1
        elif CheckIfStraightFlush(hand):
            sfc += 1
        elif kind == "Four of a kind":
            four_pair += 1
        elif kind == "Full House":
            full_house += 1
        elif kind == "Three of a kind":
            three_pair += 1
        elif kind == "Two pair":
            two_pair += 1
        elif kind == "One pair":
             one_pair += 1
        elif CheckIfFlush(hand):
            fc += 1
        elif CheckIfStraight(hand):
            sc += 1
        elif CheckIfNothing(hand):
            nc += 1

        total += 1

    royal_percent = (rc / total) * 100
    straightflush_percent = (sfc / total) * 100
    flush_percent = (fc / total) * 100
    straight_percent = (sc / total) * 100
    nothing_percent = (nc / total) * 100
    four_percent = (four_pair / total) * 100
    full_house_percent = (full_house / total) * 100
    three_percent = (three_pair / total) * 100
    two_percent = (two_pair / total) * 100
    one_percent = (one_pair / total) * 100 
    print("The odds of you drawing a royal flush are " + str(round(royal_percent, 5)) + " percent")
    print("The odds of you drawing a straight flush are " + str(round(straightflush_percent, 5)) + " percent")
    print("The odds of you drawing a flush are " + str(round(flush_percent, 5)) + " percent")
    print("The odds of you drawing a straight are " + str(round(straight_percent, 5)) + " percent")
    print("The odds of you drawing four of a kind are " + str(round(four_percent, 5)) + " percent")
    print("The odds of you drawing a full house are " + str(round(full_house_percent, 5)) + " percent")
    print("The odds of you drawing three of a kind are " + str(round(three_percent, 5)) + " percent")
    print("The odds of you drawing a two pair " + str(round(two_percent, 5)) + " percent")
    print("The odds of you drawing a pair are " + str(round(one_percent, 5)) + " percent")
    print("The odds of you drawing nothing are " + str(round(nothing_percent, 5)) + " percent")

main()
