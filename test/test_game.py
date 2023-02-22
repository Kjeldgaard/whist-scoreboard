from game import Game


def test_game_begin(monkeypatch):
    inputs = iter(["-100", "Niels", "Anders", "Mads", "Stef", "q"])
    monkeypatch.setattr('builtins.input', lambda name: next(inputs))
    game = Game()
    game.begin_game()
    score = game.get_total_score()
    assert score == -400


def test_game_add_round(monkeypatch):
    inputs = iter(["-100", "Niels", "Anders", "Mads", "Stef", "q", "10", "r", "10", "w", "l", "w", "l"])
    monkeypatch.setattr('builtins.input', lambda name: next(inputs))
    game = Game()
    game.begin_game()
    game.add_round()
    score = game.get_total_score()
    assert score == -400


