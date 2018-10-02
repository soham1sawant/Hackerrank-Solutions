# bon_appetit.py

def bonAppetit(bill , k , b):
    b_actual = 0
    for i in range(len(bill)):
        if i != k:
            b_actual += bill[i]

    b_actual = int(b_actual/2)

    if b-b_actual == 0:
        print('Bon Appetit')
    else:
        print(b-b_actual)


def main():
    print()
    print("Hackerrank : Bon Appetit")
    print()

    n , k = map(int , input("Enter the number of items ordered and the index if that item : ").split())
    bill = list(map(int , input("Enter the space separated integers of bill : ").split()))
    b = int(input("Enter the amount of money Brian charged Anna : "))

    bonAppetit(bill , k , b)

main()
