# kangaroo.py

def compute(x1 , v1 , x2 , v2):
    if (x1 > x2 and v1 > v2 ) or (x1 < x2 and v1 < v2) or (v1 - v2 == 0):
        print('NO')
    if (x1 - x2) % (v2 - v2) == 0:
        print("YES")
    else:
        print('NO')

def main():
    print()
    print("Hackerrank : Kangaroo")
    print()

    x1 , v1 , x2 , v2 = map(int , input("Enter the starting position and jump distance for kangaroo 1 and 2 :  ").split())

    compute(x1 , v1 , x2 , v2)

main()
