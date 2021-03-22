'''
Contains the whole game session, where multiple single games
are recorded.
'''

from modules.player import Player
from time import sleep

class Session():
    '''
    Session to record played games.

    Give a Player class as an argument to properly setup the session.
    '''

    def __init__(self, player, deck):
        '''
        Session to record played games.

        Give a Player class and a Deck class as an argument
        to properly setup the session.
        '''
        self._num_of_games = 0
        self._player_wins = 0
        self._dealer_wins = 0
        self.player = player
        self.ai = Player('Dealer')
        self.deck = deck

    def game_winner(self, winner):
        '''
        Declare the game winner.

        1 = Human
        2 = Dealer
        '''

        if winner == 1:
            self._player_wins += 1
        elif winner == 2:
            self._dealer_wins += 1

    def start_next_game(self):
        '''
        Starts the next blackjack game.

        Return a tuple of cards
        '''
        self._num_of_games += 1
        for _ in range(2):
            self.player.add_card(self.deck.deal_card())
        self.ai.add_card(self.deck.deal_card())
