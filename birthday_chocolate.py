# birthday_chocolate.py

def birthday(s , d , m):
    ctr = 0
    for i in range(len(s)):
        if ((m-1) + i) < len(s):
            total = sum(s[i:m+i])
            if total == d:
                ctr += 1
    print(ctr)


def main():
    print()
    print("Hackerrank : Birthday Chocolate")
    print()

    n = int(input("Enter the number of sqaures in the chocolate bar : "))
    s = list(map(int , input("Enter the numbers on the chocolate bar : ").split()))
    d , m = map(int , input("Enter Ron's birthday and his birth month : ").split())

    birthday(s , d , m)

main()
