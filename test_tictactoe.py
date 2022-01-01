import pytest
import random

from tictactoe import Board, SmallBoardStyle, TicTacToeGame


class TestGame:
    pass


class TestTicTacToeGame:
    def test_validate_turn(self):
        game = TicTacToeGame()
        assert game.validate_turn("1")
        assert not game.validate_turn("M")


class TestBoard:
    def test_mutate_game_state(self):
        start = "---------"
        new = Board._mutate_game_state(start, 0, "X")
        assert new == "X--------"

    def test_extract_line(self):
        for _ in range(100):
            board_state = "012345678"
            target_chars = "".join(random.sample(board_state, 3))
            indecies = tuple([int(c) for c in target_chars])
            assert Board._extract_line(board_state, indecies) == target_chars

    def test_win_found(self):
        win = "XXX"
        no_win = "XXO"
        assert Board._win_found(win)
        assert not Board._win_found(no_win)

    def test_generate_new_board(self):
        new_state = Board.generate_fresh_board()
        assert len(new_state) == 9
        for c in new_state:
            assert c == Board.NULL_CHAR

    def test_check_lines(self):
        win_state = "XXX------"
        win_dict = Board._decompose_board(win_state)
        no_win_state = "XOX------"
        no_win_dict = Board._decompose_board(no_win_state)
        assert Board._check_lines(win_dict) is not None
        assert Board._check_lines(no_win_dict) is None


class TestInterface:
    pass


class TestInput:
    pass


class TestSmallBoard:

    EMPTY_BOARD = "---------"
    PARTIAL_BOARD = "X---O----"
    FULL_BOARD = "XOXOXOXOX"

    def test_populate_board_string(self):
        empty = SmallBoardStyle._populate_board_string(self.EMPTY_BOARD)
        partial = SmallBoardStyle._populate_board_string(self.PARTIAL_BOARD)
        full = SmallBoardStyle._populate_board_string(self.FULL_BOARD)
        assert "-" not in empty
        assert empty.isnumeric()
        assert "X" in partial
        assert full.isalpha()

    def test_format_board_string(self):
        empty = SmallBoardStyle._format_board_string(self.EMPTY_BOARD)
        expected = "---\n---\n---\n"
        assert empty == expected

    def test_build_board_string(self):
        empty = SmallBoardStyle.build_board_string(self.EMPTY_BOARD)
        full = SmallBoardStyle.build_board_string(self.FULL_BOARD)
        assert empty == "123\n456\n789\n"
        assert full == "XOX\nOXO\nXOX\n"