# abbreviation.py

def abbreviation (a , b):
    a = a.upper()
    newA = ''

    for l in a:
        if l in b:
            newA += l

    if newA == b:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':

    q = int(input("Enter the value of 'q' : "))

    for i in range(q):
        a = input("Enter the string 'a' : ")
        b = input("Enter the string 'b' : ")
        print(abbreviation (a,b))