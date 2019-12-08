# angry_professor.py

def angryProfessor(k , a):
    ontime = []
    for i in a:
        if i <=0:
            ontime.append(i)
    
    if len(ontime) == k or len(ontime) > k:
        return 'NO'
    else:
        return 'YES'

if __name__ == '__main__':
    t = int(input("Enter the number of test cases : "))

    for _ in range(t):
        n , k = map(int , input("Enter the values of 'n' & 'k' : ").split())
        a = list( map(int , input("Enter the arrival times of each student : ").rstrip().split()) )
        
        result = angryProfessor(k , a)
        print(result)