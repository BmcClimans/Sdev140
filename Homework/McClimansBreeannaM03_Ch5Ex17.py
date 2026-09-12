"""
This exercise assumes that you have already written the  function in Programming Exercise 16.
Write another program that displays all of the prime numbers from 1 to 100. The program should have a loop that calls the is_prime function.
"""


def is_prime(number: int) -> bool:
    #return True if n is a prime number, otherwise return False
    if number < 2:
        return False
    for divisor in range(2, number):
        if number % divisor == 0:
            return False
    return True


def main() -> None:
   #display all prime numbers from 1 to 100
    print("Prime numbers from 1 to 100:")

    for num in range(1, 101):
        if is_prime(num):
            print(num)

if __name__ == "__main__":
    main()