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

# Establishing counter variables and printing the emoji row
row_counter = 1
while row_counter <= grid_size:
    emoji_row = ""
    column_counter = 1
    while column_counter <= grid_size:
        if guess_column == column_counter and guess_row == row_counter:
            if guess_column == secret_column and guess_row == secret_row:
                emoji_row += RED_BOX
            else:
                emoji_row += WHITE_BOX
        else:
            emoji_row += BLUE_BOX
        column_counter += 1
    print(emoji_row)
    row_counter += 1

# Printing text strings based on outcome
if guess_row == secret_row and guess_column == secret_column:
    print("Hit!")
elif guess_row == secret_row:
    print("Close! Correct row, wrong column.")
elif guess_column == secret_column:
    print("Close! Correct column, wrong row.")
else:
    print("Miss!")




def invert(non_inverted: (dict[str, str])) -> dict[str, str]:
    """Function that inverts a dictionary."""
    inverted: dict[str, str] = {}
    values_seen = []   # List to keep track of the values seen so far
    for key, value in non_inverted.items():
        if value in values_seen:  # If a to-be key has already been recorded
            raise KeyError("Duplicate key was detected.")
        else:
            inverted[key] = value  # Establishing the new key assuming it is not a duplicate
            values_seen.append(value)
        inverted[value] = key  # Establishing the new value
    return inverted



def add_by_kind(by_kind: dict[str, list[str]], new_plant_kind: str, new_plant: str) -> None:
    """Add plant number under its kind."""
    if new_plant_kind in by_kind: # if the kind is already in the dictionary ("flower" is in by_kind)
        by_kind[new_plant_kind].append(new_plant)
    else: # if the kind is not in the dictionary ("fruit" is not in by_kind)
        by_kind[new_plant_kind] = []
        by_kind[new_plant_kind].append(new_plant)