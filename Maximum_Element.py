# Maximum_Element.py
# Practice > Data Structures > Stacks > Maximum Element

import sys

items = [0]

for i in range(int(sys.stdin.readline().strip())):
    nums = list(map(int , sys.stdin.readline().strip().split()))

    if nums[0] == 1:
        items.append( max(nums[1] , items[-1] ))      # compares the item and the last item of the list and appends the maximum between the two
    elif nums[0] == 2:
        items.pop()
    else:
        _ = sys.stdout.write( str(items[-1]) + '\n')