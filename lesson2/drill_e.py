"""
Author: Yarin Galmor
Description: Python Basics, Lesson 2, Drill E
Flow Control, Loops and Functions.
"""


def print_variables(age, letter, currency, has_flew_abroad, apartment_number):
    print(f"Age: {age}\n"
          f"First letter of last name: {letter}\n"
          f"Shekel - Dollar currency: {currency}\n"
          f"Flew abroad: {has_flew_abroad}\n"
          f"Apartment number: {apartment_number}\n")


def add_currency_with_age(currency, age):
    print(f"Result of adding currency to age - {float(currency) + int(age)}")


def main():
    age = input("Enter your age: ")
    letter = input("Enter the first letter of your last name: ")
    currency = 3.6
    has_flew_abroad = bool(input("Have you flew abroad (true/false)? ").lower() == 'true')
    apartment_number = input("Enter your apartment number: ")

    print_variables(age, letter, currency, has_flew_abroad, apartment_number)
    add_currency_with_age(currency, age)


if __name__ == '__main__':
    main()
