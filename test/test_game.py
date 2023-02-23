from src.game.game import Game


def test_game_begin(monkeypatch):
    inputs = iter(["-100", "Niels", "Anders", "Mads", "Stef", "q"])
    monkeypatch.setattr("builtins.input", lambda name: next(inputs))
    game = Game()
    game.begin_game()
    score = game.get_total_score()
    assert score == -400


def test_game_add_round(monkeypatch):
    inputs = iter(
        [
            "-100",
            "q",
            "Niels",
            "Anders",
            "Mads",
            "Stef",
            "MadsH",
            "q",
            "10",
            "r",
            "10",
            "w",
            "l",
            "w",
            "l",
            "d",
        ]
    )
    monkeypatch.setattr("builtins.input", lambda name: next(inputs))
    game = Game()
    game.begin_game()
    game.add_round()
    score = game.get_total_score()
    assert score == -500


def test_game_to_account(monkeypatch):
    inputs = iter(
        [
            "Test",
            "-100",
            "Niels",
            "Niels",
            "Anders",
            "Mads",
            "Stef",
            "MadsH",
            "q",
            "r",
            "10",
            "t",
            "w",
            "w",
            "p",
            "l",
            "d",
        ]
    )
    monkeypatch.setattr("builtins.input", lambda name: next(inputs))
    game = Game()
    game.begin_game()
    game.add_round()
    to_account = game.get_to_account()
    assert to_account == 563.3333333333333


def test_game_add_rounds(monkeypatch):
    inputs = iter(
        [
            "-100",
            "Niels",
            "Anders",
            "Mads",
            "Stef",
            "q",
            "s",
            "10",
            "w",
            "w",
            "w",
            "l",
            "o",
            "3",
            "w",
            "l",
            "w",
            "w",
            "9",
            "v",
            "8",
            "w",
            "l",
            "l",
            "w",
            "s",
            "1",
            "l",
            "l",
            "w",
            "l",
            "r",
            "0",
            "l",
            "w",
            "l",
            "l",
            "o",
            "0",
            "w",
            "l",
            "l",
            "l",
        ]
    )
    monkeypatch.setattr("builtins.input", lambda name: next(inputs))
    game = Game()
    game.begin_game()
    game.add_round()
    game.add_round()
    game.add_round()
    game.add_round()
    game.add_round()
    game.add_round()
    to_account = game.get_to_account()
    assert to_account == 400


def test_game_add_round2(monkeypatch):
    inputs = iter(
        [
            "-100",
            "Niels",
            "Anders",
            "Mads",
            "Stef",
            "q",
            "6",
            "10",
            "f",
            "v",
            "11",
            "w",
            "l",
            "w",
            "l",
        ]
    )
    monkeypatch.setattr("builtins.input", lambda name: next(inputs))
    game = Game()
    game.begin_game()
    game.add_round()
    score = game.get_total_score()
    assert score == -400
