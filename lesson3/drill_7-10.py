"""
Author: Yarin Galmor
Description: Python Basics, Lesson 2, Drill 7-10
Flow Control, Loops and Functions.
"""


def create_words_text_file():
    name = input("Enter your name: ")

    with open("words.txt", "a") as words_text_file:
        words_text_file.write(name)


def read_words_content():
    with open("words.txt") as words_text_file:
        content = words_text_file.read()
        print(f"Files content - {content}")


def heb_text_file():
    heb_name = input("Enter your name in Hebrew: ")
    with open("words.txt", "a", encoding="utf-8") as words_text_file:
        words_text_file.write(f"\n{heb_name}")

    with open("words.txt", encoding="utf-8") as words_text_file:
        content = words_text_file.read()
        print(f"Files content including Hebrew - {content}")


def main():
    create_words_text_file()
    read_words_content()
    heb_text_file()


if __name__ == '__main__':
    main()

