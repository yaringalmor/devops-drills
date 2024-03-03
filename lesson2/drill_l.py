"""
Author: Yarin Galmor
Description: Python Basics, Lesson 2, Drill L
Flow Control, Loops and Functions.
"""


def x_pyramid(number):
    for i in range(number + 1):
        print()
        for j in range(number + 1):
            if j == i or j == number - i:
                print("#", end="")
            else:
                print(" ", end="")


def main():
    pyramid_base = int(input("Enter number for pyramid base: "))
    x_pyramid(pyramid_base)


if __name__ == '__main__':
    main()
