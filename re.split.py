import re

def compute():
    regex_pattern = r'[,.]+'
    print("\n".join(re.split(regex_pattern, input("Enter the string : "))))

if __name__ == "__main__":
    compute()