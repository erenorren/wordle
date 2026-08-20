import pytest
from src.game import WordleGame

def test_evaluate_guess_correct():
    game = WordleGame()
    game.target_word = "CYBER"
    result = game.evaluate_guess("CYBER")
    assert result == ["CORRECT", "CORRECT", "CORRECT", "CORRECT", "CORRECT"]

def test_evaluate_guess_partial():
    game = WordleGame()
    game.target_word = "CYBER"
    result = game.evaluate_guess("CRAZY")
    assert result[0] == "CORRECT"   # C
    assert result[1] == "PRESENT"   # R (ada di CYBER tapi beda posisi)

def test_game_over_loss():
    game = WordleGame(max_attempts=1)
    game.make_move("WRONG")
    assert game.is_game_over() is True
    assert game.is_won() is False