from sympy import *


def compute():
    x, k = map(int, input("Enter the values of 'x' & 'k' : ").strip().split())
    p = sympify(input("Enter the polynomial 'P' : "))

    return (p.subs('x',x) == k)

ans = compute()
print(ans)