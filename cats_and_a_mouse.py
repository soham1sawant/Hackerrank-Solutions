# cats_and_a_mouse.py

def catAndMouse(x , y , z):
    catA = abs(x-z)     # holds the absolute value of the subtraction of 'x' and 'z'
    catB = abs(y-z)     # holds the absolute value of the subtraction of 'y' and 'z'

    if catA < catB:     # checks if value of catA is less than value of catB
        return 'Cat A'
    elif catB < catA:       # checks if value of catB is less than value of catA
        return 'Cat B'
    else:               # if both the values of catA and catB are the same
        return 'Mouse C'

if __name__ == '__main__':
    q = int(input("Enter the number of queries : "))
    
    for i in range(q):
        x , y , z = map(int , input("Enter the values of 'x' , 'y' & 'z' : ").split())
        result = catAndMouse(x , y , z)
        print(result)