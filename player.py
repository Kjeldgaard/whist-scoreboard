class Player:
    def __init__(self, name: str, start_score: float) -> None:
        self.name = name
        self.score_per_round = list()
        self.start_score = start_score
        self.total_score = 0
        self.to_account = 0
        self._update_scores()

    def _update_total_score(self):
        self.total_score = self.start_score + sum(self.score_per_round)

    def _update_to_account(self):
        total_score = self.total_score
        self.to_account = 0
        divisor = 0
        while total_score < 0:
            self.to_account += max(-100, total_score) / max(divisor, 1)
            divisor += 1
            total_score += 100
        self.to_account = abs(self.to_account)

    def _update_scores(self):
        self._update_total_score()
        self._update_to_account()

    def add_score(self, score: float):
        self.score_per_round.append(score)
        self._update_scores()

    def get_total_score(self):
        return self.total_score

    def get_to_account(self):
        return self.to_account

    def edit_score(self, new_score: float):
        pass

    def get_scoring(self):
        score_out = list()
        score_out.append(self.start_score)
        score_out.extend(self.score_per_round)
        score_out.append(self.total_score)
        score_out.append(self.to_account)
        return score_out

    def get_name(self) -> str:
        return self.name
