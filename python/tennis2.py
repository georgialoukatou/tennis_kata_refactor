from typing import Dict


class TennisGame2:
    SCORE_MAPPING: Dict[int, str] = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}
    DEUCE: str = "Deuce"
    SCORE_ADVANTAGE_POSITIVE: int = 1
    SCORE_ADVANTAGE_NEGATIVE: int = -1
    SCORE_WIN_POSITIVE: int = 2
    SCORE_WIN_NEGATIVE: int = -2
    SCORE_DEUCE: int = 0

    def __init__(self, player1_name: str, player2_name: str) -> None:
        if player1_name == player2_name:
            raise ValueError("Players have the same name")
        self._player1_name: str = player1_name
        self._player2_name: str = player2_name
        self._p1_points: int = 0
        self._p2_points: int = 0

    def won_point(self, player_name: str) -> None:
        if player_name == self._player1_name:
            self._increment_p1_score()
        elif player_name == self._player2_name:
            self._increment_p2_score()
        else:
            raise ValueError("Invalid player name")

    def score(self) -> str:
        if max(self._p1_points, self._p2_points) >= 4:

            return self._get_advantage_or_win_score()

        return self._get_regular_score()

    def _calculate_score_difference(self) -> int:
        score_diff: int = self._p1_points - self._p2_points
        return score_diff

    def _get_advantage_or_win_score(self) -> str:
        score_diff: int = self._calculate_score_difference()
        if score_diff == self.SCORE_ADVANTAGE_POSITIVE:
            return f"Advantage {self._player1_name}"
        elif score_diff == self.SCORE_ADVANTAGE_NEGATIVE:
            return f"Advantage {self._player2_name}"
        elif score_diff >= self.SCORE_WIN_POSITIVE:
            return f"Win for {self._player1_name}"
        elif score_diff <= self.SCORE_WIN_NEGATIVE:
            return f"Win for {self._player2_name}"
        elif score_diff == self.SCORE_DEUCE:
            return self.DEUCE
        else:
            return "Invalid Score Difference"

    def _increment_p1_score(self) -> None:
        self._p1_points += 1

    def _increment_p2_score(self) -> None:
        self._p2_points += 1

    def _get_regular_score(self) -> str:
        p1_res: str = self.SCORE_MAPPING.get(self._p1_points, "Invalid")
        p2_res: str = self.SCORE_MAPPING.get(self._p2_points, "Invalid")

        if self._calculate_score_difference() == 0:
            if self._p1_points == 3:
                return self.DEUCE
            return f"{p1_res}-All"

        return f"{p1_res}-{p2_res}"

    def set_p1_score(self, number: int) -> None:
        if number < 0:
            raise ValueError("Score cannot be negative.")
        for _ in range(number):
            self._increment_p1_score()

    def set_p2_score(self, number: int) -> None:
        if number < 0:
            raise ValueError("Score cannot be negative.")
        for _ in range(number):
            self._increment_p2_score()
