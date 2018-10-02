# plus_minus.py

def plusMinus():
    n = int(input("Enter the size of array : "))
    arr = list(map(int , input("Enter the elements of the array : ").rstrip().split()))
    pos = 0
    neg = 0
    zero = 0
    for i in arr:
        if i > 0:
            pos = pos + 1
        if i == 0:
            zero = zero + 1
        if i < 0:
            neg = neg + 1
    print("%.6f" % float(pos / n) , "%.6f" % float(neg / n) , "%.6f" % float(zero / n)  , sep = '\n')

def main():
    print()
    print("Hackerrank : Plus Minus")
    print()

    plusMinus()

main()
