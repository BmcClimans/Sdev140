"""
Write a program that calculates the amount of money a person would earn over a period of time 
if their salary is one penny the first day, two pennies the second day, and continues to double each day. 
The program should ask the user for the number of days. 
Display a table showing what the salary was for each day, then show the total pay at the end of the period. 
The output should be displayed in a dollar amount, not the number of pennies.
"""

# Get the number of days from the user
num_days: int = int(input("Enter the number of days: "))

# Variables, salary starts at 0.01 dollars (1 penny)
total_pay: float = 0
salary: float = 0.01

# Display the table header
print("Day\tSalary")
print("-------------")

# Calculate and display the salary for each day
for day in range(1, num_days + 1):
    salary *= 2
    total_pay += salary
    print(f"{day}\t${salary:,.2f}")

# Display the total pay
print("-------------")
print(f"Total Pay: ${total_pay:,.2f}")