# League Ranking Calculator

This calculator determines the ranking table for a league based on game results.

## Input/Output

The input and output are text-based.

### Input

The input expects a file containing the results of games, with one game per line. Each line represents a game between two teams, with the format `team1_name team1_score, team2_name team2_score`. For example:

```
TeamA 3, TeamB 1
TeamC 2, TeamD 2
```

> Example input files can be found in `tests/samples/sample_input.txt`.

### Output

The output is displayed in stdout and consists of the ranking table, ordered from most to least points. Each team's ranking is accompanied by their total points. If two or more teams have the same number of points, they will have the same rank and be printed in alphabetical order.

- The output will be ordered from most to least points, following the format specified in
`tests/samples/sample_output.txt` with stdout.

Example output format:

```
1. TeamA, 6 pts
2. TeamC, 4 pts
2. TeamD, 4 pts
3. TeamB, 1 pt
4. TeamE, 0 pts
```

> An example of the expected output can be found in `tests/samples/sample_output.txt`.

## Rules

### Scoring Rules

- **Win**: 3 points
- **Draw**: 1 point
- **Loss**: 0 points

## Local Setup

### Pre-requisites

- Python 3.8 or higher

### Running

To run the program, execute the following command:

```sh
python main.py <input_file>
```

> Replace <input_file> with the path to your input file containing game results.

### Testing

To run the unit tests, execute the following command:

```sh
python -m unittest tests.test_game_parser
```
