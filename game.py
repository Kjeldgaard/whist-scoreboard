from collections import namedtuple
from prettytable import PrettyTable
from player import Player

Score = namedtuple('Score', 'win loss')

class Game():
    def __init__(self):
        self.total_score = float(0)
        self.to_account = float(0)
        self.num_of_players = 0
        self.players = list()
        self.start_score = float(0)
        self.num_of_rounds = 0

    def _set_start_score(self, start_score):
        self.start_score = start_score

    def _update_total_score(self):
        score = 0
        for player in self.players:
            score += player.get_total_score()
        self.total_score = score

    def _update_to_account(self):
        to_account = 0
        for player in self.players:
            to_account += player.get_to_account()
        self.to_account = to_account

    def _update_scores(self):
        self._update_total_score()
        self._update_to_account()

    def _add_player(self, player: Player):
        self.players.append(player)
        self.num_of_players += 1
        self._update_scores()

    def get_total_score(self):
        return self.total_score

    def get_to_account(self):
        return self.to_account

    def _add_players(self):
        num_of_players = 0
        names = list()

        print("Input players name, minimum of 4 players are required. Write 'q' when done")
        while True:
            name = input(f"Player {num_of_players + 1}: ")
            if num_of_players >= 4 and name == "q":
                print(f"Number of players is {num_of_players}")
                break
            if name == 'q':
                continue

            if name in names:
                print(f"{name} is already entered")
                continue

            # Add new player to game
            names.append(name)
            new_player = Player(name=name, start_score=self.start_score)
            self._add_player(new_player)
            num_of_players += 1

    def begin_game(self):
        print("Welcome to Whist Scoreboard")
        while True:
            start_score_str = input("Enter start score: ")
            try:
                start_score = float(start_score_str)
                break
            except ValueError:
                print(f"'{start_score_str}' is not a valid number, try again")

        print(f"Start score is {start_score}")
        self._set_start_score(start_score)

        self._add_players()

    def add_round(self):
        score = self._get_score()

        print(f"Winning score is {score.win} and losing score is {score.loss}")

        for player in self.players:
            while True:
                result = input(f"Result for {player.get_name()}: (w)in, (l)ose, (d)ealer, or (p)enalty? ")
                match result:
                    case 'w':
                        player.add_score(score.win)
                        break
                    case 'l':
                        player.add_score(score.loss)
                        break
                    case 'd':
                        player.add_score(0)
                        break
                    case 'p':
                        player.add_score(-75)
                        break
                    case _:
                        pass
        self.num_of_rounds += 1
        self._update_scores()
        self.print_scores()

    def print_scores(self):
        tab = PrettyTable()
        index = ["Start"]
        index.extend(range(1, self.num_of_rounds + 1))
        index.append("Total")
        index.append("To account")
        tab.add_column("", index)
        for player in self.players:
            tab.add_column(player.get_name(), player.get_scoring())
        tab.float_format = '.2'
        print(tab)

    def _compute_score(self, ticks: int, modifier: bool, result: int) -> namedtuple:
        finale_score = Score(0, 0)
        if ticks == 0:
            # Oplægger
            if result > ticks:
                score = 16 * 2 * result
                finale_score = Score(score / 3, -score)
            else:
                score = 16
                finale_score = Score(3 * score, -score)

        elif ticks == 1 and not modifier:
            # Sol
            if result > ticks:
                score = 4 * 2 * (result - ticks)
                finale_score = Score(score / 3, -score)
            else:
                score = 4
                finale_score = Score(3 * score, -score)

        elif ticks == 1 and modifier:
            # Ren sol
            if result > ticks:
                score = 8 * 2 * (result - ticks)
                finale_score = Score(score / 3, -score)
            else:
                score = 8
                finale_score = Score(3 * score, -score)

        elif ticks > result:
            # Bet
            modifier_multiplier = 1
            if modifier:
                modifier_multiplier = 2
            score = modifier_multiplier * 2**(ticks - 7) * 2 * (ticks - result)
            finale_score = Score(score, -score)

        else:
            # Plain
            modifier_multiplier = 1
            if modifier:
                modifier_multiplier = 2
            score = modifier_multiplier * 2**(ticks - 7) * (result - ticks + 1)
            finale_score = Score(score, -score)
        return finale_score

    def _get_result(self) -> int:
        while True:
            result = input(f"What was the result? ")
            if not result.isnumeric():
                continue
            else:
                return int(result)

    def _get_score(self) -> namedtuple:
        modifier = False
        ticks = 0
        while True:
            input_ticks = input("What was the bid? Ticks, (s)ol, (r)en sol, (o)plægger? ")
            match input_ticks:
                case 's':
                    ticks = 1
                    break
                case 'r':
                    ticks = 0
                    break
                case 'o':
                    ticks = 1
                    modifier = True
                    break
                case '7' | '8' | '9' | '10' | '11' | '12' | '13':
                    ticks = int(input_ticks)
                    while True:
                        input_modifier = input(f"{input_ticks} ticks? (r)en, (h)alv, (v)ip, (s)ans, (g)ode? ")
                        match input_modifier:
                            case 'r':
                                break
                            case 'h' | 'v' | 's' | 'g':
                                modifier = True
                                break
                            case '_':
                                continue
                    break
                case '_':
                    continue
        result = self._get_result()

        score = self._compute_score(ticks, modifier, result)

        return score
