# calendar_module.py
import calendar

def calc():
    days = ['MONDAY' , 'TUESDAY' , 'WEDNESDAY' , 'THURSDAY' , 'FRIDAY' , 'SATURDAY' , 'SUNDAY']

    mm,dd,yy = map(int,input("Enter the date : ").strip().split())
    day = calendar.weekday(yy,mm,dd)
    print(days[day])

calc()