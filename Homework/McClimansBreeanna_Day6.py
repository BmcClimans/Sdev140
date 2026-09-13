"""
A) Write a program that writes a series of random numbers.  
Number Range 1 to 500 integers. 
 Get user prompt for the total number to generate and write.

B) For the above created file read in and display all the numbers.  
Accumulate the total number as well as the sum of numbers.  
Display these as well as the average at the end.
"""

import random

MIN_NUMBER: int = 1
MAX_NUMBER: int = 500

def get_input() -> int:
    """Get the number of random numbers to generate from the user."""
    while True:
        try:
            count = int(input("Enter the number of random numbers to generate: "))
            if count <= 0:
                print("Please enter a positive integer.")
                continue
            return count
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

def write_random_numbers_to_file(filename: str, count: int) -> None:
    """Write a specified number of random numbers to a file."""
    with open(filename, 'w') as file:
        for _ in range(count):
            number = random.randint(MIN_NUMBER, MAX_NUMBER)
            file.write(f"{number}\n")

def read_random_numbers_from_file(filename: str) -> list:
    """Read random numbers from a file and return them as a list of integers."""
    numbers = []
    with open(filename, 'r') as file:
        for line in file:
            try:
                number = int(line.strip())
                numbers.append(number)
            except ValueError:
                print(f"Invalid number found in file: {line.strip()}")
    return numbers

def display_numbers_and_stats(numbers: list) -> None:
    """Display the numbers and their statistics."""
    total: int = sum(numbers)
    count: int = len(numbers)

    print("Random Numbers:")
    for number in numbers:
        print(number)
    
    print(f"\nTotal of the numbers: {total}")
    average: float = total / count if count > 0 else 0
    print(f"Average of the numbers: {average:,.2f}")
    print(f"Number of random numbers read from the file: {count}")

def main() -> None:
    filename: str = "random_numbers.txt"
    
    #get user input for the number of random numbers to generate
    count: int = get_input()

    #write random numbers to the file
    write_random_numbers_to_file(filename, count)

    #read random numbers from the file
    numbers: list = read_random_numbers_from_file(filename)

    #display the numbers and their statistics
    display_numbers_and_stats(numbers)

if __name__ == "__main__":
    main()