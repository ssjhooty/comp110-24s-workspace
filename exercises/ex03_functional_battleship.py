"""Functional Battleship."""

__author__ = "730475919"

import random

# Establishing box constants
EMPTY_CELL: str = "\U0001F7E6"
MISS_CELL: str = "\U00002B1C"
HIT_CELL: str = "\U0001F7E5"


# Establishing input guess function
def input_guess(grid_size: int, row_or_column: str) -> int:
    """Prompting for the input guess, and delivering the appropriate textual response."""
    assert row_or_column == "row" or row_or_column == "column", "Invalid input. Expected 'row' or 'column'."
    while True:
        guess_str = input(f"Guess a {row_or_column}: ")
        try:
            guess = int(guess_str)
            if 1 <= guess <= grid_size:
                return guess
            else:
                print(f"The grid is only 1-{grid_size} by 1-{grid_size}. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")


# Establishing print grid function
def print_grid(grid_size: int, row_guess: int, col_guess: int, correct_guess: bool) -> None:
    """Printing the grid responsible for illustrating the result."""
    grid = [[EMPTY_CELL for _ in range(grid_size)] for _ in range(grid_size)]
    if correct_guess:
        grid[row_guess - 1][col_guess - 1] = HIT_CELL
    else:
        grid[row_guess - 1][col_guess - 1] = MISS_CELL
    for row in grid:
        print(''.join(row))


# Establishing the correct guess function
def correct_guess(secret_row: int, secret_col: int, row_guess: int, col_guess: int) -> bool:
    """Establishing what constitutes as a correct guess."""
    return secret_row == row_guess and secret_col == col_guess


# Establishing the main function
def main(grid_size: int, secret_row: int, secret_col: int) -> None:
    """Establishing the main function that brings the game all together."""
    total_turns = 5
    current_turn = 0
    while current_turn < total_turns:
        current_turn += 1
        print(f"=== Turn {current_turn}/{total_turns} ===")
        guess_row = input_guess(grid_size, "row")
        guess_col = input_guess(grid_size, "column")
        is_correct = correct_guess(secret_row, secret_col, guess_row, guess_col)
        print_grid(grid_size, guess_row, guess_col, is_correct)
        if is_correct:
            print(f"Hit! You won in {current_turn}/{total_turns} turns!")
            return
        else:
            print("Miss!")
    print(f"X/{total_turns} - Better luck next time!")


# Making it possible to actually run the program as a module
if __name__ == "__main__":
    grid_size = random.randint(3, 5)
    secret_row = random.randint(1, grid_size)
    secret_col = random.randint(1, grid_size)
    main(grid_size, secret_row, secret_col)