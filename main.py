from argparse import ArgumentParser, Namespace

from game_parser import (build_ranking_table, print_sorted_ranking_table,
                         sort_ranking_table)


def _init_args() -> Namespace:
    parser = ArgumentParser(
        description="Calculate the ranking table for a league.")
    parser.add_argument(
        "input_file", help="Path to the input file containing game results (one per line)")
    args = parser.parse_args()
    return args


def main():
    args = _init_args()
    ranking_table = build_ranking_table(args.input_file)
    sorted_ranking_table = sort_ranking_table(ranking_table)
    print_sorted_ranking_table(sorted_ranking_table)


if __name__ == '__main__':
    main()
