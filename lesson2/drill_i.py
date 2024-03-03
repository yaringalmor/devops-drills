"""
Author: Yarin Galmor
Description: Python Basics, Lesson 2, Drill I
Flow Control, Loops and Functions.
"""


def adding_numbers(number1, number2):
    return int(number1) + int(number2)


def spacing_strings(string1, string2):
    return f"{string1} {string2}"


def main():
    number1 = input("Enter the first number for numbers addition: ")
    number2 = input("Enter the second number for numbers addition: ")
    string1 = input("Enter the first string for string spacing: ")
    string2 = input("Enter the first string for string spacing: ")

    print(f"Adding numbers {number1} and {number2} - {adding_numbers(number1, number2)}")
    print(f"Spacing strings {string1} and {string2} - {spacing_strings(string1, string2)}")


if __name__ == '__main__':
    main()