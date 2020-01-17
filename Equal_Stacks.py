# Equal_Stacks.py
# Practice > Data Structures > Stacks > Equal Stacks

import sys

def equalStacks(h1 , h2 , h3):
    h1 = h1[::-1]
    h2 = h2[::-1]
    h3 = h3[::-1]

    equal = False
    while not equal:
        


if __name__ == '__main__':
    n1 , n2 , n3 = map( int , sys.stdin.readline().strip().split() )

    h1 = list( map( int, sys.stdin.readline().strip().split() ) )
    h2 = list( map( int, sys.stdin.readline().strip().split() ) )
    h3 = list( map( int, sys.stdin.readline().strip().split() ) )

    result = equalStacks(h1 , h2 , h3)

    _ = sys.stdout.write( result + '\n')