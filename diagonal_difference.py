# diagonal_difference.py

import math, os, random, re, sys

def diagonalDifference(arr , n):
    l_dia = 0
    r_dia = 0
    ctr = 0                 # counter variable for counting the position of the number in a row of the array
    
    for j in arr:           # calculates the value of the left diagonal
        l_dia += j[ctr]
        ctr += 1
    
    ctr = n - 1

    for k in arr:           # calculates the value of the right diagonal
        r_dia += k[ctr]
        ctr -= 1
    
    return abs(l_dia - r_dia)


if __name__ == '__main__':
    n = int(input("Input 'n' : ").strip())
    arr = []

    for i in range(n):
        arr.append(list(map(int , input("Enter values : ").rstrip().split())))

    print(diagonalDifference(arr , n))
