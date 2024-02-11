from typing import Counter
import unittest
from game_parser import build_ranking_table, sort_ranking_table
from game_parser.serializers import Game
from game_parser.exceptions import GameParseException


class TestGameParser(unittest.TestCase):

    def test_game_serializer_invalid_commas(self):
        raw_line = 'Lions 3, Snakes 3,Test 1'
        with self.assertRaises(GameParseException):
            Game(raw_line)

    def test_game_serializer_invalid_spaces(self):
        raw_line = 'Lions3, Snakes 3'
        with self.assertRaises(GameParseException):
            Game(raw_line)

    def test_game_serializer_invalid_scores(self):
        raw_line = 'Lions -1, Snakes 3'
        with self.assertRaises(GameParseException):
            Game(raw_line)

    def test_game_serializer_nan_scores(self):
        raw_line = 'Lions 0, Snakes A'
        with self.assertRaises(GameParseException):
            Game(raw_line)

    def test_game_serializer_points_win_lose(self):
        raw_line = 'Lions 1, Snakes 2'
        game = Game(raw_line)

        self.assertEqual(game.team_1.points, 0)
        self.assertEqual(game.team_2.points, 3)

    def test_game_serializer_points_draw(self):
        raw_line = 'Lions 1, Snakes 1'
        game = Game(raw_line)

        self.assertEqual(game.team_1.points, 1)
        self.assertEqual(game.team_2.points, 1)

    def test_build_ranking_table_with_sample_file(self):
        filename = 'tests/samples/sample_input.txt'
        ranking_table = build_ranking_table(filename)

        self.assertEqual(len(ranking_table), 5)
        self.assertEqual(ranking_table.get('Grouches'), 0)

    def test_sort_ranking_table_with_sample_file(self):
        ranking_table = Counter({'C': 2, 'A': 2, 'B': 4})
        sorted_ranking_table = sort_ranking_table(ranking_table)

        self.assertEqual(len(sorted_ranking_table), 3)
        self.assertEqual(sorted_ranking_table[0][0], 'B')
        self.assertEqual(sorted_ranking_table[1][0], 'A')
        self.assertEqual(sorted_ranking_table[2][0], 'C')


if __name__ == '__main__':
    unittest.main()
