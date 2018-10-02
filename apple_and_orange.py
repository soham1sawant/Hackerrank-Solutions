# apple_and_orange.py

def countApplesAndOranges(s , t , a , b , apples , oranges):
    print(sum([1 for x in apples if (x + a) >= s and (x + a) <= t]))
    print(sum([1 for x in oranges if (x + a) >= s and (x +a) <= t]))

def main():
    print()
    print("Hackerrank : Apple and Orange")
    print()

    s , t = map(int , input("Enter the starting and ending locations of Sam's house : ").split())
    a , b = map(int , input("Enter the location of Apple tree and Orange Tree : ").split())
    m , n = map(int , input("Enter the number of Apples and Oranges : ").split())

    apples = list(map(int , input("Enter the distances the apples fell from the tree : ").split()))
    oranges = list(map(int , input("Enter the distances the oranges fell from the tree : ").split()))

    countApplesAndOranges(s , t , a , b , apples , oranges)

main()
