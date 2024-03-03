"""
Author: Yarin Galmor
Description: Python Basics, Lesson 2, Drill C
Flow Control, Loops and Functions.
"""


def select_season(season_index):
    if season_index == 1:
        print('summer')
    elif season_index == 2:
        print('winter')
    elif season_index == 3:
        print('fall')
    elif season_index == 4:
        print('spring')


def main():
    season_index = int(input("Select season index by value of 1 to 4 - "))
    select_season(season_index)


if __name__ == '__main__':
    main()
