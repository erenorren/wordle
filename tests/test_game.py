from src.game import ScrambleGame

def test_scramble_word_different_from_target():
    game = ScrambleGame()
    # Memastikan hasil acakan huruf tidak sama persis dengan kata asli
    scrambled_clean = game.scrambled_word.replace(" ", "")
    assert scrambled_clean != game.target_word
    assert sorted(scrambled_clean) == sorted(game.target_word)

def test_make_move_correct():
    game = ScrambleGame()
    game.target_word = "GREEN"
    assert game.make_move("GREEN") is True
    assert game.is_won() is True

def test_make_move_wrong():
    game = ScrambleGame()
    game.target_word = "GREEN"
    assert game.make_move("WATER") is False
    assert game.attempts == 2