from src.whist_scoreboard import whist_scoreboard


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
            "e",
        ]
    )
    monkeypatch.setattr("builtins.input", lambda name: next(inputs))
    whist_scoreboard.main()
