import random
import art

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculater_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

