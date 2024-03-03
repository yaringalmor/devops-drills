"""
Author: Yarin Galmor
Description: Python Basics, Lesson 2, Drill A
Flow Control, Loops and Functions.
"""


def compare_numbers(x, y):
    if x > y:
        print("BIG")
    elif x < y:
        print("small")


def main():
    x = input("Enter a number for variable x: ")
    y = input("Enter a number for variable y: ")
    compare_numbers(x, y)


if __name__ == '__main__':
    main()
