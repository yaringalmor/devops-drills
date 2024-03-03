"""
Author: Yarin Galmor
Description: Python Basics, Lesson 4, Drill 3
Web automation testing - Selenium & Requests
"""
import requests


def test_universities_api():
    response = requests.get("http://universities.hipolabs.com/search?country=Israel")
    universities = response.json()
    universities_names = [uni['name'] for uni in universities]

    if len(universities) >= 5:
        print(f"There are more than 5  universities in Israel\n")
    else:
        print(f"Israel currently has less than 5 universities\n")

    for index, uni_name in enumerate(universities_names):
        print(f'{index}. {uni_name}')


def main():
    test_universities_api()


if __name__ == '__main__':
    main()