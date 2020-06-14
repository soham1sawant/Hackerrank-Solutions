from itertools import combinations_with_replacement

s,k = input("Enter the values of 's' and 'k' : ").strip().split()

ans = []
for i in list(combinations_with_replacement(sorted(s), int(k))):
    print(''.join(i))