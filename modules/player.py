'''
This module contains the Player class.

Player attributes:
- Credits ($)
- Hand, as what cards does the player have
'''

from modules.card import Card
import re

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
            hand_sum = sum(self.hand.values())
            if hand_sum > 21:
                # Check for aces in hand
                aces_list = [i for i in self.hand.keys() if 'Ace' in i]
                if len(aces_list) > 0:
                    for x in aces_list:
                        if self.hand[x] == 11:
                            self.hand[x] = 1
                            break
                    hand_sum = sum(self.hand.values())
            return hand_sum
        return 0

    def print_cards(self):
        for card in self.hand:
            print('\t' + card)

    def clear_hand(self):
        self.hand.clear()
