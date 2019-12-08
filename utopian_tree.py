# utopian_tree.py

def utopianTree(n):
    height = 0

    for i in range(n+1):
        if i == 0:
            height += 1
        else:
            if i%2 != 0:
                height  = height * 2
            else:
                height += 1
    
    return height

if __name__ == '__main__':

    t = int(input("Enter the number of test cases : "))

    for i in range(t):
        n = int(input("Enter the number of cycles : "))
        result = utopianTree(n)
        print(result)