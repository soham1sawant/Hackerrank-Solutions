# find_angle_MBC.py
import math

def calc():
    ab = float(input("Enter length of side AB :"))
    bc = float(input("Enter length of side BC :"))

    angle = str(int(round(math.degrees(math.atan2(ab,bc))))) + '°'
    print(angle)

calc()