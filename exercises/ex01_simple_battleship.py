"""EX01 - Simple Battleship - A cute step toward Battleship."""

__author__ = "730475919"

# 3 color boxes and the corresponding strings
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

try:
    # Prompting for Player 1 input
    player1_input = int(input("Pick a secret boat location between 1 and 4: "))

    # Checking if the input is within the valid range
    if 1 <= player1_input <= 4:
        # Input is valid and between 1 and 4. Continue as planned
        pass
    else:
        # Input is valid but not within 1 and 4. Print error message and exit
        print(f"Error! {player1_input} too {'low' if player1_input < 1 else 'high'}!")
        exit()

except ValueError:
    #  Input is invalid. It is not an integer. Print error message and exit
    print("Error! Please enter a valid integer between 1 and 4.")
    exit()

try:
    # Prompting for Player 2 input
    player2_input = int(input("Guess a number between 1 and 4: "))

    # Checking if the input is within the valid range
    if 1 <= player2_input <= 4:
        # Input is valid and between 1 and 4. Continue as planned
        pass
    else:
        # Input is valid but not within 1 and 4. Print error message and exit
        print(f"Error! {player2_input} too {'low' if player2_input < 1 else 'high'}!")
        exit()

except ValueError:
    #  Input is invalid. It is not an integer. Print error message and exit
    print("Error! Please enter a valid integer between 1 and 4.")
    exit()

# Linking result variable to correct color based on whether the inputs match
true_battleship_location = RED_BOX if player2_input == player1_input else WHITE_BOX

# Building the full string of colored boxes
emoji_string = ""
for box_number in range(1, 5):
    if box_number == player2_input:
        emoji_string += true_battleship_location
    else:
        emoji_string += BLUE_BOX

# Printing the string of colored boxes
print(emoji_string)

# Printing the string of text that describes the outcome
if player2_input == player1_input:
    print("Correct! You hit the ship.")
else:
    print("Incorrect! You missed the ship.")