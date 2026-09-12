"""
Modify the program that you wrote for Exercise 6 so it handles the following exceptions:                              
It should handle any  exceptions that are raised when the file is opened and data is read from it.                            
It should handle any  exceptions that are raised when the items that are read from the file are converted to a number.
"""

def main() -> None:
    #Calculate the average of numbers in a file.
    filename: str = "numbers.txt"
    total: int = 0
    count: int = 0

    try:
        #open the file and read numbers
        with open(filename, 'r') as file:
            for line in file:
                try:
                    number: int = int(line.strip())
                    total += number
                    count += 1
                except ValueError:
                    print(f"Invalid number found in file: {line.strip()}")
    except FileNotFoundError:
        print(f"File not found: {filename}")
    except IOError:  # noqa: UP024
        print(f"Error reading file: {filename}")

    if count > 0:
        #calculate and display the average
        average: float = total / count
        print(f"The average of the numbers in {filename} is: {average:,.2f}")
    else:
        print("No valid numbers found in the file.")

if __name__ == "__main__":
    main()