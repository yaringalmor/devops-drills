"""
Author: Yarin Galmor
Description: Python Basics, Lesson 4, Drill 2
Web automation testing - Selenium & Requests
"""
import requests


def test_agify_api():
    names = ["Alice", "Bob", "Charlie"]
    for name in names:
        response = requests.get(f"https://api.agify.io/?name={name}")
        data = response.json()
        age = int(data["age"])

        if 0 <= age <= 120:
            print(f"Age for name '{name}' is between 0 and 120 - {age}")
        else:
            print(f"Age for name '{name}' is out of 0-120 range - {age}")


def main():
    test_agify_api()


if __name__ == '__main__':
    main()