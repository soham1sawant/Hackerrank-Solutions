# collections_counter.py

from collections import Counter

def compute():
    X = int(input("Enter the number of shoes : "))
    sizes = list(map(int , input("Enter the space separated list of all the sizes in the shop : ").split()))
    mylist = Counter(sizes)
    N = int(input("Enter the number of customers : "))
    total = 0
    for i in range(N):
        shoe_size , price = map(int , input("Enter the pace separated shoe size and the price : ").split())
        if shoe_size in mylist:
            if mylist[shoe_size] != 0:
                mylist[shoe_size] -= 1
                total += price
    print(total)

def main():
    print()
    print("Hackerrank : collections.counter()")
    print()

    compute()

main()
