import pytest

from tictactoe import TicTacToeBoard


def test_update_game_state():
    start = "---------"
    new = TicTacToeBoard._get_updated_game_state(start, 0, "X")
    assert new == "X--------"
