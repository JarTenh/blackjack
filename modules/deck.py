'''
This module defines a standard 52-card deck as default.

You should use Card-class along with this class.
'''

from random import shuffle, randint
from modules.card import Card

class Deck():

    def __init__(self, index, suites):
        '''
        Create a new deck with (len(index) * len(suites)) number of cards. Method shuffles
        the deck after creation.

        You can specify what index should be used in creation of cards. For example,
        in the game of blackjack the 'Jack', 'Queen' and 'King' cards are valued to
        10. So give 'blackjack' as an argument to create a blackjack deck, and 'default'
        to create a stardard valued deck.

        Suites-parameter accepts a list as an argument, that contains the suites to be used.
        '''
        self.deck = []
        self.original_deck = []
        try:
            # print('Creating new deck...')
            index_list = list(index.keys())
            # print(index_list[0])
            for i in range(len(suites)):
                for j in range(len(index_list)):
                    # print('Put card...')
                    self.deck.append(Card(suites[i], index_list[j], index))
                    self.original_deck.append(Card(suites[i], index_list[j], index))
            shuffle(self.deck)
        except:
            print('The creation of the deck failed!')
            print('Please check your input.\n')

    def list_deck(self):
        for card in self.deck:
            print(card)

    def deal_card(self):
        '''
        Picks a random card from deck and returns it. If the deck is empty,
        -1 is returned instead.
        '''
        if len(self.deck) > 0:
            random_card = self.deck.pop(randint(0, len(self.deck) - 1))
            return random_card
        else:
            return -1

    def reset_deck(self):
        self.deck = [x for x in self.original_deck]
