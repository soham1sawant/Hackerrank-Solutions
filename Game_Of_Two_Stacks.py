# Game_Of_Two_Stacks.py
# Practice > Data Structures > Stacks > Game Of Two Stacks

import sys

def twoStacks(x , a , b):
    a = a[::-1]
    b = b[::-1]
    ctr = 0
    sum = 0

    while sum <= x:
        if len(a) != 0:
            if a[-1] < b[-1]:
                aa = a.pop()
                if (sum + aa) <= x:
                    sum = sum + aa

        elif len(b) != 0:
            if b[-1] < a[-1]:
                bb = b.pop()
                if (sum + bb) <= x:
                    sum = sum + bb

    print(sum)
    return str(ctr)


if __name__ == '__main__':
    g = int( sys.stdin.readline().strip() )

    for i in range(g):
        n , m , x = map( int , sys.stdin.readline().strip().split() )
        a = list(map(int , sys.stdin.readline().strip().split()))
        b = list(map(int , sys.stdin.readline().strip().split()))

        result = twoStacks(x , a , b)
        _ = sys.stdout.write( result + '\n')