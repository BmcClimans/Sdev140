"""
Write a program that predicts the approximate size of a population of organisms. 
The application should prompt the user to enter the starting number of organisms, the average daily population increase (as a percentage), 
and the number of days the organisms will be left to multiply. For example, assume the user enters the following values:
Starting number of organisms: 2Average daily increase: 30%Number of days to multiply: 
The program should display the following table of data:
Day Approximate Population
1   2
2   2.6
3   3.38
4   4.394
5   5.7122
6   7.42586
7   9.653619
8   12.5497
9   16.31462
10  21.209
"""

organism_input: str = input('Starting number of organisms: ')
while organism_input.isdigit() == False or int(organism_input) <= 0:
    print('Please enter an integer greater than 0!')
    organism_input: str = input('Starting number of organisms: ')

start_num_organims: int = int(organism_input)

avg_daily_increase_input: str = input('Average daily increase as an integer representing a percentage (e.g. 30 for 30%): ')
while avg_daily_increase_input.isdigit() == False or int(avg_daily_increase_input) < 1:
    print('Please enter an integer greater than 0!')
    avg_daily_increase_input: str = input('Enter  the average daily increase as an integer representing a percentage (e.g. 30 for 30%): ')

avg_daily_increase: float = 1 + int(avg_daily_increase_input) / 100

num_days_input: str = input('Enter the number of days to multiply: ')
while num_days_input.isdigit() == False or int(num_days_input) <= 0:
    print('Please enter an integer greater than 0!')
    num_days_input: str = input('Enter the number of days to multiply: ')

num_days: int = int(num_days_input)

print('Day Approximate Population')
for day_num in range(num_days):
    print(day_num + 1, (day_num + 1) * avg_daily_increase)