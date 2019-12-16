# viral_advertising.py

def viralAdvertising(n):
    total = 2
    liked = 2

    for _ in range(n-1):
        liked = liked * 3//2
        total += liked
    
    return total


if __name__ == '__main__':

    n = int(input("Enter the number of days : "))

    result = viralAdvertising(n)
    print(result)