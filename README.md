# League Ranking Calculator

This calculator will calculate the ranking table for a league.

## Input/Output

The input and output will always be in be text.

- The input expects a file name (`input_file` argument), the file contains results of games, one per line. See `tests/samples/sample_input.txt` for details.
- The output will be ordered from most to least points, following the format specified in
`tests/samples/sample_output.txt` with stdout.

## Rules

### Scoring Rules

| Outcome  | Points  |
| -------- | ------- |
| Win      | 3       |
| Draw     | 1       |
| Lose     | 0       |

### Output Rules

If two or more teams have the same number of points, they will have the same rank and be
printed in alphabetical order.

## Local Setup

### Pre-requisites

- Python 3.8+

```sh
python main.py tests/samples/sample_input.txt
```

## Testing

```sh
python -m unittest tests.test_game_parser
```
