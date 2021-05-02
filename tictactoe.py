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
    """A class to manage a game a tic tac toe."""

    def __init__(self):
        pass

    @classmethod
    def _get_next_player(cls):
        pass

    def next_turn(self):
        pass

    def end_game(self):
        pass


class Board:
    """A class to handle the game logic of Tic Tac Toe"""

    NULL_CHAR = "-"
    PLAYERS = "XO"
    _GAME_SIZE = 9

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
        pass

    def evaluate_board(self) -> str:
        """
        Checks the current board state for end-of-game conditions, and returns a string describing the condition.
        Return Values:
          "": no end game condition
          "draw": the game has concluded in a draw
          "win": the game has concluded in a win
        """
        pass

    @staticmethod
    def _mutate_game_state(game_state: str, index: int, player: str) -> str:
        state_list = list(game_state)
        state_list[index] = player
        return "".join(state_list)

    @staticmethod
    def _extract_line(game_state: str, line_indecies: list) -> str:
        """Returns the contents of a specified line from a supplied game state."""
        line_state = ""
        for i in line_indecies:
            line_state += game_state[i]
        return line_state

    @classmethod
    def _strip_line(cls, line_state: str) -> str:
        """Removes the null character from a supplied line state string."""
        return line_state.replace(cls._NULL_CHAR, "")

    @classmethod
    def _evaluate_line(cls, line_state: str) -> str:

        filled_spots = len(line_state)
        players_present = len(set(line_state))
        if filled_spots >= 2 and players_present >= 2:
            return "D"
        if filled_spots == 3 and players_present == 1:
            return "W"

    @classmethod
    def _win_found(cls, full_line: str) -> bool:
        if len(set(full_line)) == 1:
            return True

    @classmethod
    def _draw_found(cls, full_line: str) -> bool:
        if len(set(full_line)) > 1:
            return True


class TicTacToeInterface:
    """
    A class to handle tictactoe's I/O logic.
    """

    def get_valid_turn(self):
        # prompt
        # get input
        # if the input is invalid, notify the player and repeat the prompt
        pass

    @classmethod
    def _input_is_valid(cls, user_input: str) -> bool:
        pass

    @classmethod
    def _generate_board_string_small(game_state: str) -> str:
        """Returns a string representing the current game state using the small format."""
        pass

    @classmethod
    def _generate_boad_string_large(game_state: str) -> str:
        """Returns a string representing the current game state using the large format."""
        pass

    @staticmethod
    def generate_win_message(win: tuple) -> str:
        player, line, turns = win
        return f"Player {player} wins on line {line} in {turns} turns!"

    @staticmethod
    def generate_draw_message() -> str:
        return f"The game ends in a draw."


class ConsoleInputManager:
    """
    A small class to separate the actual I/O handling from the interface logic
    """

    def __init__(self) -> None:
        pass

    def get_input(self):
        # get raw input

        pass


class ConsoleOutputManager:
    """
    A small class to separate the actual I/O handling from the interface logic
    """

    def __init__(self) -> None:
        pass

    @staticmethod
    def display(message) -> None:
        print(message)


class TicTacToePlayer:
    """
    An AI player
    """

    pass