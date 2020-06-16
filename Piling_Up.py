from collections import deque

def compute():
    t = int(input("Enter the number of test cases : ").strip())

    for _ in range(t):
        n = int(input("Enter the number of cubes : "))
        data = deque( list(map(int , input("Enter the space seperated side lengths of each cube : ").strip().split())) )

        stack = []
        check = True
        while (data != []) or check:
            if stack != []:
                