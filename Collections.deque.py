from collections import deque

def compute():
    n = int(input("Enter the value of 'n' : "))
    d = deque()
    for i in range(n):
        method = input("Enter the command :").strip()
        if method == 'pop':
            d.pop()
        elif method == 'popleft':
            d.popleft()
        else:
            method, value = method.split()
            value = int(value)
        
            if method == 'append':
                d.append(value)
                
            if method == 'appendleft':
                d.appendleft(value)
    
    for i in list(d):
        print(i, end=" ")

if __name__ == "__main__":
    compute()
