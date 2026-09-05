"""
Write a program that inputs a score from zero to 100.  Use If statements to calculate grade on a ten point scale.
90-100   A
80-89     B
70-79     C
60-69     D
<60         F
"""

# Get user input for the score
score: int = int(input('Enter a score from 0 to 100: '))

# Calculate the grade based on the score using if statements
if score >= 90:
    grade: str = 'A'
elif score >= 80:
    grade: str = 'B'
elif score >= 70:
    grade: str = 'C'
elif score >= 60:
    grade: str = 'D'
else:
    grade: str = 'F'

# Output the grade
print(f'The grade for a score of {score} is: {grade}')