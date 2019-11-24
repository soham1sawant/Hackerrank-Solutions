# between_two_sets.py

def getTotalX(a , b):
    l1 = []
    for i in range(a[len(a)-1] , b[0]+1): # Iterates through the values from the end of 'a' till the start of 'b' including both values
        ctr = 0                 # counter variable 
        for j in a:
            if i%j == 0:       # checks if the considered integers are divisible by the value of 'a'
                ctr += 1
        if ctr == len(a):       # checks if all the values of 'a' divide evenly with the considered intergers
            l1.append(i)    # if true then it adds the number from the considered integers to the list 'l1'
    
    l2 = []
    for i in l1:                 # Iterates through the values in 'l1'
        ctr = 0                     # counter variable
        for j in b:         # Iterates through values in 'b' 
            if j%i == 0:      # checks if the integer from 'b' divides evenly with the integer from 'l1'
                ctr += 1
        if ctr == len(b):   # checks how many values of 'b' divide with all the values of 'l1'
            l2.append(i)    # if true then adds it to list 'l2'
    
    return len(l2)          # returns the length of the list 'l1' 

if __name__ == '__main__':
    n , m = map(int , input("Enter the values of 'n' and 'm' : ").split())
    a = list(map(int , input("Enter the values of 'a' : ").rstrip().split()))
    b = list(map(int , input("Enter the values of 'a' : ").rstrip().split()))

    print(getTotalX(a , b))