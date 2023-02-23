from src import whist_scoreboard


def test_whist(monkeypatch):
    inputs = iter(
        [
            "-100",
            "Niels",
            "Mads",
            "Anders",
            "Stef",
            "q",
            "z",
            "a",
            "9",
            "r",
            "9",
            "w",
            "w",
            "l",
            "l",
            "q",
        ]
    )
    monkeypatch.setattr("builtins.input", lambda name: next(inputs))
    whist_scoreboard.main()


def test_whist_edit(monkeypatch):
    inputs = iter(
        [
            "-100",
            "Niels",
            "Mads",
            "Anders",
            "Stef",
            "q",
            "a",
            "9",
            "r",
            "9",
            "w",
            "w",
            "l",
            "l",
            "e",
            "Mads",
            "1",
            "-75",
            "q",
        ]
    )
    monkeypatch.setattr("builtins.input", lambda name: next(inputs))
    whist_scoreboard.main()
