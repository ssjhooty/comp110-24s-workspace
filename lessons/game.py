"""Number Guessing Game."""
from random import randint

SECRET: int = randint(1,5)
correct: bool = False

while correct == False: # could also write "while not correct"
    guess: int = int(input("Guess a number: "))
    if guess == SECRET:
        print(f"Correct! {guess} is the number!")
        # something to help us exit
        correct = True
    elif guess > SECRET:
        print("Too high. Guess lower.")
    else:
        print("Too low. Guess higher.")