"""One Shot Battleship."""

__author__ = "730475919"

# Part 1

# Establishing constants
grid_size = 4
secret_row = 3
secret_column = 2

# Establishing Part 2 constants
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

# Prompting for a row guess
guess_row = int(input("Guess a row: "))

# Notifying user of invalid row guess
while guess_row < 1 or guess_row > grid_size:
    guess_row = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))

# Prompting for a column guess
guess_column = int(input("Guess a column: "))

# Notifying user of invalid column guess
while guess_column < 1 or guess_column > grid_size:
    guess_column = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))

# Part 2

#row_counte is the location placer of the result box
# Establishing counter variables and printing the emoji row
column_counte = 1
while column_counte <= grid_size:
    emoji_row = ""
    row_counte = 1
    while row_counte <= grid_size:
        if guess_column == column_counte and guess_row == row_counte:
            if guess_column == secret_column and guess_row == secret_row:
                emoji_row += RED_BOX
            else:
                emoji_row += WHITE_BOX
        else:
            emoji_row += BLUE_BOX
        column_counte += 1
    row_counte += 1
    print(emoji_row)
    

# Printing text strings based on outcome
if guess_row == secret_row and guess_column == secret_column:
    print("Hit!")
elif guess_row == secret_row:
    print("Close! Correct row, wrong column.")
elif guess_column == secret_column:
    print("Close! Correct column, wrong row.")
else:
    print("Miss!")