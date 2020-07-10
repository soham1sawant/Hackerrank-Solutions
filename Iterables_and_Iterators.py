import itertools

def compute():
    n = int(input("Enter the value of 'n' : "))
    l = input("Enter the space separated letters : ").strip().split()
    k = int(input("Enter the value of 'k' : "))

    C = list(itertools.combinations(l, k))
    F = filter(lambda c: 'a' in c, C)
    print("{0:.3}".format(len(list(F))/len(C)))

if __name__ == "__main__":
    compute()