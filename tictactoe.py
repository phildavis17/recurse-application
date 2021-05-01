"""
Write a program that lets two humans play a game of Tic Tac Toe in a terminal.
The program should let the players take turns to input their moves.
The program should report the outcome of the game.
"""


"""
012
345
678
"""

"""
A1, B1, C1,
A2, B2, C2,
A3, B3, C3,
"""

"""
"""


class TicTacToeGame:
    """A class to handle the game logic of Tic Tac Toe"""

    _INITIAL_STATE = "---------"
    _INITIAL_LINES = {
        "Row 1": [0, 1, 2],
        "Row 2": [3, 4, 5],
        "Row 3": [6, 7, 8],
        "Column A": [0, 3, 6],
        "Column B": [1, 4, 7],
        "Column C": [2, 5, 8],
        "Diagonal 1": [0, 4, 8],
        "Diagonal 2": [2, 4, 6],
    }

    def __init__(self) -> None:
        self.game_state = self._INITIAL_STATE
        self.lines = self._INITIAL_LINES
        self.turns = 0

    def evaluate_board(self):
        pass

    @staticmethod
    def _coord_to_index(coord: str) -> int:
        pass

    @staticmethod
    def _update_game_state(game_state: str, index: int, player: str) -> str:
        state_list = list(game_state)
        state_list[index] = player
        return "".join(state_list)


class TicTacToeInterface:
    """
    A class to handle tictacto's I/O.
    """

    pass


class TicTacToePlayer:
    """
    An AI player
    """

    pass