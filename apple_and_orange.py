# apple_and_orange.py

def countApplesAndOranges(s , t , a , b , apples , oranges):
    ctr1 = 0
    for apple in apples:
        apple += a                  # add the distance of the apple tree to the fallen apple
        if apple >= s and apple <= t:   # checks if the final fallen distance lies within the values of Sam's house
            ctr1 += 1                   # if yes then it increases the value of counter by 1

    ctr2 = 0
    for orange in oranges:
        orange += b                 # add the distance of the orange tree to the fallen orange
        if orange >= s and orange <= t:     # checks if the final fallen distance lies within the values of Sam's house
            ctr2 += 1                   # if yes then it increases the value of counter by 

    print(ctr1)
    print(ctr2)

if __name__ == '__main__':
    s , t = map(int, input("Enter 's' and 't' : ").split())

    a , b = map(int , input("Enter 'a' and 'b' : ").split())

    m , n = map(int , input("Enter 'm' and 'n' : ").split())

    apples = list(map(int, input("Enter the falling distance of the apples : ").rstrip().split()))
    oranges = list(map(int, input("Enter the falling distance of the oranges : ").rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)