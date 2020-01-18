# Equal_Stacks.py
# Practice > Data Structures > Stacks > Equal Stacks

import sys

def equalStacks(h1 , h2 , h3):
    h11 = [0 , h1.pop() ]
    while len(h1) > 0:
        h11.append( h11[-1] + h1.pop() )

    h22 = [0 , h2.pop() ]
    while len(h2) > 0:
        h22.append( h22[-1] + h2.pop() )

    h33 = [0 , h3.pop() ]
    while len(h3) > 0:
        h33.append( h33[-1] + h3.pop() )

    equal = False
    while not equal:
        if h11[-1] == h22[-1] == h33[-1]:
            equal = True
            break
        else:
            if h11[-1] > h22[-1] and h11[-1] > h33[-1] and len(h11) != 0:
                h11.pop()
            elif h22[-1] > h11[-1] and h22[-1] > h33[-1] and len(h22) != 0:
                h22.pop()
            elif h33[-1] > h11[-1] and h33[-1] > h22[-1] and len(h33) != 0:
                h33.pop()
    
    return str(h11[-1])

if __name__ == '__main__':
    n1 , n2 , n3 = map( int , sys.stdin.readline().strip().split() )

    h1 = list( map( int, sys.stdin.readline().strip().split() ) )
    h2 = list( map( int, sys.stdin.readline().strip().split() ) )
    h3 = list( map( int, sys.stdin.readline().strip().split() ) )

    result = equalStacks(h1 , h2 , h3)

    _ = sys.stdout.write( result + '\n')