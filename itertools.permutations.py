# itertools.permutations.py

from itertools import permutations

def compute():
    s , k = input("Enter the string S and the value of k : ").split()
    ans = list(permutations(s , int(k)))
    ans.sort()
    for i in ans:
        str = ''
        for j in i:
            str += j
        print(str)

def main():
    print()
    print("Hackerrank : itertools.permutaions()")
    print()

    compute()

main()
