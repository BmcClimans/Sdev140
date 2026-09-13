"""
Write a program that will ask the user to enter the amount of a purchase. 
The program should then compute the state and county sales tax. 
Assume the state sales tax is 5 percent and the county sales tax is 2.5 percent. 
The program should display the amount of the purchase, the state sales tax, 
the county sales tax, and the total sales tax.
design it so the subtasks are in functions.                     
Hint: Use the value 0.025 to represent 2.5 percent, and 0.05 to represent 5 percent.
"""

def get_purchase_amount() -> float:
    """Get the purchase amount from the user."""
    while True:
        try:
            amount: float = float(input("Enter the amount of the purchase: "))
            if amount < 0:
                print("Please enter a non-negative amount.")
                continue
            return amount
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def calculate_sales_tax(amount: float) -> tuple:
    """Calculate the state and county sales tax."""
    state_tax_rate: float = 0.05
    county_tax_rate: float = 0.025

    state_sales_tax: float = amount * state_tax_rate
    county_sales_tax: float = amount * county_tax_rate
    total_sales_tax: float = state_sales_tax + county_sales_tax
    total_cost: float = amount + total_sales_tax

    return state_sales_tax, county_sales_tax, total_sales_tax, total_cost

def display_results(amount: float, state_sales_tax: float, county_sales_tax: float, total_sales_tax: float, total_cost: float) -> None:
    """Display the purchase amount and sales tax details."""
    print(f"\nPurchase Amount: ${amount:,.2f}")
    print(f"State Sales Tax (5%): ${state_sales_tax:,.2f}")
    print(f"County Sales Tax (2.5%): ${county_sales_tax:,.2f}")
    print(f"Total Sales Tax: ${total_sales_tax:,.2f}")
    print(f"Total Cost: ${total_cost:,.2f}")

def main() -> None:
    """Main function to run the sales tax calculator."""
    amount: float = get_purchase_amount()
    state_sales_tax, county_sales_tax, total_sales_tax, total_cost = calculate_sales_tax(amount)
    display_results(amount, state_sales_tax, county_sales_tax, total_sales_tax, total_cost)

if __name__ == "__main__":
    main()