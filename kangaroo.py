# kangaroo.py

def kangaroo(x1 , v1 , x2 , v2):
    l1 = [ (x1 + v1)]
    for i in range(100000):
        l1.append( l1[i]+v1 )

    l2 = [ (x2 + v2)]
    for i in range(100000):
        l2.append( l2[i]+v2 )

    ctr = 0
    for i in range(100000):
        if l1[i] == l2[i]:
            ctr +=1

    if ctr>0:
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':

    x1 , v1 , x2 , v2 = map(int , input("Enter the starting position and jump distance for kangaroo 1 and 2 :  ").split())

    print(kangaroo(x1 , v1 , x2 , v2))