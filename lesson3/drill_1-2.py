"""
Author: Yarin Galmor
Description: Python Basics, Lesson 3, Drill 1-2
Error handling, Working with files and Modules.
"""


def main():
    try:
        a = 1 / 0
    except ZeroDivisionError:
        print("Caught division by zero")


if __name__ == '__main__':
    main()