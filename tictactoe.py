"""
Write a program that lets two humans play a game of Tic Tac Toe in a terminal.
The program should let the players take turns to input their moves.
The program should report the outcome of the game.
"""

from itertools import cycle
from typing import Optional


class TicTacToeGame:
    """A class to manage a game a tic tac toe."""

    _PLAYER_NAMES = "XO"

    def __init__(self):
        self.board = Board(self)
        self.interface = Interface(self)
        self.win = None
        self.turns = 0
        self._player_seuqence = (p for p in cycle(self._PLAYER_NAMES))
        self.game_state = self.board.generate_fresh_board()

    def play(self) -> None:
        self.interface.greet()
        while self.board.NULL_CHAR in self.game_state and self.win is None:
            self.next_turn()
        self.end_game()

    def get_next_player(self) -> str:
        """Returns a string representing the next player in the sequence."""
        return next(self._player_seuqence)

    def _get_turn(self, player: str) -> dict:
        """Collects a turn input and returns it as a properly formated turn dict."""
        turn_input = self.interface.get_valid_turn(player)
        turn_input = int(turn_input) - 1
        turn_dict = {"player": player, "index": turn_input}
        return turn_dict

    def next_turn(self) -> None:
        self.turns += 1
        self.interface.draw_game(self.game_state)
        player = self.get_next_player()
        index = int(self.interface.get_valid_turn(player)) - 1
        turn = {"player": player, "index": index}
        self.game_state = self.board.mutate_game_state(self.game_state, turn)
        self.win = self.board.evaluate_board(self.game_state)

    def end_game(self) -> None:
        if self.win is not None:
            self.win["turn"] = self.turns
        self.interface.report_outcome(self.game_state, self.win)

    def turn_is_playable(self, turn: str) -> bool:
        pass

    def validate_turn(self, turn: str):
        """Returns True if the turn input can be converted to an int representing an un-played position on the board."""
        try:
            index = int(turn) - 1
            current_char = self.game_state[index]
        except (ValueError, IndexError):
            return False
        if current_char == self.board.NULL_CHAR:
            return True
        return False


class Board:
    """A class to handle the game logic of Tic Tac Toe"""

    NULL_CHAR = "-"
    LINES = {
        (0, 1, 2): "Row 1",
        (3, 4, 5): "Row 2",
        (6, 7, 8): "Row 3",
        (0, 3, 6): "Column 1",
        (1, 4, 7): "Column 2",
        (2, 5, 8): "Column 3",
        (0, 4, 8): "Diagonal 1",
        (2, 4, 6): "Diagonal 2",
    }

    def __init__(self, game: "TicTacToeGame") -> None:
        self.game = game

    @classmethod
    def generate_fresh_board(cls) -> str:
        return cls.NULL_CHAR * 9

    @staticmethod
    def mutate_game_state(game_state: str, turn: dict) -> str:
        """Modifies a supplied game state according to a supplied turn, and returns the result."""
        state_list = list(game_state)
        state_list[turn["index"]] = turn["player"]
        return "".join(state_list)

    @staticmethod
    def _extract_line(game_state: str, line_indecies: tuple) -> str:
        """Returns the contents of a specified line from a supplied game state."""
        line_state = ""
        for i in line_indecies:
            line_state += game_state[i]
        return line_state

    def evaluate_board(self, game_state: str) -> Optional[dict]:
        """
        Evaluates the supplied board position for situations that require a response.
        """
        line_states = self._decompose_board(game_state)
        win_descriptor = self._check_lines(line_states)
        return win_descriptor

    @classmethod
    def _decompose_board(cls, game_state: str) -> dict:
        """Converts a supplied game state string to a dict of linestates and their matching names."""
        line_states = {}
        for indecies, name in cls.LINES.items():
            line_state = cls._extract_line(game_state, indecies)
            line_states[line_state] = name
        return line_states

    @classmethod
    def _check_lines(cls, line_states: dict) -> Optional[dict]:
        """
        Checks all of the supplied lines, and returns a dict describing the win state if a win is found. Returns None otherwise.
        The win description is a dict, with keys "player" which is X or O, and "line" which is the name of the line where the win occurred.
        """
        for line, name in line_states.items():
            if cls.NULL_CHAR not in line and cls._win_found(line):
                win_descriptor = {}
                win_descriptor["player"] = line[0]
                win_descriptor["line"] = name
                return win_descriptor
        return None

    @classmethod
    def _win_found(cls, full_line: str) -> bool:
        """Returns True if the supplied full line state is a win."""
        if len(set(full_line)) == 1:
            return True
        return False


class Interface:
    """
    A class to handle tictactoe's I/O logic.
    """

    STANDARD_MESSAGES = {
        "greeting": "\nTic! Tac! Toe!!",
        "bad turn": "Please enter a valid turn:",
        "draw": "The game ends in a draw.",
        "play again": "Would you like to play again? (Y/N): ",
    }

    def __init__(self, game: "TicTacToeGame") -> None:
        self.game = game
        self.style = SmallBoardStyle
        self.input = ConsoleInput()
        self.output = ConsoleOutput()

    def greet(self) -> None:
        """Displays a standard greeting message."""
        self.output.display(self.STANDARD_MESSAGES["greeting"])

    def get_valid_turn(self, player: str) -> str:
        """Prompts for a turn. If the input is invalid, prompts until a valid turn is entered."""
        turn_prompt = f"Player {player}, where would you like to play?: "
        turn = self.get_input(turn_prompt)
        if self.game.validate_turn(turn):
            return turn
        while not self.game.validate_turn(turn):
            turn = self.get_input(self.STANDARD_MESSAGES["bad turn"])
        return turn

    def show(self, message: str) -> None:
        """Displays the supplied message using the assigned output method."""
        self.output.display(message)

    def draw_game(self, game_state: str) -> None:
        """Displays a representation of the supplied game state using the assigned Style."""
        board_string = self.style.build_board_string(game_state)
        self.show(board_string)

    def get_input(self, prompt: str = None) -> str:
        """Uses the assigned Input to retrieve user input. Displays a prompt, if provided."""
        if prompt is None:
            prompt = ""
        return self.input.get_input(prompt)

    def report_outcome(self, game_state: str, outcome: Optional[dict]) -> None:
        """Uses the assigned Output to display a message describing the end result of the game."""
        message = self._compose_outcome_message(outcome)
        if outcome is not None:
            self.draw_win(game_state, outcome)
        else:
            self.draw_game(game_state)
        self.output.display(message)

    @classmethod
    def _compose_outcome_message(cls, outcome: Optional[dict]) -> str:
        if outcome is not None:
            message = "Player {player} wins along {line} on turn {turn}!".format(
                **outcome
            )
        else:
            message = cls.STANDARD_MESSAGES["draw"]
        return message

    def draw_win(self, game_state: str, win_descriptor: dict) -> None:
        """Uses the assigned Output to display a board with certain characters substituted to indicate a win."""
        win_string = self.style.build_win_string(game_state, win_descriptor)
        self.show(win_string)


class SmallBoardStyle:

    _EMPTY_BORD = "123456789"

    _WIN_CHARACTERS = {
        "Row": "-",
        "Column": "|",
        "Diagonal 1": "\\",
        "Diagonal 2": "/",
    }

    def __init__(self) -> None:
        pass

    @classmethod
    def _populate_board_string(cls, board_state: str) -> str:
        out_string = ""
        for i, c in enumerate(board_state):
            if c == Board.NULL_CHAR:
                next_char = cls._EMPTY_BORD[i]
            else:
                next_char = c
            out_string += next_char
        return out_string

    @classmethod
    def _format_board_string(cls, board_string: str) -> str:
        out_string = "\n"
        for i, c in enumerate(board_string):
            out_string += c
            if (i + 1) % 3 == 0:
                out_string += "\n"
        return out_string

    @classmethod
    def build_board_string(cls, board_state: str) -> str:
        populated_string = cls._populate_board_string(board_state)
        return cls._format_board_string(populated_string)

    @classmethod
    def _get_win_character(cls, line: str) -> str:
        for line_type, char in cls._WIN_CHARACTERS.items():
            if line_type in line.casefold():
                return char
        raise ValueError(f"Unhandled line descriptor: {line}")

    @classmethod
    def build_win_string(cls, board_state: str, win_descriptor: dict) -> str:
        populated_string = cls._populate_board_string(board_state)
        win_string = cls._populate_win_string(populated_string, win_descriptor)
        return cls._format_board_string(win_string)

    @classmethod
    def _populate_win_string(cls, board_string: str, win_descriptor: dict) -> str:
        win_lines = {title: indecies for indecies, title in Board.LINES.items()}
        win_line = win_descriptor["line"]
        win_indecies = win_lines[win_line]
        win_character = cls._get_win_character(win_line)
        board_list = list(board_string)
        for i in win_indecies:
            board_list[i] = win_character
        return "".join(board_list)


class LargeBoardStyle:

    CELL_INDEX_MAP = (
        "\n"
        "111┃222┃333\n"
        "111┃222┃333\n"
        "111┃222┃333\n"
        "━━━╋━━━╋━━━\n"
        "444┃555┃666\n"
        "444┃555┃666\n"
        "444┃555┃666\n"
        "━━━╋━━━╋━━━\n"
        "777┃888┃999\n"
        "777┃888┃999\n"
        "777┃888┃999\n"
        "\n"
    )

    CELL_INDICIES = "123456789"

    EMPTY_BOARD = (
        "\n"
        "   ┃   ┃   \n"
        " 1 ┃ 2 ┃ 3 \n"
        "   ┃   ┃   \n"
        "━━━╋━━━╋━━━\n"
        "   ┃   ┃   \n"
        " 4 ┃ 5 ┃ 6 \n"
        "   ┃   ┃   \n"
        "━━━╋━━━╋━━━\n"
        "   ┃   ┃   \n"
        " 7 ┃ 8 ┃ 9 \n"
        "   ┃   ┃   \n"
        "\n"
    )

    BIG_CHARS = {
        "X": ("╲ ╱ ╳ ╱ ╲"),
        "O": ("╭─╮│ │╰─╯"),
    }

    INDEX_MAP: dict = {x: [] for x in CELL_INDICIES}
    for i, c in enumerate(CELL_INDEX_MAP):
        if c in CELL_INDICIES:
            INDEX_MAP[c].append(i)

    def __init__(self) -> None:
        pass

    @staticmethod
    def _substitute_chars(base_string: str, indicies: list, new_chars: str) -> str:
        """Returns the supplied string with characters at supplied indecies replaced with supplied new characters."""
        str_list = list(base_string)
        for i, c in zip(indicies, new_chars):
            str_list[i] = c
        return "".join(str_list)

    @classmethod
    def build_board_string(cls, board_state: str) -> str:
        board_string = cls.EMPTY_BOARD
        for i, c in enumerate(board_state):
            if c is not Board.NULL_CHAR:
                board_string = cls._substitute_chars(
                    board_string, cls.INDEX_MAP[str(i + 1)], cls.BIG_CHARS[c]
                )
        return board_string

    @classmethod
    def build_win_string(cls, board_state: str, win_descriptor: dict) -> str:
        pass


class ConsoleInput:
    """
    A small class to separate the actual I/O handling from the interface logic
    """

    def __init__(self) -> None:
        pass

    @staticmethod
    def get_input(message: str = None) -> str:
        if message is None:
            message = ""
        in_str = input(message)
        return in_str


class ConsoleOutput:
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


if __name__ == "__main__":
    the_game = TicTacToeGame()
    the_game.play()