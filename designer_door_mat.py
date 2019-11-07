# designer_door_mat.py

def compute():
    n,m = map(int,input().split())
    oddnum = []                                     
    for i in range(1,n+1,2):                
        oddnum.append(i)
    center =  round(n/2)

    oddnum1 = []
    for i in range(0,center-1):
        oddnum1.append(oddnum[i])
    print(oddnum1)

    #Top Part
    for i in oddnum1:
        print((".|."*i).center(m,'-'))

    #Center Part
    print("WELCOME".center(m,'-'))

    # Bottom Part
    for i in oddnum1[::-1]:
        print((".|."*i).center(m,'-'))

def main():
    print()
    print("Hackerrank : Designer Door Mat")
    print()

    compute()

main()