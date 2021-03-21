'''
This module defines a standard 52-card deck as default.

You should use Card-class along with this class.
'''

from random import shuffle, randint
from modules.card import Card

class Deck():
    '''
    Defines a default size of 52 Card-class objects, like a standard card deck.

    You can specify the number of cards optionally with create_new_deck method.
    '''

    def __init__(self) -> None:
        print('Initialized deck!')
        self.deck = []

    def create_new_deck(self, index, suites):
        '''
        Create a new deck with (len(index) * len(suites)) number of cards. Method shuffles
        the deck after creation.

        You can specify what index should be used in creation of cards. For example,
        in the game of blackjack the 'Jack', 'Queen' and 'King' cards are valued to
        10. So give 'blackjack' as an argument to create a blackjack deck, and 'default'
        to create a stardard valued deck.

        Suites-parameter accepts a list as an argument, that contains the suites to be used.
        '''

        try:
            # print('Creating new deck...')
            index_list = list(index.keys())
            # print(index_list[0])
            for i in range(len(suites)):
                for j in range(len(index_list)):
                    # print('Put card...')
                    self.deck.append(Card(suites[i], index_list[j], index))
            shuffle(self.deck)
        except:
            print('The creation of the deck failed!')
            print('Please check your input.\n')

    def list_deck(self):
        for card in self.deck:
            print(card)
