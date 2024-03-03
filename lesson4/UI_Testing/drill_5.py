"""
Author: Yarin Galmor
Description: Python Basics, Lesson 4, Drill 5
Web automation testing - Selenium & Requests
"""

from selenium import webdriver


def test_dockerhub_title():
    driver = webdriver.Chrome()
    driver.get("https://hub.docker.com")
    title = driver.title
    driver.quit()

    if title == "Docker Hub Container Image Library | App Containerization":
        print("Page title is as expected")
    else:
        print(f"Page title is not as expected - {title}")


def main():
    test_dockerhub_title()


if __name__ == '__main__':
    main()