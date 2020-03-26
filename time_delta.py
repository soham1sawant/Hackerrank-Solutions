# time_delta.py
from dateutil import parser

def time_delta(t1 , t2):
    t1 = parser.parse(t1)
    t2 = parser.parse(t2)

    ans = abs(int((t1-t2).total_seconds()))
    return ans                                  # return str(ans) in the online editor of Hackerrank


if __name__ == '__main__':
    t = int(input("Enter the no. of test cases : "))

    for i in range(t):
        t1 = input("Enter the 1st input : ").strip()
        t2 = input("Enter the 2nd input : ").strip()

        delta = time_delta(t1,t2)
        print(delta)