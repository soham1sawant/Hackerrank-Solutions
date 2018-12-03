# mod_divmod.py

def compute():
    a = int(input("Enter the value of a : "))
    b = int(input("Enter the value of b : "))

    print(a//b)
    print(a%b)
    print(divmod(a , b))

def main():
    print()
    print("Hackerrank : Mod Divmod")
    print()

    compute()

main()