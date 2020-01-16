# Maximum_Element.py
# Practice > Data Structures > Stacks > Maximum Element

import sys
class Stack:

    def __init__(self):
        self.items = []

    def push(self , item):
        self.items.append(item)

    def delete(self):
        self.items.pop()

    def is_empty(self):
        return self.items == []

    def maximum(self):
        return max(self.items)

st = Stack()

n = int(sys.stdin.readline().strip())

for i in range(n):
    query = list(map(int , sys.stdin.readline().strip().split()))
    
    if query[0] == 1:
        st.push( query[1])
    elif query[0] == 2:
        if not st.is_empty():
            st.delete()
    elif query[0] == 3:
        _ = sys.stdout.write(str(st.maximum()) + '\n')