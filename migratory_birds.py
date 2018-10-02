# migratory_birds.py

def migratoryBirds(arr):
    ctr = [0]*6
    for t in arr:
        ctr[t] += 1
    print(ctr.index(max(ctr)))


def main():
    print()
    print("Hackerrank : Migratory Birds")
    print()

    arr_count = int(input("Enter the number of birds spotted : "))
    arr = list(map(int , input("Enter the type numbers of each bird sighted : ").split()))
    migratoryBirds(arr)


main()
