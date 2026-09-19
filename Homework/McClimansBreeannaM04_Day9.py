"""
Download both program.
The modify the Day 7 program to use the Die() class in the Ch_10_
Die_ClassDefined.py file.
"""

from Ch_10_Die_ClassDefined import Die


def main():
    another = 'y'

    # define tuple for expected values.
    ExpectedProb = (0, 0, 1 / 36, 2 / 36, 3 / 36, 4 / 36, 5 / 36, 6 / 36,
                    5 / 36, 4 / 36, 3 / 36, 2 / 36, 1 / 36)

    # create two die objects
    die1 = Die()
    die2 = Die()

    while another == 'y':
        NumRoll: int = int(input('Enter number of 2-dice rolls as an integer: '))

        #Create list of 13 elements initialized to 0
        result2Die = [0] * 13

        #roll both die objects
        for x in range(NumRoll):
            die1.roll()
            die2.roll()

            #add the values of the two dice
            result = die1.get_roll() + die2.get_roll()

            #Add 1 to the position on the list
            result2Die[result] += 1

        print('Num----Total Act   Actual Pct          Expected Pct')

        for i in range(2,13,1):
            resultPct: float = result2Die[i] / NumRoll
            print(f'{i:3} - {result2Die[i]:7}    {resultPct:^7.2%}   \
                             {ExpectedProb[i]:^7.2%}')  # Pretty professional print, *not gonna lie I kept what the original program had its a bit off though*
        another = input('Another run? (y)')

if __name__ == "__main__":
    main()