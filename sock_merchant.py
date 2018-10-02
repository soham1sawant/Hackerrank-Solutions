# sock_merchant.py

def sockMerchant(n , ar):
    l = dict()
    for i in ar:
        if i in l:
            l[i] += 1
        else:
            l[i] = 1
    pair = 0
    for i in l:
        pair += l[i]//2
    print(pair)

def main():
    print()
    print("Hackerrank : Sock Merchant")
    print()

    n = int(input("Enter the number of socks : "))
    ar = list(map(int , input("Enter the colours of the socks in the pile : ").split()))
    sockMerchant(n , ar)

main()
