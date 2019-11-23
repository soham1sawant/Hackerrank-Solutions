# abbreviation.py

def abbreviation (a , b):
    s1 = ''
    s2 = ''

    for l in a:
        if l.islower() and l.upper() not in b:
            #print(l)
            s1 += l

    for l in a:
        if l not in s1:
            #print(l)
            s2 += l.upper()

    if s2 == b:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':

    q = int(input("Enter the value of 'q' : "))

    for i in range(q):
        a = input("Enter the string 'a' : ")
        b = input("Enter the string 'b' : ")
        print(abbreviation (a,b))