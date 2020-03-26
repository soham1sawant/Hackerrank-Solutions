# any_or_all.py

def calc():
    n = int(input("Enter the value of 'n' : "))
    arr = input("enter the numbers : ").strip().split()
    print(all([int(i)>0 for i in arr]) and any([i==i[::-1] for i in arr]))

calc()

