# day_of_the_programmer.py

def dayOfProgrammer(year):
    if year==1918:
        print('26.09.1918')

    elif ((year<=1917) and (year%4==0)) or ((year>1918) and (year%400==0)) or ((year%4==0) and(year%100!=0)):
        print('12.09.%s'%year)

    else:
        print('13.09.%s'%year)
    
def main():
    print()
    print("Hackerrank : Day Of Programmer")
    print()

    year = int(input("Enter the year : "))
    dayOfProgrammer(year)

main()
