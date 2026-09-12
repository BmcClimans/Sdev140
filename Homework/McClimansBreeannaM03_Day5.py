"""
Make use of the random number feature in Python to simulate the rolling of a pair of dice.  
Get input from operator for the number of rolls and retrieve an optional seed number (zero to use the system clock).  
Encase this in a while loop to allow multiple runs.  
Experiment with two runs with no seed number, two runs with the same seed number and a run with a different seed number.
"""

import random

# Constants for min and max random numbers on a die
MIN: int = 1
MAX: int = 6


def get_rolls() -> int:
    # Get the number of rolls from the user
    while True:
        try:
            rolls: int = int(input("Enter the number of rolls: "))

            if rolls <= 0:
                print("Please enter a positive integer.")
                continue
            return rolls

        except ValueError:
            print("Invalid input. Please enter a positive integer.")


def get_seed() -> int:
    # Get the optional seed number from the user
    while True:
        try:
            seed: int = int(input("Enter an optional seed number (0 to use system clock): "))

            if seed == 0:
                random.seed()
            else:
                random.seed(seed)

            return seed

        except ValueError:
            print("Invalid input. Please enter an integer.")


def roll_dice(rolls: int) -> None:
    for roll in range(rolls):
        die1: int = random.randint(MIN, MAX)
        die2: int = random.randint(MIN, MAX)
        print(f"Roll {roll + 1}: Die 1: {die1}, Die 2: {die2}")


def main() -> None:
    while True:
        rolls: int = get_rolls()
        get_seed()
        roll_dice(rolls)
        
        #ask the user if they want to run again
        while True:
            again: str = input(str.lower("Do you want to roll again? (y/n): "))
            if again == 'y':
                break
            elif again == "n":
                print("Thank you for playing!")
                return
            else:
                print("Invalid input. Please enter 'y' or 'n'.")


if __name__ == "__main__":
    main()