# designer_door_mat.py

def compute():
    n,m = map(int,input().split())
    oddnum = []                               # creates list for all odd numbers till 'n'      
    for i in range(1,n+1,2):                
        oddnum.append(i)
    center =  int(n/2)              #takes the center of 'n' and converts it into int

    oddnum1 = []                # creates list for collecting oddnumbers from oddnum till center
    for i in range(center):
        oddnum1.append(oddnum[i])

    #Top Part                   
    for i in oddnum1:                   # runs through oddnum1 and print the top half with center()
        print((".|."*i).center(m,'-'))
    
    #Center Part                        # prints the 'WELCOME' message at the center
    print("WELCOME".center(m,'-'))

    # Bottom Part                       # same as the top part but runs through oddnum1 in reverse order with [::-1]
    for i in oddnum1[::-1]:
        print((".|."*i).center(m,'-'))

def main():
    print()
    print("Hackerrank : Designer Door Mat")
    print()

    compute()

main()