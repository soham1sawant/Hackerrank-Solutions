# itertools.combinations.py

from itertools import combinations

def compute():
    S , k = input("Enter the string S and the value of k : ").split()
    ans = list(combinations(S , int(k)))
    ans.sort()
    S = list(S)
    S.sort()
    for i in ans:
        S.append(i)
    for i in S:
        str = ''
        for j in i:
            str +=j
        print(str)

def main():
    print()
    print("HAckerrank : itertools.combinations()")
    print()

    compute()

main()
