# N Queens Solver

This program solves the N queens puzzle, where the challenge is to place N non-attacking queens on an N×N chessboard.

## Usage

```bash
./nqueens.py N
```

- `N` must be an integer greater than or equal to 4.

## Examples

```bash
./nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
```

## Error Handling

- If the program is called with the wrong number of arguments, it will print:
  ```
  Usage: nqueens N
  ```
- If `N` is not a number, it will print:
  ```
  N must be a number
  ```
- If `N` is smaller than 4, it will print:
  ```
  N must be at least 4
  ```

## Notes

- The script is written in Python 3.4.3.
- The code follows PEP 8 style guidelines.
