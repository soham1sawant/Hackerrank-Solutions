# sequence_equation.py

def permutationEquation(p):
    ans = []                        # list for final answers
    for i in range(1 , len(p)+1 ):
        ans.append( p.index( p.index(i)+1 )+1 )         #finds the index of the index of the value of 'i'

    return ans

if __name__ == '__main__':
    n = int(input("Enter the vaue of 'n' : "))
    p = list(map(int , input("Enter the array of integers : ").rstrip().split()))

    result = permutationEquation(p)

    print('\n'.join(map(str , result)))