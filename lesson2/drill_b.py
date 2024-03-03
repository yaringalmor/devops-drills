"""
Author: Yarin Galmor
Description: Python Basics, Lesson 2, Drill B
Flow Control, Loops and Functions.
"""


def iterate():
    iterations = 5

    print("Option 1")
    for i in range(iterations):
        print(f"Iteration index - {i + 1}")  # range first number starts with zero

    print("\nOption 2")
    for j in range(1, iterations + 1):
        print(f"Iteration index - {j}")


def main():
    iterate()


if __name__ == '__main__':
    main()
