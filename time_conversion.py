# time_conversion.py

def timeConversion():
    s = input("Enter the time in 12 HR format : ")              # spilts the string into hours, minutes and seconds
    if 'AM' in s:                                               # checks if the time is AM
        if s == '12:00:00AM':
            return '00:00:00'
        elif s[0:2] == '12':
            return '00'+s[2:8]
        else:
            return s[0:8]


    else:                                                       # checks if the time is PM
        if s == '12:00:00PM':
            return'12:00:00'
        elif s[0:2] == '12':
            return '12'+s[2:8]
        else:
            s = s.split(':')
            time = str(int(s[0])+12) + ':' + s[1] + ':' + s[2][0:2]
            return time

def main():
    print()
    print("Hackerrank : Time Coversion")
    print()

    print(timeConversion())

main()
