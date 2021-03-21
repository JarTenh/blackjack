'''
This module defines a single card from standard 52 card deck.

Card class contains following attributes:
- Suite
- Value_str
- Value_int (to do some calculations)
'''

class Card():
    '''
    Class card containing card suite, value_str and value_int.

    Takes following parameters:
    - suite -> string as title-characters
    - value_str -> string, for example 'Two' or 'Ace'
    - index -> a dictionary, from which the card values are taken
      for example: {'Jack': 10} in a game of blackjack

    Value_int attribute is determined based on value_str value.
    '''

    def __init__(self, suite, value_str, index) -> None:
        try:
            # print('Creating card...')
            if suite in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
                self.suite = suite
            if value_str in index:
                self.value_str = value_str
            self.value_int = index[value_str]
        except:
            print('Please provide a valid input!')

    def __repr__(self) -> str:
        return f'{self.value_str} of {self.suite}'

    def __str__(self) -> str:
        return f'{self.value_str} of {self.suite}'

    def __eq__(self, other) -> bool:
        if isinstance(other, self.__class__):
            return self.value_int == other.value_int
        else:
            return False
    
    def __ne__(self, other) -> bool:
        return not self.__eq__(other)

    def __lt__(self, other) -> bool:
        if isinstance(other, self.__class__):
            return self.value_int < other.value_int
        else:
            return False
    
    def __gt__(self, other) -> bool:
        if isinstance(other, self.__class__):
            return self.value_int > other.value_int
        else:
            return False