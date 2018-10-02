# divisible_sum_pairs.py

def divisibleSumPairs(n , k , ar):
    ctr = 0
    for i in range(0 , n):
        for j in range(i+1 , n):
            if (ar[i] + ar[j]) % k == 0:
                ctr += 1
    print(ctr)



def main():
    print()
    print("Hackerrank : Divisible Sum Pairs")
    print()

    n , k = map(int , input("Enter the integer length of array ar and the integer to divide the pair sum by : ").split())
    ar = list(map(int , input("Enter the space separated integers of array ar : ").split()))

    divisibleSumPairs(n , k , ar)

main()
