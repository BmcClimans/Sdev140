"""
You have a group of friends coming to visit for your high school reunion, 
and you want to take them out to eat at a local restaurant. 
You aren’t sure if any of them have dietary restrictions, but your restaurant choices are as follows:
Write a program that asks whether any members of your party are vegetarian, vegan, or gluten-free, 
to which then displays only the restaurants to which you may take the group. 
Joe's Gourmet Burgers-Vegetarian: No, Vegan: No, Gluten-Free: No

Main Street Pizza Company-Vegetarian: Yes, Vegan: No, Gluten-Free: Yes

Mama's Fine Italian-Vegetarian: Yes, Vegan: No, Gluten-Free: No

Corner Cafe-Vegetarian: Yes, Vegan: Yes, Gluten-Free: Yes
The Chef's Kitchen-Vegetarian: Yes, Vegan: Yes, Gluten-Free: Yes
"""
#get user input for dietary restrictions
vegetarian: str = str.lower(input('Are there any vegetarians in your group (y/n)? '))
vegan: str = str.lower(input('Are there any vegans in your group (y/n)? '))
gluten_free: str = str.lower(input('Are there any gluten free in your group (y/n)? '))

#if loop to determine which restaurants are suitable based on dietary restrictions
if vegetarian == 'n' and vegan == 'n' and gluten_free == 'n':
    print("You can go to Joe's Gourmet Burgers, Main Street Pizza Company, Mama's Fine Italian, Corner Cafe, or The Chef's Kitchen.")
elif vegetarian == 'y' and vegan == 'n' and gluten_free == 'n':
    print("You can go to Main Street Pizza Company, Mama's Fine Italian, Corner Cafe, or The Chef's Kitchen.")
elif vegetarian == 'n' and vegan == 'y' and gluten_free == 'n':
    print("You can go to Corner Cafe or The Chef's Kitchen.")
elif vegetarian == 'n' and vegan == 'n' and gluten_free == 'y':
    print("You can go to Main Street Pizza Company, Corner Cafe, or The Chef's Kitchen.")
elif vegetarian == 'y' and vegan == 'y' and gluten_free == 'n':
    print("You can go to The Chef's Kitchen.")
elif vegetarian == 'y' and vegan == 'n' and gluten_free == 'y':
    print("You can go to Main Street Pizza Company, Corner Cafe, or The Chef's Kitchen.")
elif vegetarian == 'n' and vegan == 'y' and gluten_free == 'y':
    print("You can go to Corner Cafe or The Chef's Kitchen.")
elif vegetarian == 'y' and vegan == 'y' and gluten_free == 'y':
    print("You can go to The Chef's Kitchen and Corner Cafe.")