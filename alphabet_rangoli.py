# alphabet_rangoli.py

from string import ascii_lowercase

def print_rangoli(size):
    mystr = ascii_lowercase[0:size]         # takes the required string from the aplhabet
    
    for i in range(size-1 , -size , -1):
        x = abs(i)
        line = mystr[size:x:-1] + mystr[x:size]
        print('--'*x + '-'.join(line) + '--'*x)

def main():
    print()
    print("Hackerrank : Alphabet Rangoli")
    print()

    n = int(input("Enter the value of 'N' : "))
    print_rangoli(n)

main()