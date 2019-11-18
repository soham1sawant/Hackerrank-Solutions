# incorrect_regex.py

import re

def compute():
    for i in range(int(input("Enter the number of test cases : "))):
        try:
            re.compile(input("Enter the string 's' : "))
            print("True")
        except re.error:
            print("False")


def main():
    print()
    print("Hackerrank : Incorrect Regex")
    print()

    compute()

main()