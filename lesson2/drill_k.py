"""
Author: Yarin Galmor
Description: Python Basics, Lesson 2, Drill K
Flow Control, Loops and Functions.
"""


def triangle_pyramid(number):
    for i in range(number):
        print()
        for j in range(number):
            if j <= i:
                print("#", end="")


def main():
    pyramid_base = int(input("Enter number for pyramid base: "))
    triangle_pyramid(pyramid_base)


if __name__ == '__main__':
    main()
