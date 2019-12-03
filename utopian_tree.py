# utopian_tree.py

def utopianTree(n):
    height = 0
    for i in range(n):
        if i%2 == 0:
            height += 1
        else:
            height  = height * 2
    
    return height

if __name__ == '__main__':

    t = int(input("Enter the number of test cases : "))

    for i in range(t):
        n = int(input("Enter the number of cycles : "))
        result = utopianTree(n)
        print(result)