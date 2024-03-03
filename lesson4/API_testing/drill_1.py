"""
Author: Yarin Galmor
Description: Python Basics, Lesson 4, Drill 1
Web automation testing - Selenium & Requests
"""
import requests


def verify_aviel_github_repos():
    github_url = "https://api.github.com/users/avielb/repos"

    response = requests.get(github_url)
    repos = response.json()
    if len(repos) >= 5:
        print("Success! There are at least 5 repositories for GitHub user avielb")
    else:
        print("Failure! Repository count is less than 5 for GitHub user avielb")


def main():
    verify_aviel_github_repos()


if __name__ == '__main__':
    main()
