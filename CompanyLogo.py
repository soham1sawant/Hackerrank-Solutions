from collections import Counter

logo = dict(Counter(sorted(input())).most_common(3))
[print(i,j) for i,j in logo.items()]