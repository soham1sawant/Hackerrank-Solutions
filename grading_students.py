# grading_students.py

def gradingStudents():
    n = int(input("Enter the number of students : "))
    grades = []
    for i in range(n):
        grade = int(input("Enter the grade : "))
        grades.append(grade)

    ans = []
    for i in grades:
        if i < 38:
            ans.append(i)
        else:
            mul = ((i//5) + 1) * 5
            if (mul-i) < 3:
                ans.append(mul)
            else:
                ans.append(i)
    for i in ans:
        print(i)

def main():
    print()
    print("Hackerrank : graading Students")
    print()

    gradingStudents()

main()
