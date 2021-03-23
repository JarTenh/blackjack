'''
Contains the whole game session, where multiple single games
are recorded.
'''

from modules.player import Player

class Session():
    '''
    Session to record played games.

    Give a Player class as an argument to properly setup the session.
    '''

    def __init__(self, player_name, deck):
        '''
        Session to record played games.

        Give a Player class and a Deck class as an argument
        to properly setup the session.
        '''
        self._num_of_games = 0
        self._player_wins = 0
        self._dealer_wins = 0
        self.player = Player(player_name)
        self.dealer = Player('Dealer')
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

        Increases the games played by one, and 
        adds cards to the player's and the dealer's hand.
        '''
        self.player.clear_hand()
        self.dealer.clear_hand()
        self.deck.reset_deck()
        self._num_of_games += 1
        for _ in range(2):
            self.player.add_card(self.deck.deal_card())
            self.dealer.add_card(self.deck.deal_card())

    def player_busted(self):
        '''
        Checks if the human player busted, that is 
        his/her hand value is over 21.
        '''

        if self.player.get_hand_value() > 21:
            return True
        return False

    def dealer_busted(self):
        '''
        Checks if the human player busted, that is 
        his/her hand value is over 21.
        '''

        if self.dealer.get_hand_value() > 21:
            return True
        return False
