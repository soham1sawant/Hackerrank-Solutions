# polar_coordinates.py

import cmath

def calc():
    r = complex(input("Enter complex number :").strip())
    print(cmath.polar(r)[0])
    print(cmath.polar(r)[1])

calc()