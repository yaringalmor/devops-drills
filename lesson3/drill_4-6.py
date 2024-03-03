"""
Author: Yarin Galmor
Description: Python Basics, Lesson 3, Drill 4-6
Flow Control, Loops and Functions.
"""


def syntax_error():
    return 1 + "string"


def failing_method():
    raise RuntimeError("Raising Error")


def main():
    try:
        a = 1 / 0
        failing_method()
        syntax_error()
    except:
        print("These except block is too wide. Too broad exception clause (PyCharm note).")

    try:
        print("Error handling explanation")
    except IOError:
        print("This handler catches Disk input output related errors such as non existing files.")
    except ZeroDivisionError:
        print("This handler catches division by zero, which is an arithmetical error.")


if __name__ == '__main__':
    main()
