# athlete_sort.py

def calculate(n,m,arr,k):
    ans = sorted(arr , key = lambda x:x[k])     # sends the key to sort on the lambda function i.e. 'k'
    for ele in ans:
        for i in ele:
            print(i, end=' ')
        print()


if __name__ == '__main__':
    n,m = map(int , input("Enter the values of 'n' & 'm' :").strip().split())
    arr = []

    for _ in range(n):
        arr.append(list(map(int , input("Enter the array : ").rstrip().split())))

    k = int(input("Enter the value of 'k' : "))

    calculate(n,m,arr,k)