# compare_the_triplets.py

def compareTriplets():
    a = input("Enter Alice's triplet : ").split()
    for i in range(len(a)):
        a[i] = int(a[i])

    b = input("Enter Bob's triplet : ").split()
    for i in range(len(b)):
        b[i] = int(b[i])

    alice = 0
    bob = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            alice = alice + 1
        if a[i] < b[i]:
            bob = bob + 1
    print(alice , bob)

def main():
    print()
    print("Hackerrank : Compare the Triplets")
    print()

    compareTriplets()

main()
