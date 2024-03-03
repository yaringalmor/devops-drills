"""
Author: Yarin Galmor
Description: Python Basics, Lesson 2, Drill M
Flow Control, Loops and Functions.
"""

def get_number_from_user():
    number = input("Enter a number: ")
    return int(number)


def sum_digits():
    number = get_number_from_user()
    result = 0

    for digit in str(number):
        result += int(digit)
    return result

    # Option 2 (Using list comprehension)- return sum([int(digit) for digit in str(number)])


def main():
    print(f"Result of sum up digits - {sum_digits()}")


if __name__ == '__main__':
    main()
