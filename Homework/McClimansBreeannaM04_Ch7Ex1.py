"""
1. Total Sales
Design a program that asks the user to enter a store’s sales for each day of the week. 
The amounts should be stored in a list. 
Use a loop to calculate the total sales for the week and display the result.
Make sure you use the loop to calculate the total AFTER you've had the user entered the numbers; 
don't keep a running total as the numbers are being entered.
"""

def main() -> None:
    #list to store sales for each day of the week
    sales: list[float] = []

    #get sales for each day of the week from user
    for day in range(1, 8):
        while True:
            try:
                amount: float = float(input(f"Enter sales for day {day}: "))
                if amount < 0:
                    print("Please enter a non-negative number.")
                    continue
                sales.append(amount)
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

    #calculate and display total sales using sum of list
    print(f"Total sales for the week: ${sum(sales):,.2f}")

if __name__ == "__main__":
    main()