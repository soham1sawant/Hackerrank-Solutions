import re

def compute():
    for _ in range(int(input("Enter in value of 'n' : "))):
        Number = input("Enter the credit card number : ")
        if re.match(r"^[456]([\d]{15}|[\d]{3}(-[\d]{4}){3})$", Number) and not re.search(r"([\d])\1\1\1", Number.replace("-", "")):
            print('Invalid')
        else:
            print('Valid')

if __name__ == '__main__':
    compute()