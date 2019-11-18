# exceptions.py

def compute():
    case = int(input("Enter the number of test cases : "))

    for i in range(case):
        try:
            a , b = map(int , input("Enter the values of 'a' and 'b' : ").split())
            print(a//b)
        except BaseException as b:
            print('Error Code: ' + str(b))

def main():
    print()
    print("Hackerrank : Exceptions")
    print()

    print()

    compute()

main()