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


class TicTacToeBoard:
    """A class to handle the game logic of Tic Tac Toe"""

    _NULL_CHAR = "-"
    _GAME_SIZE = 9
    _PLAYERS = "XO"
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
        self.game_state = self._NULL_CHAR * self._GAME_SIZE
        self.lines = self._INITIAL_LINES
        self.turns = 0

    def process_turn(self, turn: tuple) -> None:
        """Advances the game to the next turn"""

        self._update_game_state(turn)
        # advance turn count
        self.turns += 1
        # check for wins


    def _update_game_state(self, turn: tuple) -> None:
        index, player = turn
        current_state = self.game_state
        next_state = self._mutate_game_state(current_state, index, player)
        self.game_state = next_state

    @staticmethod
    def _mutate_game_state(game_state: str, index: int, player: str) -> str:
        state_list = list(game_state)
        state_list[index] = player
        return "".join(state_list)

    @staticmethod
    def _extract_line(cls, game_state: str, line_indecies: list) -> str:
        line_state = ""
        for i in line_indecies:
            line_state += game_state[i]
        return line_state

    @classmethod
    def _evaluate_line(cls, line_state: str) -> str:
        line_state = line_state.replace(cls._NULL_CHAR, "")
        filled_spots = len(line_state)
        players_present = len(set(line_state))
        if filled_spots >= 2 and players_present >= 2:
            return "D"
        if filled_spots == 3 and players_present == 1:
            return "W"


        
        


class TicTacToeInterface:
    """
    A class to handle tictactoe's I/O.
    """

    @staticmethod
    def _coord_to_index(coord: str) -> int:
        pass

    @classmethod
    def _input_is_valid(user_input: str)

class TicTacToePlayer:
    """
    An AI player
    """

    pass