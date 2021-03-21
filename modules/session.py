'''
Contains the whole game session, where multiple single games
are recorded.
'''

class Session():
    '''
    Session to record played games.

    Give a Player class as an argument to properly setup the session.
    '''

    def __init__(self, player):
        self._num_of_games = 0
        self._player_wins = 0
        self._computer_wins = 0
        self.player = player
        return

    def play_game(self):
        '''
        Increase the _num_of_games variable by one.
        '''

        self._num_of_games += 1
        return

    def game_winner(self, winner):
        '''
        Declare the game winner.

        1 = Human
        2 = Computer
        '''

        if winner == 1:
            self._player_wins += 1
        elif winner == 2:
            self._computer_wins += 1
        return
