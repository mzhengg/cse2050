import random
random.seed(658) # Change the seed to generate a new order of cards

def CardGenerator():
    cards = []
    suits = ['hearts', 'diamonds', 'clubs', 'spades']
    values = ['two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
    'jack', 'queen', 'king', 'ace']
    for suit in suits:
        for value in values:
            cards.append(value + ' of ' + suit)
    random.shuffle(cards)
    return cards