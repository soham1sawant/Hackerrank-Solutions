def reverseArray(a):
    return a[::-1]

n = int(input("Enter the size of array : "))
arr = list(map(int, input("Enter the array : ").rstrip().split()))

res = reverseArray(arr)
print(' '.join(map(str, res)))