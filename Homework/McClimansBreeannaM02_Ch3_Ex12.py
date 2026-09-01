"""
A software company sells a package that retails for $99. 
Quantity discounts are given according to the following table:
Quantity Discount 10-19 10%
Quantity Discount 20-49 20%
Quantity Discount 50-99 30%
Quantity Discount 100 or more 40%
Write a program that asks the user to enter the number of packages purchased. 
The program should then display the amount of the discount (if any) and the total amount of the purchase after the discount.
"""
#Constant to hold the price of a single package
PACKAGE_PRICE:float = 99.00

#get user input for number of packages purchased
packages_purchased:int = int(input("Enter the number of packages purchased: "))

#Calculate the discount based on the number of packages purchased
if packages_purchased >= 100:
    discount = 0.40
elif packages_purchased >= 50:
    discount = 0.30
elif packages_purchased >= 20:
    discount = 0.20
elif packages_purchased >= 10:
    discount = 0.10
else:
    discount = 0.0  

#Calculate the total amount before discount
total_before_discount:float = packages_purchased * PACKAGE_PRICE

#Calculate the discount amount
discount_amount:float = total_before_discount * discount

#Calculate the total amount after discount
total_after_discount:float = total_before_discount - discount_amount

#Display the results
print(f"Packages purchased: {packages_purchased}")
print(f"Total cost before discount: ${total_before_discount:,.2f}")
print(f"Discount: ${discount_amount:,.2f}")
print(f"Total cost after discount: ${total_after_discount:,.2f}")