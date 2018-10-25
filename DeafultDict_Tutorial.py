# DeafultDict_Tutorial.py

def compute():
    n , m = map(int , input("Enter space separated values of 'n' and 'm' : ").split())
    list = []
    for i in range(n):
        ele = input("Enter the word/character : ")
        list.append(ele)

    final_ans = []
    for i in range(m):
        ele = input("Enter the word/character : ")
        ans = ''
        for j in range(len(list)):
            if list[j] == ele:
                ans += str(j+1)+' '
        ans = ans.strip()
        if ans == '':
            final_ans.append(-1)
        else:
            final_ans.append(ans)

    for i in final_ans:
        print(i)


def main():
    print()
    print("Hackerrank : Defaultdict Tutorial")
    print()

    compute()

main()
