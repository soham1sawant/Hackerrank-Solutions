# counting_valleys.py

def countingValleys(n , s):
    UD = {'U' : 1 , 'D' : -1}   # creates a dictioary to store the values of climb and descend
    sea_level = 0               # initializes value to 0
    valley = 0                  # variable to count the number of valleys

    for step in s:          # iterates through string s
        sea_level += UD[step]   # increases/decreases the value of sea_level depending on the character step
        if not sea_level and step == 'U':   # if we are not at sea level and the step is climb
            valley += 1             # increase the valleys by 1
    
    return valley


if __name__ == '__main__':

    n = int(input("Enter the number of steps : "))
    s = input("Enter the string 's' : ")

    result = countingValleys(n , s)
    print(result)