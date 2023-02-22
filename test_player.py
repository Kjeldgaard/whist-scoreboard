from player import Player

def test_player_name():
    player = Player(name="john", start_score=-100)
    name = player.get_name()
    assert name == "john"

def test_player_score():
    player = Player(name="john", start_score=-100)
    player.add_score(-200)
    score = player.get_total_score()
    assert score == float(-300)

def test_player_account():
    player = Player(name="john", start_score=-100)
    player.add_score(-200)
    to_account = player.get_to_account()
    assert to_account == float(250)

def test_player_scoring():
    player = Player(name="john", start_score=-100)
    player.add_score(-200)
    player.add_score(-16)
    score_list = player.get_scoring()
    assert score_list == [-100, -200, -16, -316, 255.33333333333334]
