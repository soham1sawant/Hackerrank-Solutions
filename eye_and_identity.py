# eye_and_identity.py

import numpy
numpy.set_printoptions(sign = ' ')

def compute():
    n , m = map(int , input("Enter the space separated values of N and M : ").split())
    
    print(numpy.eye(n , m , k = 0))

def main():
    print()
    print("Hackerrank: Eye and Identity")
    print()

    compute()

main()