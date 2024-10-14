class TennisGame2:
    SCORE_MAPPING = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1_points = 0
        self.p2_points = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.p1_score()
        elif player_name == self.player2_name:
            self.p2_score()
        else:
            raise ValueError("Invalid player name")


    def _get_advantage_or_win_score(self):
        score_diff = self.p1_points - self.p2_points
        if score_diff >= 2:
            return "Win for player1"
        if score_diff <= -2:
            return "Win for player2"
        if score_diff == 1:
            return "Advantage player1"
        if score_diff == -1:
            return "Advantage player2"
        if score_diff == 0:
            return "Deuce"

    def score(self):
        result = ""
        if max(self.p1_points, self.p2_points) >= 4:
            return self._get_advantage_or_win_score()

        if self.p1_points == self.p2_points and self.p1_points < 3:
            result = self.SCORE_MAPPING.get(self.p1_points, "Invalid")   
            result += "-All"
        if self.p1_points == self.p2_points and self.p1_points > 2:
            result = "Deuce"

        p1_res = ""
        p2_res = ""
        if self.p1_points > 0 and self.p2_points == 0:
            p1_res = self.SCORE_MAPPING.get(self.p1_points, "Invalid")   
            p2_res = "Love"
            result = p1_res + "-" + p2_res
        if self.p2_points > 0 and self.p1_points == 0:
            p2_res = self.SCORE_MAPPING.get(self.p2_points, "Invalid")   
            p1_res = "Love"
            result = p1_res + "-" + p2_res

        if self.p1_points > self.p2_points and self.p1_points < 4:
            p1_res = self.SCORE_MAPPING.get(self.p1_points, "Invalid")   
            p2_res = self.SCORE_MAPPING.get(self.p2_points, "Invalid")   
            result = p1_res + "-" + p2_res
        if self.p2_points > self.p1_points and self.p2_points < 4:
            p2_res = self.SCORE_MAPPING.get(self.p2_points, "Invalid")   
            p1_res = self.SCORE_MAPPING.get(self.p1_points, "Invalid")
            result = p1_res + "-" + p2_res
            
        return result

    def set_p1_score(self, number):
        for i in range(number):
            self.p1_score()

    def set_p2_score(self, number):
        for i in range(number):
            self.p2_score()

    def p1_score(self):
        self.p1_points += 1

    def p2_score(self):
        self.p2_points += 1
