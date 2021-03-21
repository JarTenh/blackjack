import sys
from modules.clear_screen import clear

class ui():
    '''
    Class for UI for the blackjack game.

    Contains some functions to communicate with the user.
    '''

    def __init__(self) -> None:
        return

    def intro(self):
        '''
        Print the welcome message to the user.
        '''

        print('######################')
        print('#                    #')
        print('#      BLACKJACK     #')
        print('#                    #')
        print('######################')

        return

    def show_instructions(self):
        print()
        print('------------------')
        print('Game Instructions')
        print('------------------')
        print()
        print('You play against a computer a simple blackjack-game.')
        print('First you get two cards, number cards being valued from 2 to 9,')
        print('Jack, Queen and King being valued as 10 and')
        print('Ace as either 1 or 11.')
        print()
        print('Your aim is get as close to (or equal to) value of 21 with your cards.')
        print('You\'ll have to get closer to 21 than the computer to win the game.')
        print()

        try:
            answer = input('Press "Enter" to continue...')
            return
        except KeyboardInterrupt:
            sys.exit()
