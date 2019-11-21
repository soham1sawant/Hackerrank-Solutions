# fibonnaci_modified.py

def fibonnaciModified(first , second , n):
    ans = [ first , second]
    for i in range(n):
        third = first + (second**2)
        ans.append(third)
        first = second
        second = third
    return ans[n - 1]

if __name__ == '__main__':
    t1 , t2 , n = map(int , input("Enter t1 , t2 , n : ").split())

    print(fibonnaciModified(t1 , t2 , n))