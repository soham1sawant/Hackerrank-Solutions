# time_conversion.py

def timeConversion():
    s = input("Enter the time in 12 HR format : ").split(':')
    ampm = s[2][2:4]
    sec = s[2][0:2]
    if ampm == 'PM':
        if s[0] == '12':
            print('12' + ':' + s[1] + ':' + sec)
        else:
            print(str(int(s[0])+12) + ':' + s[1] + ':' + sec)
    elif ampm == 'AM':
        if s[0] == '12':
            print('00' + ':' + s[1] + ':' + sec)
        else:
            print(s[0] + ':' + s[1] + ':' + sec)

def main():
    print()
    print("Hackerrank : Time Coversion")
    print()

    timeConversion()

main()
