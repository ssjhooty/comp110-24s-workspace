"""One Shot Battleship"""

__author__ = "730475919"

#Establishing constants.
grid_size: int = 4
secret_row: int = 3
secret_column: int = 2

#Defining the parameters of a valid guess.
def valid_guess(row, column):
    return 1 <= row <= grid_size and 1 <= column <= grid_size
def invalid_guess(row, column):
    return row<1 or row>grid_size and column<1 or column>grid_size

#Prompting for input.
guess_row: int = int(input("Guess a row: "))
guess_column: int = int(input("Guess a column: "))

#Printing the correct word string response based on user input.
if valid_guess(guess_row,guess_column) and guess_row == secret_row and guess_column == secret_column:
    print ("Hit!")
elif valid_guess(guess_row,guess_column) and guess_row != secret_row and guess_column != secret_column:
    print ("Miss!")
elif valid_guess(guess_row,guess_column) and guess_row == secret_row and guess_column != secret_column:
    print ("Close! Correct row, wrong column.")
elif valid_guess(guess_row,guess_column) and guess_row != secret_row and guess_column == secret_column:
    print ("Close! Correct column, wrong row.")
elif invalid_guess(guess_row,guess_column):
    print(f"The grid is only {grid_size} by {grid_size}. Try again:")

#Establishing more constants (for colored boxes).
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

#Creating the rules for printing the correct string of colored boxes in a grid format based on user input.
if valid_guess(guess_row,guess_column):
    def grid():
        guess_box = RED_BOX if guess_row == secret_row and guess_column == secret_column else WHITE_BOX
        row_number = 1

        while row_number <= grid_size:
            column_number = 1
            row_string = ""

            if row_number == guess_row:
                while column_number <= grid_size:
                    if column_number == guess_column:
                        row_string += guess_box
                    else:
                        row_string += BLUE_BOX
                    column_number += 1
            else:
                while column_number <= grid_size:
                    row_string += BLUE_BOX
                    column_number += 1

            print(row_string)
            row_number += 1

#Printing said grid.
grid()