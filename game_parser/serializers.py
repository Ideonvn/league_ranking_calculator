from typing import Iterator

from game_parser.exceptions import GameParseException


WIN_POINTS = 3
DRAW_POINTS = 1
LOSE_POINTS = 0


class Team:
    """Class to represent a team."""

    def __init__(self, name: str, score: int) -> None:
        """
        Initialize a Team object.

        Parameters:
        - name (str): The name of the team.
        - score (int): The score of the team.
        """
        self.name = name
        self.score = score
        self.points = LOSE_POINTS


class Game:
    """Class to represent a game between two teams."""

    def __init__(self, raw_line: str) -> None:
        """
        Initialize a Game object.

        Parameters:
        - raw_line (str): A raw string containing information about the game.
        """
        self._parse_game(raw_line)
        self._calculate()

    def _parse_game(self, raw_line: str) -> None:
        """
        Parse the raw line to extract information about the teams.

        Parameters:
        - raw_line (str): A raw string containing information about the game.

        Raises:
        - GameParseException: If the raw line cannot be parsed correctly.
        """
        teams = raw_line.strip().split(',')
        if len(teams) != 2:  # Only support 2 team games
            raise GameParseException(raw_line)

        self.team_1: Team = self._parse_team(teams[0])
        self.team_2: Team = self._parse_team(teams[1])
        # Duplicate team name is not supported
        if self.team_1.name == self.team_2.name:
            raise GameParseException(raw_line)

    def _parse_team(self, raw_team: str) -> Team:
        """
        Parse a raw string representing a team.

        Parameters:
        - raw_team (str): A raw string representing a team.

        Returns:
        - Team: A Team object representing the parsed team.

        Raises:
        - GameParseException: If the raw team data cannot be parsed correctly.
        """
        try:
            team_data = raw_team.strip().rsplit(' ', 1)
            # Splitting the team name and score, expecting 2 results only
            if len(team_data) != 2:
                raise GameParseException(raw_team)
            name = team_data[0]
            # Invalid (NaN) score will raise exception
            score = int(team_data[1])
            if score < 0:  # Negative scores are not supported
                raise GameParseException(raw_team)
            return Team(name, score)
        except:
            raise GameParseException(raw_team)

    def _calculate(self):
        """
        Calculate points for each team based on the game result.
        """
        if self.team_1.score > self.team_2.score:
            self.team_1.points = WIN_POINTS
        elif self.team_1.score < self.team_2.score:
            self.team_2.points = WIN_POINTS
        else:
            self.team_1.points = DRAW_POINTS
            self.team_2.points = DRAW_POINTS


def parse_input(filename: str) -> Iterator[Game]:
    """
    Parse a file containing game data and yield Game objects.

    Parameters:
    - filename (str): The name of the file containing game data.

    Yields:
    - Game: A Game object representing each game parsed from the file.
    """
    with open(filename, 'r') as file:
        for line in file:
            yield Game(line)
