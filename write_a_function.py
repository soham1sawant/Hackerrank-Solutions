def is_leap(year):
    if year%4 == 0:
        return True
    else:
        return False

year = int(input("Enter the leap year : "))
ans = is_leap(year)
print(ans)
