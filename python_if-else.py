n = int(input("Enter a number: "))

if n%2 != 0:
    print("Wierd")
elif n%2 == 0 and n>1 and n<6:
    print("Not Wierd")
elif n%2 == 0 and n>5 and n<21:
    print("Wierd")
elif n%2 == 0 and n>20:
    print("Not Wierd")
