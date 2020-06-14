# itertools.combinations.py

from itertools import *

def compute():
    S , k = input("Enter the string S and the value of k : ").split()

    for i in range(1, int(k)+1):
        for c in combinations(sorted(S), i):
            print(''.join(c))

def main():
    print()
    print("Hackerrank : itertools.combinations()")
    print()

    compute()

main()
