"""
12. Falling Distance

When an object is falling because of gravity, the following formula can be used
to determine the distance the object falls in a specific time period:

d=1/2 * g * t^2

The variables in the formula are as follows: d is the distance in meters, g is 9.8,
and t is the amount of time, in seconds, that the object has been falling.

Write a function named falling_distance that accepts an object's falling
time (in seconds) as an argument. The function should return the distance, in
meters, that the object has fallen during that time interval. Write a program that
calls the function in a loop that passes the values 1 through 10 as arguments
and displays the return value.
"""


def falling_distance(t: float) -> float:
    # calculate and return the distance fallen in meters
    GRAVITY: float = 9.8
    distance: float = 0.5 * GRAVITY * t ** 2
    return distance


def main():
    #calculate falling distance for time intervals from 1 to 10 seconds
    for t in range(1, 11):
        distance: float = falling_distance(t)
        print(f"Time: {t} seconds, Distance: {distance:.2f} meters")


if __name__ == "__main__":
    main()
