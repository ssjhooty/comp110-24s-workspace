import random

# Establishing box constants
EMPTY_CELL: str = "\U0001F7E6"
MISS_CELL: str = "\U00002B1C"
HIT_CELL: str = "\U0001F7E5"

def input_guess(grid_size, row_or_column):
    assert row_or_column or "row" and row_or_column == "column"
    while True:
        guess = input(f"Guess a {row_or_column}: ")
# Ensuring guess is a digit and converting it into an integer type if it is
        if guess.isdigit():
            guess = int(guess)
            if 1 <= guess <= grid_size:
                return guess
            else:
                print(f"The grid is only {grid_size} by {grid_size}. Try again.")
        else:
            print("Invalid input. Please enter a number.")

# Defining print_grid function
def print_grid(grid_size, row_guess, col_guess, correct_guess):

# Establishing the types for the 4 inputs
    grid_size = int
    row_guess = int
    col_guess = int
    correct_guess = bool
    
# Establishing the output for all the non-guessed squares
    grid = [[EMPTY_CELL for _ in range(grid_size)] for _ in range(grid_size)]
# Establishing the output for the guess square
    if correct_guess:
        grid[row_guess - 1][col_guess - 1] = HIT_CELL
    else:
        grid[row_guess - 1][col_guess - 1] = MISS_CELL
    for row in grid:
        print(''.join(row))

# Establishing the correct guess function
def correct_guess(secret_row, secret_col, row_guess, col_guess):
    return secret_row == row_guess and secret_col == col_guess

def input_guess(grid_size):
    guess_row = int(input(f"Guess a row (1-{grid_size}): "))
    while guess_row < 1 or guess_row > grid_size:
        guess_row = int(input(f"The grid is only 1-{grid_size} by 1-{grid_size}. Try again: "))
    guess_col = int(input(f"Guess a column (1-{grid_size}): "))
    while guess_col < 1 or guess_col > grid_size:
        guess_col = int(input(f"The grid is only 1-{grid_size} by 1-{grid_size}. Try again: "))
    return guess_row, guess_col

def print_grid(grid_size, guess_row, guess_col, is_correct):
    BLUE_BOX = "\U0001F7E6"
    RED_BOX = "\U0001F7E5"
    WHITE_BOX = "\U00002B1C"
    
    for i in range(1, grid_size + 1):
        emoji_row = ""
        for j in range(1, grid_size + 1):
            if guess_row == i and guess_col == j:
                if is_correct:
                    emoji_row += RED_BOX
                else:
                    emoji_row += WHITE_BOX
            else:
                emoji_row += BLUE_BOX
        print(emoji_row)

def correct_guess(secret_row, secret_col, row_guess, col_guess):
    return secret_row == row_guess and secret_col == col_guess

def main(grid_size, secret_row, secret_col):
    total_turns = 5
    current_turn = 0
    while current_turn < total_turns:
        current_turn += 1
        print(f"=== Turn {current_turn}/{total_turns} ===")
        guess_row, guess_col = input_guess(grid_size)
        is_correct = correct_guess(secret_row, secret_col, guess_row, guess_col)
        print_grid(grid_size, guess_row, guess_col, is_correct)
        if is_correct:
            print(f"Hit! You won in {current_turn}/{total_turns} turns!")
            return
        else:
            print("Miss!")
    print(f"X/{total_turns} - Better luck next time!")

if __name__ == "__main__":
    grid_size = random.randint(3, 5)
    secret_row = random.randint(1, grid_size)
    secret_col = random.randint(1, grid_size)
    main(grid_size, secret_row, secret_col)






import random

# Establishing box constants
EMPTY_CELL: str = "\U0001F7E6"
MISS_CELL: str = "\U00002B1C"
HIT_CELL: str = "\U0001F7E5"

def input_guess(grid_size: int, row_or_column: str) -> int:
    while True:
        guess = input(f"Guess a {row_or_column}: ")
# Ensuring guess is a digit and converting it into an integer type if it is
        if guess.isdigit():
            guess = int(guess)
            if 1 <= guess <= grid_size:
                return guess
            else:
                print(f"The grid is only 1-{grid_size} by 1-{grid_size}. Try again.")
        else:
            print("Invalid input. Please enter a number.")

# Establishing print_grid function
def print_grid(grid_size: int, row_guess: int, col_guess: int, correct_guess: bool) -> None:
    grid = [[EMPTY_CELL for _ in range(grid_size)] for _ in range(grid_size)]
    if correct_guess:
        grid[row_guess - 1][col_guess - 1] = HIT_CELL
    else:
        grid[row_guess - 1][col_guess - 1] = MISS_CELL
    for row in grid:
        print(''.join(row))

# Establishing the correct guess function
def correct_guess(secret_row: int, secret_col: int, row_guess: int, col_guess: int) -> bool:
    return secret_row == row_guess and secret_col == col_guess

# Establishing the main function
def main(grid_size: int, secret_row: int, secret_col: int) -> None:
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