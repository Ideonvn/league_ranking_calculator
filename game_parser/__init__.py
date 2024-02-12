from collections import Counter
from typing import List, Tuple

from game_parser.serializers import parse_input


def build_ranking_table(filename: str) -> Counter:
    """
    Build a ranking table based on game results stored in a file.

    Parameters:
    - filename (str): The name of the file containing game results.

    Returns:
    - Counter: A Counter object representing the ranking table.
    """
    ranking_table = Counter()
    for game in parse_input(filename):
        ranking_table[game.team_1.name] += game.team_1.points
        ranking_table[game.team_2.name] += game.team_2.points
    return ranking_table


def sort_ranking_table(teams: Counter) -> List[Tuple[str, int]]:
    """
    Sort a ranking table.

    Parameters:
    - teams (Counter): The ranking table to be sorted.

    Returns:
    - List[Tuple[str, int]]: A list of tuples representing teams and their points, sorted by points in descending order.
    """
    return sorted(teams.items(), key=lambda x: (-x[1], x[0]))


def print_sorted_ranking_table(teams: List[Tuple[str, int]]) -> None:
    """
    Print a sorted ranking table.

    Parameters:
    - teams (List[Tuple[str, int]]): The ranking table to be printed.
    """
    for rank, (team, points) in enumerate(teams, start=1):
        print(f"{rank}. {team}, {points} pts")
