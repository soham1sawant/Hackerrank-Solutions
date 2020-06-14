# Collections.namedtuple().py

from collections import namedtuple

n = int(input("Enter the number of students : "))
student = namedtuple('student', input())
total = 0

for _ in range(n):
    Student = student(*input().split())
    total += int(Student.MARKS)

print('{:.2f}'.format(total/n)) 