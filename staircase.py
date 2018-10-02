# staircase.py

def compute():
    n = int(input("Enter the size of the staircase : "))
    f = n-1
    s = 1
    for i in range(n):
        print(' ' * f + '#' * s)
        f = f-1
        s = s + 1

def main():
    print()
    print("Hackerrank : Staircase")
    print()

    compute()

main()
