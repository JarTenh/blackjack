'''
This module contains the Player class.

Player attributes:
- Credits ($)
- Hand, as what cards does the player have
'''

from modules.card import Card

class Player():
    '''
    Player class. Has an attribute credits, default value 100 $.
    '''

    def __init__(self, name, credits = 100) -> None:
        try:
            if type(name) == str:
                self.name = name
            if type(credits) == int:
                self.credits = credits
            self.hand = {}
        except:
            print('Please provide a valid input!\n')

    def bet(self, amount):
        '''
        Place bet to the deal. Balance going under zero is not allowed.

        Returns 0 if bet is accepted, else returns -1
        '''
        if self.credits - amount >= 0:
            self.credits -= amount
            return 0
        else:
            return -1

    def add_card(self, card):
        '''
        Add a card to player's hand.
        Use Card class!
        '''

        if type(card) == Card:
            self.hand[card.value_str + ' of ' + card.suite] = card.value_int

    def get_hand_value(self):
        '''
        Returns the total value of player's card.
        '''
        if len(self.hand) > 0:
            return sum(self.hand.values)
        return 0

    def print_cards(self):
        for card in self.hand:
            print(card)
