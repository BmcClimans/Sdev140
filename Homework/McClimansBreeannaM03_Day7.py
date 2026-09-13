"""
Write a program that takes the number of times to roll two dice from the console.  Do a tally of the result number (2 through 12) in an indexed list.  
When program completes this experiment, you will display the tallies from the list and use them to calculate the percent of times each number occurred. 
Additional item: Store the expected percent for each result number in a stable table and display these alongside the corresponding results of your experiments in your display.  
If you run two different experiments, one using a relatively small number (<500) and another with a large number (say a million), you will see a demonstration of the law of large numbers:  
The larger your sample size, the closer to the theoretical probability you will get.
Hint: Use formatted print lines to make results professionally lined up.
"""

import random

#constants for min and max random numbers on a die
MIN_DIE: int = 1
MAX_DIE: int = 6

#expected percentages for each possible sum of two dice (2-12)
EXPECTED_PERCENTAGES: list[float] = [2.78, 5.56, 8.33, 11.11, 13.89, 16.67, 13.89, 11.11, 8.33, 5.56, 2.78]

def get_rolls() -> int:
    #get the number of rolls from the user
    while True:
        try:
            rolls: int = int(input("Enter the number of rolls: "))

            if rolls <= 0:
                print("Please enter a positive integer.")
                continue
            return rolls

        except ValueError:
            print("Invalid input. Please enter a positive integer.")

def roll_dice(rolls: int) -> list[int]:
    #initialize a list to hold the tally of results (index 0 and 1 will be unused)
    tallies: list[int] = [0] * 11

    for _ in range(rolls):
        die1: int = random.randint(MIN_DIE, MAX_DIE)
        die2: int = random.randint(MIN_DIE, MAX_DIE)
        result: int = die1 + die2
        #increment the tally for the result (subtract 2 to align with index 0 for result 2)
        tallies[result-2] += 1

    return tallies

def display_results(tallies: list[int], rolls: int) -> None:
    #display the results, percentages, and expected percentages
    print("\nResults of rolling two dice:")
    print(f"{'Result':<10}{'Tally':<15}{'Percent':<15}{'Expected Percent':<10}")

    for result in range(2, 13):
        tally: int = tallies[result-2]
        percent: float = (tally / rolls) * 100
        expected: float = EXPECTED_PERCENTAGES[result-2]
        percent_str: str = f"{percent:.2f}%"
        expected_str: str = f"{expected:.2f}%"
        print(f"{result:<10}{tally:<15,}{percent_str:<15}{expected_str:<15}")

def main() -> None:
    rolls: int = get_rolls()
    tallies: list[int] = roll_dice(rolls)
    display_results(tallies, rolls)

if __name__ == "__main__":
    main()