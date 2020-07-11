def compute():
    n, x = map(int, input("Enter the value of 'n' and 'x' : ").strip().split())
    marks = []
    for _ in range(x):
        marks.append( list( map(float, input("Enter the marks of the subject : ").strip().split()) ) )

    studentMarks = list(zip(*marks))
    for i in studentMarks:
        print( round(sum(i)/x, 1) )

if __name__ == "__main__":
    compute()    