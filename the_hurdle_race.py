# the_hurdle_race.py

def hurdleRace(k , height):
    result = max(height) - k        # computes the difference between the max. number in height and subtracts it with 'k'
    if result <= 0:         # if result is less than equal to 0 return '0'
        return 0
    else:                   # else return the result
        return result

if __name__ == '__main__':

    n , k = map(int , input("Enter the values of 'n' and 'k' : ").split())
    height = list(map(int , input("Enter the heights : ").rstrip().split()))

    result = hurdleRace(k , height)
    print(result)