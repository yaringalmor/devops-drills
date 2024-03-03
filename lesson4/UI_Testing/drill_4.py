"""
Author: Yarin Galmor
Description: Python Basics, Lesson 4, Drill 4
Web automation testing - Selenium & Requests
"""
from selenium import webdriver


def test_ycombinator_title():
    driver = webdriver.Chrome()
    driver.get("https://www.ycombinator.com/")
    title = driver.title
    driver.quit()

    if title == "Y Combinator":
        print("Page title is as expected - Y combinator")
    else:
        print(f"Page title is not as expected - {title}")


def main():
    test_ycombinator_title()


if __name__ == '__main__':
    main()