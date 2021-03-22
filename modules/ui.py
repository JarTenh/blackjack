import sys
from time import sleep
from modules.clear_screen import clear
from modules.session import Session
from modules.player import Player
from modules.deck import Deck

index = {
    'Ace': 11,
    'Two': 2,
    'Three': 3,
    'Four': 4,
    'Five': 5,
    'Six': 6,
    'Seven': 7,
    'Eight': 8,
    'Nine': 9,
    'Ten': 10,
    'Jack': 10,
    'Queen': 10,
    'King': 10
}

suites = ['Hearts', 'Diamonds', 'Spades', 'Clubs']


class UI():
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

    def ask_player_name(self):
        name = input('Please enter your name: ')
        print()
        print(f'Good luck with the game, {name}!')
        sleep(1)
        return name

    def play_game(self, player_name):

        session = Session(Player(player_name), Deck(index, suites))

        while True:
            clear()
            print('**********************')
            print('Playing blackjack!')
            print('**********************')
            print()
            print(f'Player: {session.player.name} \
                \t\t\t\t\tPlayer wins: {session._player_wins}')
            print(f'Credits: $ {session.player.credits}\
                \t\t\t\t\tComputer wins: {session._dealer_wins}')
            print()
            print('\t\tPlayer\'s hand:')
            session.player.print_cards()
            print()
            try:
                command = input('What do you want to do: (D)eal cards, (B)et or (Q)uit? ')
                if command == 'Q' or command == 'q':
                    break
                if command == 'D' or command == 'd':
                    session.start_next_game()
            except KeyboardInterrupt:
                sys.exit()
            except:
                print('Something went wrong.')