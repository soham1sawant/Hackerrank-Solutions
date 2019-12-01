# electronics_shop.py

def getMoneySpent(keyboards , drives , b):
    prices = []         # to store all the combination of prices of keyboards and drives
    for i in keyboards:        # iterates through keyboard array
        for j in drives:        # iterates through drives array
            if i + j <= b:      # if the price of keyboard 'i' plus drive 'j' is less than or equal to price 'b'
                prices.append(i + j)    # then add the price to list prices

    if len(prices) == 0:    # if the list prices contain no values then return '-1'
        return -1
    else:                   # else return the maximum value from prices
        return max(prices)

if __name__ == '__main__':
    b , n , m = map(int , input("Enter the values of 'b' , 'n' , 'm' : ").split())
    keyboards = list(map(int , input("Enter the prices of each keyboard model : ").rstrip().split()))
    drives = list(map(int , input("Enter the prices of each USB model : ").rstrip().split()))

    moneySpent = getMoneySpent(keyboards , drives , b)
    
    print(moneySpent)