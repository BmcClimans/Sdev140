"""
Assume a file containing a series of integers is named numbers.txt and exists on the computer’s disk. 
Write a program that calculates the average of all the numbers stored in the file.
"""

def main() -> None:
    """Calculate the average of numbers in a file."""
    filename: str = "numbers.txt"
    total: int = 0
    count: int = 0

    with open(filename, 'r') as file:
        for line in file:
            number: int = int(line.strip())
            total += number
            count += 1

    average: float = total / count 

    print(f"The average of the numbers in {filename} is: {average:,.2f}")

if __name__ == "__main__":
    main()