"""
Author: Yarin Galmor
Description: Python Basics, Lesson 2, Drill D
Flow Control, Loops and Functions.
"""


def what_will_happen():
    count = 1
    while count < 11:
        print(count)
        count = count + 1
    print(f"\nLast print is {count - 1}")


def main():
    what_will_happen()


if __name__ == '__main__':
    main()
