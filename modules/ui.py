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
        self.session = None

    def intro(self):
        '''
        Print the welcome message to the user.
        '''

        clear()
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
        '''
        Simple function to ask a player's name.
        '''

        name = ''

        try:
            name = input('Please enter your name: ')
            print()
            print(f'Good luck with the game, {name}!')
            sleep(1)
        except KeyboardInterrupt:
            sys.exit(0)
        return name

    def print_header(self):
        '''
        Prints the window header on the screen, containing:
        - Playing blackjack!
        - Num of player and dealer wins

        Takes a Session object as a parameter.
        '''

        print(f'**********************' \
            f'\t\t\t\t\tPlayer wins: {self.session._player_wins}')
        print('Playing blackjack!' \
            f'\t\t\t\t\tDealer wins: {self.session._dealer_wins}')
        print('**********************')
        print()
        print(f'Player: {self.session.player.name}')
        print(f'Credits: $ {self.session.player.credits}')

    def print_hands(self, player):
        '''
        Prints the cards in player's or dealers hand.
        Accepts a Player class as a parameter.
        '''

        if type(player) == Player:
            print(f'\t\t{player.name}\'s hand:'.upper())
            print()
            player.print_cards()
        print()
        print(f'Total value of cards: {player.get_hand_value()}')

    def start_session(self, player_name):
        '''
        This function starts a game Session. A session can contain
        multiple games, started with play_single_game method.
        '''

        self.session = Session(player_name, Deck(index, suites))

        while True:
            clear()
            self.print_header()
            print()
            try:
                command = input('What do you want to do: (D)eal cards, (B)et or (Q)uit? ')
                if command == 'Q' or command == 'q':
                    clear()
                    break
                if command == 'D' or command == 'd':
                    self.play_single_game()
            except KeyboardInterrupt:
                sys.exit()
            except:
                print('Something went wrong.')

    def play_single_game(self):
        '''
        Play a single game of blackjack. This function should be run
        only after a Session has been already created.
        '''
        self.session.start_next_game()

        while True:
            clear()
            self.print_header()
            print()
            self.print_hands(self.session.player)
            print('\n')
            self.print_hands(self.session.dealer)
            print()
            if self.session.player_busted():
                self.session.game_winner(2)
                print('YOU\'RE BUSTED! DEALER WINS!')
                print()
                sleep(2)
                while True:
                    play_again = input('Play again (y/n)? ')
                    if play_again == 'Y' or play_again == 'y':
                        break
                    elif play_again == 'N' or play_again == 'n':
                        clear()
                        raise KeyboardInterrupt
                break
            print('What do you want to do? ')
            command = input('(H)it, (S)tay? or (Q)uit game? ')
            if command == 'H' or command == 'h':
                self.session.player.add_card(self.session.deck.deal_card())
            elif command == 'S' or command == 's':
                if self.session.player.get_hand_value() <= self.session.dealer.get_hand_value():
                    print()
                    print('\tDEALER WINS!')
                    print()
                    sleep(2)
                    break
                else:
                    while True:
                        clear()
                        self.print_header()
                        print()
                        self.print_hands(self.session.player)
                        print('\n')
                        self.print_hands(self.session.dealer)
                        print()

                        if self.session.dealer.get_hand_value() >= self.session.player.get_hand_value():
                            if self.session.dealer_busted():
                                self.session.game_winner(1)
                                print()
                                print(f'DEALER BUSTED! {self.session.player.name} WINS!')
                                print()
                                sleep(2)
                                break
                            else:
                                self.session.game_winner(2)
                                print()
                                print('DEALER WINS!')
                                print()
                                sleep(2)
                                break
                        
                        print('Dealer picking card...')
                        self.session.dealer.add_card(self.session.deck.deal_card())
                        sleep(2)
                        print()
                    while True:
                        play_again = input('Play again (y/n)? ')
                        if play_again == 'Y' or play_again == 'y':
                            break
                        elif play_again == 'N' or play_again == 'n':
                            clear()
                            raise KeyboardInterrupt
                        break    
                    break
            elif command == 'Q' or command == 'q':
                clear()
                raise KeyboardInterrupt
            else:
                clear()
