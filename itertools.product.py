# itertools.product.py
from itertools import product

def compute():
    a = list(map(int , input("Enter the space separated elements of list A : ").split()))
    a.sort()
    b = list(map(int , input("Enter the space separated elements of list B : ").split()))
    b.sort()

    ans = list(product(a , b))
    ans.sort()
    for i in ans:
        print(i , end = ' ')

def main():
    print()
    print("Hackerrank : itertools.product()")
    print()

    compute()

main()
