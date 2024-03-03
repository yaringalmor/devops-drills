"""
Author: Yarin Galmor
Description: Python Basics, Lesson 2, Drill H
Flow Control, Loops and Functions.
"""


def print_name(name):
    print(f"Name: {name}")


def divide_by_two(number):
    result = int(number) / 2
    print(f"Result of dividing your number {number} by 2 - {result}")


def main():
    name = input("Enter your name: ")
    number = int(input("Enter a number: "))

    print_name(name)
    divide_by_two(number)


if __name__ == '__main__':
    main()