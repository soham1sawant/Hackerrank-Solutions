# Balanced_Brackets.py
# Practice > Data Structures > Stacks > Balanced Brackets

import sys

def isBalanced(str):
    stack = []
    table = { ")" : "(" , "}" : "{" , "]" : "[" }

    for symbol in str:
        if not stack:
            stack.append(symbol)
        elif symbol not in table:
            stack.append(symbol)
        elif table[symbol] == stack[-1]:
            stack.pop()
        else:
            stack.append(symbol)

    if stack:
        return 'NO'
    else:
        return 'YES'

if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())

    for i in range(n):
        s = sys.stdin.readline().strip()
        result = isBalanced(s)

        _ = sys.stdout.write( result + '\n')