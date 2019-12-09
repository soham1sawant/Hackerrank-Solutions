# beautiful_days_at_the_movies.py

def beautifulDays(i , j , k):
    ctr = 0                     # counter variable for counting the whole numbers 
    for num in range(i , j+1):
        reverse = int( str(num)[::-1] )     # computes the reverse of 'num'

        if (abs(num - reverse) / k) % 1 == 0:   # cheecks if 'num' - 'reverse' divided by 'k' is a whole number
            ctr += 1
    
    return ctr

if __name__ == '__main__':
    i , j , k = map(int , input("Enter the values of 'i' , 'j' & 'k' : ").split())

    result = beautifulDays(i,j,k)

    print(result)