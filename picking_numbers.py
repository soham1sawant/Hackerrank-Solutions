# picking_numbers.py

def pickingNumbers(s):
    arr  = [s[0]]
    for i in range(1 , len(s)):
        if abs(s[i-1] - s[i]) <= 1:
            print(abs(s[i-1] - s[i]))           # to remove
            arr.append(s[i])
    print(arr)

if __name__ == '__main__':

    n = int(input("Enter the size of the array : ").strip())
    a = list(map(int , input("Ente the array : ").rstrip().split()))
    

    result = pickingNumbers(a)